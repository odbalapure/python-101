from math import hypot
from typing import List

# If we’re only trying to calculate the perimeter of one polygon in the context 
# of a much greater problem, using a function will probably be the quickest to 
# code and easier to use one time only. On the other hand, if our program needs 
# to manipulate numerous polygons in a wide variety of ways (calculating the perimeter, 
# area, and intersection with other polygons, moving or scaling them, and so on), we have 
# almost certainly identified a class of related objects.

def distance(p_1, p_2):
  return hypot(p_1[0]-p_2[0], p_1[1]-p_2[1]) 
  
def perimeter(polygon):
  pairs = zip(polygon, polygon[1:]+polygon[:1])
  return sum (
    distance(p1, p2) for p1, p2 in pairs
  )

square = [(1,1), (1,2), (2,2), (2,1)]
print(perimeter(square))

class Point:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

  def distance(self, other: "Point") -> float:
    return hypot(self.x - other.x, self.y - other.y)

class Polygon:
  def __init__(self, vertices) -> None:
    self.vertices: List[Point] = list(vertices) if vertices else []
      
  def perimeter(self) -> float:
    pairs = zip(
      self.vertices, self.vertices[1:] + self.vertices[:1])
    return sum(p1.distance(p2) for p1, p2 in pairs)

square = Polygon([Point(1,1), Point(1,2), Point(2,2), Point(2,1)])
print(square.perimeter())

# NOTE:
# One size does not fit all. The built-in, generic collections and functions 
# work well for a large number of simple cases. A class definition works well 
# for a large number of more complex cases. The boundary is hazy at best.
