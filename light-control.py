import board
import neopixel
import sys
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--on", action='store_true')
group.add_argument("--off", action='store_true')
parser.add_argument("--brightness", "-b", type=int)
args = parser.parse_args()

pixels = neopixel.NeoPixel(board.D18, 12, pixel_order=neopixel.GRBW)


if args.on:
    if args.brightness:
        pixels.fill((0,0,0,args.brightness))
    else:
        pixels.fill((0,0,0,30))

if args.off:
    pixels.fill((0,0,0,0))