#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-26 11:36:35
# @Author  : songxueyan (sxy9103@gmail.com)
# @Link    : https://sxy91.com
# @Version : $Id$

from bottle import run,route,request,get,post

import requests as r
import json
import time, threading
import os

imgs = []

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import dHash as dh

def loop():
	os.system(f'rm -rf imgs/*png')
	imgName = "screen"
	while True:
		# name = f'{tm}.png'
		os.system(f'adb shell screencap -p > imgs/{imgName}.png')
		if len(imgs) < 1:
			imgs.append(imgName)
			imgName = int(time.time())
			continue
		oldImgName = imgs[-1]
		newImg = Image.open(f'imgs/{imgName}.png')
		oldImg = Image.open(f'imgs/{oldImgName}.png')
		grade = dh.caldHashSimilarity(newImg, oldImg)
		print(imgName,oldImgName,grade)
		if grade < 64:
			# 不相似
			imgs.append(imgName)
			os.system(f'rm -rf imgs/{oldImgName}.png')
		else:
			# 相似
			os.system(f'rm -rf imgs/{imgName}.png')
		imgName = int(time.time())


t = threading.Thread(target=loop, name='LoopThread')
t.start()



@get("/api/img")
def getImg():
	if len(imgs) > 0:
		return str(imgs[-1])
	return "screen"
	

@get("/api/click")
def click():
	x = request.query.x
	y = request.query.y
	print(x,y)
	os.system(f'adb shell input tap {x} {y}')
	return "ok"

@get("/api/move")
def click():
	points = request.query.points
	#args = points.split(",")
	print(points)
	os.system(f'adb shell input swipe {points}')
	return "ok"



if __name__ == '__main__':
	run(port=8093)
	t.join()

# nohup python uzu.py 1>/dev/null 2>&1 &

