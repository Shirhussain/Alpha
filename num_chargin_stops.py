# at at my first read i thought it is similar to coin change or Climbing Stairs which I have solved before here:
# https://github.com/Shirhussain/Algorithm_by_shir/blob/main/Dynamic_programming/out/coin_chagne.py
# https://github.com/Shirhussain/Algorithm_by_shir/blob/main/recursion/out/climb_staris.py
# but then i realized that it is not the same, because we can skip charging if we don't need to
# and we can charge more than once
from typing import List
def num_charging_stops(legs: List[int], capacity: int) -> int:
  """Calculates the number of necessary charging stops to reach the destination.

  Each "leg" of your journey represents the amount of energy required to drive
  that leg of the trip. For example, if a leg has a value of 5 and your
  battery's energy level before driving the leg is 12, then driving that leg
  will drop the battery's energy level to 7 (12-5). After driving each leg, you
  have the choice of whether to charge or not. If you decide to charge, your
  battery's energy level get's returned to "capacity". If you decide not to
  charge, your battery's energy level is unchanged. The goal is to calculate
  the minimum number of charging stops needed to reach the destination without
  ever letting your battery's level fall below 0. If it isn't possible to reach
  the destination with the given inputs, -1 should be returned.

  Assume that your battery is charged to full capacity to start.

  Examples:
    num_charging_stops([25], 30) -> 0
    num_charging_stops([25, 25], 30) -> 1
    num_charging_stops([50], 30) -> -1
    num_charging_stops([15, 15, 30]) -> 1
    num_charging_stops([15, 30, 15]) -> 2
  """
  
  if any(leg > capacity for leg in legs):
      return -1
  
  stops = 0
  current_energy = capacity
  
  for i in range(len(legs) -1):
      current_energy -= legs[i]
      
      if current_energy < legs[i+1]:
          stops += 1
          current_energy = capacity

  # Process last leg
  current_energy -= legs[-1]
  if current_energy < 0:
      stops += 1

  return stops

  
print(num_charging_stops([25], 30))
print(num_charging_stops([25, 25], 30))
print(num_charging_stops([50], 30))
print(num_charging_stops([15, 15, 30], 30))
print(num_charging_stops([15, 30, 15], 30))
