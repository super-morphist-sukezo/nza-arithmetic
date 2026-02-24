from typing import Union, Any
import math

class NZA:
    """
    N-Zero Arithmetic (NZA) number: (local_label, ∞_universe).
    
    All operations act on the local label, preserving the infinite universe total.
    Total value is always ∞, local is for computation/labels.
    
    Example:
        >>> a = NZA(5)
        >>> b = NZA(3)
        >>> a - b
        2.0_local + ∞_universe
        >>> NZA(1) / NZA(0)
        ∞_universe
    """
    
    def __init__(self, local: Union[int, float] = 0) -> None:
        self._local = float(local)
    
    @property
    def local(self) -> float:
        """Local label."""
        return self._local
    
    @property
    def universe(self) -> float:
        """Invariant infinite universe total."""
        return math.inf
    
    def total(self) -> float:
        """Always ∞ (local + universe)."""
        return self.universe  # local absorbed into inf
    
    def __repr__(self) -> str:
        if math.isinf(self.local) and self.local > 0:
            return "∞_universe"
        elif math.isinf(self.local) and self.local < 0:
            return "-∞_local + ∞_universe"
        else:
            return f"{self.local}_local + ∞_universe"
    
    def __add__(self, other: Any):
        if isinstance(other, NZA):
            return NZA(self.local + other.local)
        return NotImplemented
    
    def __radd__(self, other: Any):
        return self + NZA(other)
    
    def __sub__(self, other: Any):
        if isinstance(other, NZA):
            return NZA(self.local - other.local)
        return NotImplemented
    
    def __rsub__(self, other: Any):
        return NZA(other) - self
    
    def __mul__(self, other: Any):
        if isinstance(other, NZA):
            return NZA(self.local * other.local)
        return NotImplemented
    
    def __rmul__(self, other: Any):
        return self * NZA(other)
    
    def __truediv__(self, other: Any):
        if isinstance(other, NZA):
            if other.local == 0:
                return NZA(math.inf)
            return NZA(self.local / other.local)
        return NotImplemented
    
    def __rtruediv__(self, other: Any):
        return NZA(other) / self
    
    def __neg__(self):
        return NZA(-self.local)
    
    def __pos__(self):
        return self
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, NZA):
            return self.local == other.local
        elif isinstance(other, (int, float)):
            return self.local == float(other)
        return False
    
    def __ne__(self, other: Any) -> bool:
        return not self == other
    
    def __lt__(self, other: Any) -> bool:
        if isinstance(other, NZA):
            return self.local < other.local
        return self.local < float(other)
    
    def __le__(self, other: Any) -> bool:
        return self < other or self == other
    
    def __gt__(self, other: Any) -> bool:
        if isinstance(other, NZA):
            return self.local > other.local
        return self.local > float(other)
    
    def __ge__(self, other: Any) -> bool:
        return self > other or self == other
