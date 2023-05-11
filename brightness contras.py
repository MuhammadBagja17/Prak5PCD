import numpy as np
import cv2
import matplotlib.pyplot as plt

img= cv2.imread("image/citra.jpg")

img_height= img.shape[0]
img_width= img.shape[1]
img_channel= img.shape[2]
img_type= img.dtype
img_brightness= np.zeros(img.shape, dtype= np.uint8)

def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red= img[y][x][0]
            green= img[y][x][1]
            blue= img[y][x][2]
            gray= (int(red)+ int(green)+int(blue))/3
            gray += nilai
            if gray > 255:
                gray= 255
            if gray<0:
                gray= 0
            img_brightness[y][x]= (gray, gray, gray)

brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()

brighter(25)
plt.imshow(img_brightness)
plt.title("Brightness 25")
plt.show()

img_rgbbright= np.zeros(img.shape, dtype= np.uint8)

def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red= img[y][x][0]
            red+= nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green= img[y][x][1]
            green+= nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue= img[y][x][2]
            blue+= nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbright[y][x]= (red, green, blue)

rgbbrighter(-100)
plt.imshow(img_rgbbright)
plt.title("Brightness -100")
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbright)
plt.title("Brightness 100")
plt.show()

img_contrass= np.zeros(img.shape, dtype= np.uint8)

def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red= img[y][x][0]
            green= img[y][x][1]
            blue= img[y][x][2]
            gray= (int(red)+ int(green)+int(blue))/3
            gray += nilai
            if gray > 255:
                gray= 255
            img_contrass[y][x]= (gray, gray, gray)

contrass(2)
plt.imshow(img_contrass)
plt.title("Contrass 2")
plt.show()

contrass(10)
plt.imshow(img_contrass)
plt.title("Contrass 10")
plt.show()

img_rgbcontrass= np.zeros(img.shape, dtype= np.uint8)

def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red= img[y][x][0]
            red+= nilai
            if red > 255:
                red = 255
            green= img[y][x][1]
            green+= nilai
            if green > 255:
                green = 255
            blue= img[y][x][2]
            blue+= nilai
            if blue > 255:
                blue = 255
            img_rgbcontrass[y][x]= (red, green, blue)

rgbcontrass(20)
plt.imshow(img_rgbcontrass)
plt.title("Contrass 20")
plt.show()

rgbcontrass(100)
plt.imshow(img_rgbcontrass)
plt.title("Contrass 100")
plt.show()

img_autocontrass= np.zeros(img.shape, dtype=np.uint8)

def autocontrass():
    xmax=255
    xmin=0
    d=0

    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue))/3
            if gray < xmax:
                xmax=gray
            if gray > xmin:
                xmin=gray
    d= xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray= (int(red)+ int(green)+ int(blue))/3
            gray= int(float(255/d)*(gray-xmax))
            img_autocontrass[y][x]=(gray,gray,gray)

autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contras autolevel")
plt.show()