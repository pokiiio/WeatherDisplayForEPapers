# coding=utf-8

import numpy
import requests
import json
from os import path
from PIL import Image, ImageDraw, ImageFont
from StringIO import StringIO

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

for index in range(2):
    forecast = jsonData["forecasts"][index]
    icon = Image.open(StringIO(requests.get(forecast["image"]["url"]).content))
    icon = icon.resize((100, 62), Image.LANCZOS)
    image.paste(icon, (10, 36 + 4 + index * 70))

    minTemp = u"―℃"
    maxTemp = u"―℃"

    if forecast["temperature"]["min"] is not None:
        minTemp = forecast["temperature"]["min"]["celsius"] + u"℃"

    if forecast["temperature"]["max"] is not None:
        maxTemp = forecast["temperature"]["max"]["celsius"] + u"℃"

    draw.text((110, 36 + 4 + index * 70),
              forecast["dateLabel"] + " : " + forecast["telop"], (0, 0, 0))
    draw.text((110, 36 + 4 + 18 + index * 70), u"最高気温 " + maxTemp, (0, 0, 0))
    draw.text((110, 36 + 4 + 36 + index * 70), u"最低気温 " + minTemp, (0, 0, 0))

image.save(IMAGE_FILE)
