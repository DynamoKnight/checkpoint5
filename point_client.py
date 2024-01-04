# this client file is provided for you
# no changes necessary
from point import Point


def main():
  p = Point(1, 2)
  print(p.get_x())    # 1
  p.set_y(4)
  print(p.display())  # '(1, 4)'


if __name__ == '__main__':
  main()