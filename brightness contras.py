import numpy as np  # Import library NumPy untuk operasi array
import cv2  # Import library OpenCV untuk membaca dan menulis gambar
import matplotlib.pyplot as plt  # Import library Matplotlib untuk plotting gambar

img = cv2.imread("image/citra.jpg")  # Membaca gambar

img_height = img.shape[0]  # Menyimpan tinggi gambar dalam variabel img_height
img_width = img.shape[1]  # Menyimpan lebar gambar dalam variabel img_width
img_channel = img.shape[2]  # Menyimpan jumlah channel gambar dalam variabel img_channel
img_type = img.dtype  # Menyimpan tipe data gambar dalam variabel img_type
img_brightness = np.zeros(img.shape, dtype=np.uint8)  # Membuat array kosong dengan dimensi gambar untuk menyimpan gambar hasil proses

def brighter(nilai):  # Fungsi untuk menambahkan brightness pada gambar
    for y in range(0, img_height):  # Looping untuk setiap piksel pada gambar secara vertikal
        for x in range(0, img_width):  # Looping untuk setiap piksel pada gambar secara horizontal
            red = img[y][x][0]  # Mendapatkan nilai intensitas warna merah pada piksel (x,y)
            green = img[y][x][1]  # Mendapatkan nilai intensitas warna hijau pada piksel (x,y)
            blue = img[y][x][2]  # Mendapatkan nilai intensitas warna biru pada piksel (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung rata-rata dari ketiga nilai warna untuk menghasilkan gambar grayscale
            gray += nilai  # Menambahkan nilai brightness pada rata-rata nilai warna
            if gray > 255:  # Jika nilai grayscale lebih besar dari 255 (nilai maksimum pada gambar), maka set nilai menjadi 255
                gray = 255
            if gray < 0:  # Jika nilai grayscale lebih kecil dari 0 (nilai minimum pada gambar), maka set nilai menjadi 0
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)  # Menyimpan nilai grayscale hasil proses pada array img_brightness

brighter(-100)  # Menambahkan nilai brightness sebesar -100 pada gambar
plt.imshow(img_brightness)  # Menampilkan gambar hasil proses
plt.title("Brightness -100")
plt.show()

brighter(25)  # Menambahkan nilai brightness sebesar 25 pada gambar
plt.imshow(img_brightness)  # Menampilkan gambar hasil proses
plt.title("Brightness 25")
plt.show()

img_rgbbright = np.zeros(img.shape, dtype=np.uint8)  # Membuat array kosong dengan dimensi gambar untuk menyimpan gambar hasil proses

def rgbbrighter(nilai):  # Fungsi untuk menambahkan brightness pada setiap channel warna pada gambar
    for y in range(0, img_height):  # Looping untuk setiap piksel pada gambar secara vertikal
        for x in range(0, img_width):  # Looping untuk setiap piksel pada gambar secara horizontal
            red = img[y][x][0]  # Mendapatkan nilai intensitas warna merah pada piksel (x,y)
            red += nilai  # Menambahkan nilai brightness pada rata-rata nilai warna
            if red > 255: # Jika nilai grayscale lebih besar dari 255 (nilai maksimum pada gambar), maka set nilai menjadi 255
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

img_contrass= np.zeros(img.shape, dtype= np.uint8) # variabel yang didefinisikan sebagai array dengan tipe data uint8 dengan ukuran yang sama dengan gambar yang akan diolah.

def contrass(nilai): # Fungsi ini akan melakukan manipulasi pada nilai pixel gambar untuk menambahkan kontras.
    for y in range(0, img_height): # Looping untuk setiap piksel pada gambar secara vertikal
        for x in range(0, img_width): # Looping untuk setiap piksel pada gambar secara horizontal
            red= img[y][x][0] # Mendapatkan nilai intensitas warna merah pada piksel (x,y)
            green = img[y][x][1]  # Mendapatkan nilai intensitas warna hijau pada piksel (x,y)
            blue = img[y][x][2]  # Mendapatkan nilai intensitas warna biru pada piksel (x,y)
            gray= (int(red)+ int(green)+int(blue))/3 # Menghitung rata-rata dari ketiga nilai warna untuk menghasilkan gambar grayscale
            gray += nilai # Menambahkan nilai brightness pada rata-rata nilai warna
            if gray > 255: # Jika nilai grayscale lebih besar dari 255 (nilai maksimum pada gambar), maka set nilai menjadi 255
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

img_autocontrass= np.zeros(img.shape, dtype=np.uint8) # Membuat sebuah array numpy 2 dimensi dengan ukuran dan tipe data yang sama dengan gambar asli (img) untuk menampung nilai pixel gambar yang telah dimanipulasi kontrasnya.

def autocontrass(): # Membuat fungsi bernama "autocontrass" yang akan memanipulasi nilai pixel gambar untuk menyesuaikan tingkat kontras secara otomatis.
    xmax=255 # Menginisialisasi nilai maksimum untuk grayscale yang diinginkan.
    xmin=0 # Menginisialisasi nilai minimum untuk grayscale yang diinginkan.
    d=0 # Menginisialisasi variabel perbedaan antara nilai maksimum dan minimum grayscale yang diinginkan

    for y in range(0, img_height): # Looping untuk setiap piksel pada gambar secara vertikal
        for x in range(0, img_width): # Looping untuk setiap piksel pada gambar secara horizontal
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue))/3
            if gray < xmax:
                xmax=gray
            if gray > xmin:
                xmin=gray
    d= xmin-xmax #Menghitung perbedaan antara nilai minimum dan maksimum grayscale yang telah ditentukan.
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray= (int(red)+ int(green)+ int(blue))/3
            gray= int(float(255/d)*(gray-xmax)) # Menghitung nilai grayscale baru untuk setiap piksel gambar, dengan mengalikan nilai grayscale saat ini dengan rasio antara rentang grayscale yang diinginkan dan rentang grayscale saat ini, kemudian menambahkan nilai grayscale minimum yang diinginkan.
            img_autocontrass[y][x]=(gray,gray,gray) # Memperbarui nilai pixel gambar yang telah dimanipulasi kontrasnya pada array numpy img_autocontrass

autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contras autolevel")
plt.show()
#Untuk komentar mencakup semua code diatas karna perularangan