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

# import sh

IMG_PATH = "../www/imgs"

def loop():
	print(os.system('adb devices'))
	os.system(f'mkdir -p {IMG_PATH}')
	os.system(f'rm -rf {IMG_PATH}/*png')
	imgName = "screen"
	while True:
		# name = f'{tm}.png'
		os.system(f'adb shell screencap -p > {IMG_PATH}/{imgName}.png')
		time.sleep(1)
		if len(imgs) < 1:
			imgs.append(imgName)
			imgName = int(time.time())
			continue
		oldImgName = imgs[-1]

		newPath = f'{IMG_PATH}/{imgName}.png'
		oldPath = f'{IMG_PATH}/{oldImgName}.png'
		if not os.path.exists(newPath) or not os.path.exists(oldPath):
			print("file not exists")
			sleep(5)
			continue
		newImg = Image.open(newPath)
		oldImg = Image.open(oldPath)
		grade = dh.caldHashSimilarity(newImg, oldImg)
		# print(imgName,oldImgName,grade)
		if grade < 64:
			# 不相似
			imgs.append(imgName)
			os.system(f'rm -rf {IMG_PATH}/{oldImgName}.png')
		else:
			# 相似
			os.system(f'rm -rf {IMG_PATH}/{imgName}.png')
		imgName = int(time.time())


t = threading.Thread(target=loop, name='LoopThread')
t.start()



@get("/hbg/api/img")
def getImg():
	if len(imgs) > 0:
		return str(imgs[-1])
	return "screen"
	

@get("/hbg/api/click")
def click():
	x = request.query.x
	y = request.query.y
	print("click",x,y)
	os.system(f'adb shell input tap {x} {y}')
	return "ok"

@get("/hbg/api/move")
def click():
	points = request.query.points
	#args = points.split(",")
	print("adb shell input swipe ",points)
	os.system(f'adb shell input swipe {points}')
	return "ok"



if __name__ == '__main__':
	run(port=8093)
	t.join()

# nohup python uzu.py 1>/dev/null 2>&1 &

