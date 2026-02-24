#!/usr/bin/env python3
from nza import NZA

print(\"NZA Demo:\")

apples = NZA(5)
eaten = NZA(5)
empty_box = apples - eaten
print(f\"Box after eating: {empty_box}\")  # 0.0_local + ∞_universe (apples in universe)

three_minus_five = NZA(3) - NZA(5)
print(f\"3 - 5: {three_minus_five}\")  # -2.0_local + ∞_universe

div_zero = NZA(1) / NZA(0)
print(f\"1 / 0: {div_zero}\")  # ∞_universe

print(\"All totals: ∞ (conservation holds!)\")
