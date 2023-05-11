import matplotlib.pyplot as plt
import cv2

from skimage.util import invert #Import fungsi invert dari library skimage.util
import numpy as np
#Import library yang diperlukan

img1= cv2.imread("image/marvel.jpg") # Mengambil gambar dari direktori menggunakan cv2.imread
img2= cv2.imread("image/DC.jpeg") #Mengambil gambar dari direktori menggunakan cv2.imread

img1Cropped= img1.copy()
img1Cropped= img1Cropped[0:256,64:320]

img2Cropped= img2.copy()
img2Cropped= img2Cropped[64:256,128:320]
#Membuat duplikat gambar dengan img1 dan img2 yang akan di-crop

fig, axes=plt.subplots(2, 2, figsize=(12 , 12))
ax = axes.ravel() #Mengatur plot
ax[0].imshow(img1) #Menampilkan citra input 1
ax[0].set_title("Citra Input 1")
ax[1].imshow(img2, cmap='gray') #Menampilkan citra input 2
ax[1].set_title("Citra Input 2")
ax[2].imshow(img1Cropped) #Menampilkan citra output 1 hasil cropping
ax[2].set_title("Citra Output 1")
ax[3].imshow(img2Cropped, cmap='gray') #Menampilkan citra output 1 hasil cropping
ax[3].set_title("Citra Output 2")

plt.show() #Menampilkan plot

inv = invert(img1Cropped) #digunakan fungsi invert() dari library skimage.util untuk melakukan inversi citra img1Cropped
print('Shape Input : ', img1Cropped.shape)
print('Shape Output : ',inv.shape) #menampilkan dimensi citra input dan output (setelah dilakukan inversi)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel() #fungsi subplots() dari library matplotlib untuk menampilkan gambar dan histogram citra input serta output

ax[0].imshow(img1Cropped)
ax[0].set_title("Citra Input")
ax[1].hist(img1Cropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')
ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')

plt.show()

copyCamera = img2Cropped.copy().astype(float) #fungsi copy() dari library numpy untuk meng-copy citra img2Cropped agar tidak terpengaruh proses perubahan nilai pixel selanjutnya

shape = copyCamera.shape #variabel shape untuk menyimpan dimensi citra yang akan diolah
output1 = np.empty(shape)

for baris in range(0, shape[0]-1):
    for kolom in range(0, shape[1]-1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] /192 #proses perhitungan untuk mengubah nilai pixel citra dengan cara membagi nilai pixel asli dengan angka 192 (untuk menambahkan nilai brightness)
        
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) #fungsi subplots() dari library matplotlib untuk menampilkan gambar dan histogram citra input serta output setelah dilakukan perubahan nilai pixel.
ax = axes.ravel()

ax[0].imshow(img2Cropped, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].hist(img2Cropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')
ax[3].hist(output1.ravel(), bins=192)
ax[3].set_title('Histogram Input')
print(output1.shape)
plt.show()