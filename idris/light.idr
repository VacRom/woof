module trafficLight

data trafficLight =
  red |
  green |
  yellow

cc: trafficLight -> trafficLight
cc red = green
cc green = yellow
cc yellow = red
