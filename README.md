# N-Zero Arithmetic (NZA)

[![PyPI version](https://badge.fury.io/py/nza-arithmetic.svg)](https://badge.fury.io/py/nza-arithmetic)
[![Tests](https://github.com/super-morphist-sukezo/nza-arithmetic/actions/workflows/tests.yml/badge.svg)](https://github.com/super-morphist-sukezo/nza-arithmetic/actions)

Rigorous mathematical framework for the \&quot;No-Zero Universe\&quot; interpretation. Distinguishes *local labels* (including 0_local, negatives) from invariant infinite *universe total* (∞).

## Installation

```bash
pip install nza-arithmetic
```

## Quick Start

```python
from nza import NZA

a = NZA(5)
b = NZA(3)
print(a - b)  # 2.0_local + ∞_universe

zero = NZA(0)
print(a / zero)  # ∞_universe

print(NZA(5) - NZA(5))  # 0.0_local + ∞_universe  (no annihilation!)
```

## Features

- Full arithmetic ops: +, -, *, / (div/0 → ∞_universe)
- Comparisons on local labels
- Rich repr showing local + ∞_universe
- Type hints, tests, PyPI-ready

## Theory

See the [full thesis](https://github.com/super-morphist-sukezo/nza-arithmetic/blob/main/docs/nza-full-thesis-v4_super-morphist-sukezo.md) for axioms, proofs, Morphidism integration.

## Development

```bash
git clone https://github.com/super-morphist-sukezo/nza-arithmetic
cd nza-arithmetic
pip install -e .[dev]
pytest
```

## License

MIT