# coding=utf-8

import numpy
import requests
import json
from os import path
from PIL import Image, ImageDraw, ImageFont
from StringIO import StringIO
import textwrap

WIDTH = 264
HEIGHT = 176
URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city=140010"
FONT_SIZE = 18
FONT_PATH = path.dirname(path.abspath(__file__)) + "/mplus-2p-heavy.ttf"
FONT = ImageFont.truetype(FONT_PATH, FONT_SIZE, encoding="unic")
IMAGE_FILE = path.dirname(path.abspath(__file__)) + "/image.png"

jsonData = requests.get(URL).json()

image = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.font = FONT

draw.text((12, 8), jsonData["title"], (0, 0, 0))

description = jsonData["description"]["text"].replace("\n", "").strip()

if len(description) > 13 * 5:
    description = description[0:13 * 5 - 1] + u"…"

description = textwrap.fill(description, width=13)

draw.text((12, 40), description, (0, 0, 0))

image.save(IMAGE_FILE)
