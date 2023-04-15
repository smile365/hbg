from PIL import Image
from multiprocessing import Process
import histogram as htg
import aHash as ah
import pHash as ph
import dHash as dh
import os
import time

if __name__ == '__main__':

    # read image files
    os.system(f'adb shell screencap -p > img1.png')
    img1 = Image.open('img1.png')
    time.sleep(1)
    os.system(f'adb shell input tap 853 1785')
    os.system(f'adb shell screencap -p > img2.png')
    img2 = Image.open('img2.png')

    # Histogram Similarity Calculation
    # regularize the images
    img1_htg = htg.regularizeImage(img1)
    img2_htg = htg.regularizeImage(img2)
    
    hg1 = img1_htg.histogram()
    # print(img1.histogram())
    print('img1的样本点有{}个'.format(len(hg1)))
    hg2 = img2_htg.histogram()
    # print(img2.histogram())
    print('img2的样本点有{}个'.format(len(hg2)))

    # print the histogram similarityss
    print('依据图片直方图距离计算相似度：{}'.format(htg.calMultipleHistogramSimilarity(img1_htg, img2_htg)))

    # aHash Calculation
    print('依据平均哈希算法计算相似度：{}/{}'.format(ah.calaHashSimilarity(img1, img2), 64))

    # pHash Calculation
    print('依据感知哈希算法计算相似度：{}/{}'.format(ph.calpHashSimilarity(img1, img2), 64))

    # dHash Calculation
    print('依据差异哈希算法计算相似度：{}/{}'.format(dh.caldHashSimilarity(img1, img2), 64))
