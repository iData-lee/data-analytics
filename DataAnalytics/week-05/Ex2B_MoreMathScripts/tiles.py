# Tile room dimensions are length by width feet.
# There are 12 tiles per box, each 1 foot by 1 foot
# Can only buy full boxes not partial. How many do we need?
# Buy at least 10% more tiles than needed to handle mess ups

length = 1 
width = 1

import math

tiles = length * width
boxes_needed = math.ceil(tiles / 12)
total_boxes = math.ceil(tiles * 1.10 / 12)
# Need to troubleshoot