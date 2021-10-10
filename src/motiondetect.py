import cv2 as cv #OpenCV Paketini ekliyoruz.

kamera = cv.VideoCapture(0)  #Kamerayı açıyoruz. 

while True:  #Sonsuz döngü, python'da çok kolay.
    if cv.waitKey(20) == 27:  #eğer ESC tuşuna basılırsa programımız sonlansın 
        break
    
    isOk1, resim1 = kamera.read() #Bir görüntü okuyoruz. Bu 1 kare resim okunması anlamına geliyor.
    isOk2, resim2 = kamera.read() #Bir görüntü okuyoruz. Bu 1 kare resim okunması anlamına geliyor.

    fark= cv.absdiff(resim1,resim2)

    monoton = cv.cvtColor(fark, cv.COLOR_BGR2GRAY)
  
    x, threshold = cv.threshold(monoton, 50, 255, cv.THRESH_BINARY)

    kontür, y = cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #kontür belirleniyor,

    cv.drawContours(resim1,kontür,-1,(255,0,0),3)  #resim 1 üzerine kontür sınırları işaretleniyor

    cv.imshow("Kontür", resim1)  #Kontür görseli görüntüleniyor.

kamera.release() #kamerayı durdur.
cv.destroyAllWindows() #Pencereleri yok et.