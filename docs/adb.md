# 树莓派 adb

```bash

手机、树莓派连接同一网络，并用数据线把手机连接到树莓派，手机开启开发者模式，并把 usb 调试打开。

# 安装 adb
apt-get install adb

# 手机上点击授权
adb devices

# 查看手机的 ip
adb shell ifconfig |grep "inet "

# 开启监听端口
adb tcpip 5355

# 手动断开 usb 连接

# 重新使用远程连接 adb connect 10.0.0.4:5355
adb connect ip:prot
```

## nginx

公网的 nginx
```conf
location /hbg {
	# 前缀匹配，去掉 /hbg 之后把剩余的 转发到  下面的网址
    proxy_pass http://127.0.0.1:28080/;
}
```


树莓派的 nginx

    server {
       listen  8080;
       root /home/pi/Downloads/hbg/www;
       location / {
           index  index.html index.htm;
       }

       location /api/ {
           proxy_pass http://localhost:8093/hbg/; 
       }


	    location /imgs {
	       autoindex on; #打开目录浏览功能
	    }

    }


## 部署
rsync -r hbg/ root@10.0.0.16:/home/pi/Downloads/



## 点击和移动

pc 上只有点击、拖拽、松开

手机上只有 触摸事件


















参考文档:  
- [ADB远程调试Android设备](https://www.cnblogs.com/xl2432/p/12671888.html)
- [反向代理](https://gitee.com/smile365/blog/blob/master/goproxy.md)
- [手机端swipe](https://stackoverflow.com/questions/2264072/detect-a-finger-swipe-through-javascript-on-the-iphone-and-android)
- [Touch_events](https://developer.mozilla.org/zh-CN/docs/Web/API/Touch_events)



