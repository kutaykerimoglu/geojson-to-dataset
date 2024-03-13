import random
from shapely.geometry import Point, Polygon, MultiPolygon

def get_random_point_in_polygon(polygon: Polygon) -> Point:
  min_x, min_y, max_x, max_y = polygon.bounds
  print(polygon.bounds)
  while True:
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    print(f'random point sampled {x}, {y}')
    p = Point(x, y)
    if polygon.contains(p):
      return p

def get_random_point_in_multipolygon(multipolygon: MultiPolygon) -> Point:
    random_polygon = random.choice(multipolygon.geoms)
    return get_random_point_in_polygon(random_polygon)

def get_random_point_in_geometry(geometry) -> Point:
   if isinstance(geometry, Polygon):
      return get_random_point_in_polygon(geometry)
   elif isinstance(geometry, MultiPolygon):
      return get_random_point_in_multipolygon(geometry)
   else:
      raise Exception(f'Unsupported Geometry Exception ({geometry})')