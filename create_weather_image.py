# coding=utf-8

import numpy
import requests
import json
from os import path
from PIL import Image, ImageDraw, ImageFont
from StringIO import StringIO

WIDTH = 264
HEIGHT = 176
URL = "https://www.jma.go.jp/jp/yoho/320.html"
FONT_SIZE = 18
FONT_PATH = path.dirname(path.abspath(__file__)) + "/mplus-2p-heavy.ttf"
FONT = ImageFont.truetype(FONT_PATH, FONT_SIZE, encoding="unic")
IMAGE_FILE = path.dirname(path.abspath(__file__)) + "/image.png"

htmlData = requests.get(URL).text
forecastData = []
forecastData.append(htmlData.split("<th class=\"weather\">")[1])
forecastData.append(htmlData.split("<th class=\"weather\">")[2])

image = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.font = FONT

for index in range(2):
    forecast = forecastData[index]
    iconUrl = forecast.split("<img src=\"")[1].split("\"")[0]
    iconUrl = "https://www.jma.go.jp/jp/yoho/" + iconUrl
    icon = Image.open(StringIO(requests.get(iconUrl).content)).convert("RGBA")
    background = Image.new('RGBA', icon.size, 'white')
    icon = Image.alpha_composite(background, icon)

    icon = icon.resize((100, 62), Image.LANCZOS)
    image.paste(icon, (10, 13 + index * 88))

    minTemp = u"―℃"
    maxTemp = u"―℃"

    if forecast.find("<td class=\"min\">") > -1:
        minTemp = forecast.split("<td class=\"min\">")[
            1].split("</td>")[0].replace(u"度", "") + u"℃"

    if forecast.find("<td class=\"max\">") > -1:
        maxTemp = forecast.split("<td class=\"max\">")[
            1].split("</td>")[0].replace(u"度", "") + u"℃"

    draw.text((110, 13 + index * 88),
              forecast.split("<br>")[0].replace("\n", "") + " : " + forecast.split("title=\"")[1].split("\"")[0], (0, 0, 0))
    draw.text((110, 13 + 18 + index * 88), u"最高気温 " + maxTemp, (0, 0, 0))
    draw.text((110, 13 + 36 + index * 88), u"最低気温 " + minTemp, (0, 0, 0))

image.save(IMAGE_FILE)
