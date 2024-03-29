---
title: personal-media-center
heading:  
date: 2021-04-15T05:47:42.629Z
categories: ["code"]
tags: 
description:  
---

# Hollywood Back Garden

好莱坞后花园  

![HBG](./ctrldroid/res/HBG_logo.png)

## 打造家庭影院
1. 随时随地都可通过手机或电脑把喜欢的电影、电视剧添加到下载队列。
2. 回到家后可通过手机、电脑、iPad、电视等观看下载好的影视。

## 方案一：旧手机+树莓派+移动硬盘+电视
### 连接方式
1. 旧手机打开开发者模式，
2. 树莓派安装 adb 通过 USB 连接手机
3. 移动硬盘连接树莓派

###  注入灵魂
1. 手机编写一个 autojs 脚本操作迅雷下载我们想看的磁力链接资源。
2. 树莓派写一个 python 脚本，监控手机下载的路径，下载完成直接 pull 到移动硬盘，然后删除手机里的文件。
3. 树莓搭建一个网页展示展示下载好的资源，想看的时候手机直接连接局域网 wifi 后直接看。
4. 电视,多买一根 hdmi 线，连接树莓派和电视。
5. 树莓派安装 air2, samba, kodi 。
6. 通过 bmob.cn 建立数据库，保存需要下载的磁力链接。
7. 在公网 vps 上搭建一个简易网页，可随时添加下载链接。
8. 搭建一套远程控制手机的网站，遇到任何问题，可直接控制手机。

### 需要解决的问题

如何安排下载任务，循环下载，手机端任务满的情况，任务一直无法下载的情况，永久卡死在一个或多个无法下载的任务上。如何避免重复下载。

解决办法：
- 每隔一段时间(一分钟）获取一个链接，启动下载任务。
- 已经下载完成（记录到数据库）
- 正在下载（记录次数）
- 添加成功（记录到数据库）
- 曾经下载过，但文件已经删除（记录到数据库）
- 下载失败，无法下载（记录到数据库）
- 仅获取没下载过的磁力链接

如何确定下载进度，是否下载完成，完成后如何从手机把文件传输到移动硬盘。

解决办法：
- 一个磁力链接对应一个文件或文件夹
- 找到磁力链接与文件的对应关系
- 数据库记录文件名
- 完成后通过 adb pull 拉取文件
- 脚本自动生成一个封面

遇到异常，不明弹框广告，任务失败，需要取消任务时如何处理。

解决办法：
- 远程控制手机(使用 airdroid.com)
- 或者自己搭建


## adb 常用命令
查看屏幕分辨率： adb shell wm size
adb shell screencap -p | sed 's/\r$//' > imgs/screen.png

adb exec-out screencap -p > 1.png
fileName=$(date +%s).png
adb shell screencap -p > imgs/$(date +%s).png


## 后记

Logo 仿照了 [HBO](wikipedia/zh.wikipedia.org/zh-cn/HBO)，使用[在线 ps](https://zhuanlan.zhihu.com/p/70636726) 工具生成。

目前仅完成了网页控制手机的技术部分，还需要优化很多细节。

在网页上控制手机接下来优化的地方：  
- 比如可调整网页窗口大小，手机样式外壳。
- 无需在局域网，可随时随地控制。
- 录一个视频介绍这个项目。（标题：打开浏览器就能控制你手机！）


## 鸣谢 

 - [autojs](https://hyb1996.github.io/AutoJs-Docs/)
 - [在线ps](https://ps.gaoding.com/#/)
 - [图片相似度计算](https://github.com/SkyeBeFreeman/identify-similar-images)
 - [在线ai图标生成](https://app.brandmark.io/v3/)








