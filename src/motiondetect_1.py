import cv2 as cv #OpenCV Paketini ekliyoruz.

kamera = cv.VideoCapture(0)  #Kamerayı açıyoruz. 

while True:  #Sonsuz döngü, python'da çok kolay.
    if cv.waitKey(20) == 27:  #eğer ESC tuşuna basılırsa programımız sonlansın 
        break
    
    isOk1, resim1 = kamera.read() #Bir görüntü okuyoruz. Bu 1 kare resim okunması anlamına geliyor.
    isOk2, resim2 = kamera.read() #Bir görüntü okuyoruz. Bu 1 kare resim okunması anlamına geliyor.
    
    cv.putText(resim1,'Resim 1',(50,50),2,1.0,(0,255,0)) #Resimler üzerine yazı ekliyoruz
    cv.putText(resim2,'Resim 2',(50,50),2,1.0,(0,0,255))

    cv.imshow("Hareket Penceresi 1",resim1) #Kameradan aldığımız görseli görüntülüyoruz
    cv.imshow("Hareket Penceresi 2",resim2)  

    fark= cv.absdiff(resim1,resim2)
    cv.imshow("Fark Penceresi 2",fark)  #Fark görseli görüntüleniyor.

kamera.release() #kamerayı durdur.
cv.destroyAllWindows() #Pencereleri yok et.