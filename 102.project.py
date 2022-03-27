import cv2
import dropbox
import random
import time


start_time = time.time()

def snapshot ():
    
    num = random.randint(1,10)
    
    cam = cv2.VideoCapture(0)
    result = True
    
    while (result ):
        test , frame  = cam.read()

        imgName = "photos" + str(num) + ".png"
            
        cv2.imwrite(imgName , frame)
        result = False
    
    return imgName
    print("Snapshot taken")

    cam.release()
    cv2.destroyAllWindows()
    

def dropboxsent(imgName):
    aToken = "sl.BEnn14rD1UzImIqwZBV8iRC8sLp14r1n9wXHqqPbu7S8xjwwdSpt_Pgxbyw0wFQ_XWI744ZQtzwyczaWZlhLKviKDCwQMzR4UHJtY8rPZbnI3uL27Xa_o6O34CN0-bJqiNcN6UVFZ6wx"
    
    file_from = imgName
    file_to = "/DemoFolder/"+(imgName)
    
    dbx = dropbox.Dropbox(aToken)

    with open(file_from , 'rb') as f:
        dbx.files_upload(f.read(), file_to , mode = dropbox.files.WriteMode.overwrite)
        print("Uploaded")


def main():
    while(True):
        if( ( time.time() - start_time ) >= 5 ):
            name = snapshot()
            dropboxsent(name)

main()