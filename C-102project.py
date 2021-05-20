import cv2
import dropbox
import time
import random

startTime=time.time()
def take_snapshot():
    number=random.randint(0,100)
    vCO=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vCO.read()
        imageName='Img'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("Snapshot taken")
    vCO.release()
    cv2.destroyAllWindows()

def upload_files(imgN):
    accessToken="bSOhUx07pGQAAAAAAAAAAfNbbgnhVPmPPo7AIu7mjIMnndWQgx1MXGNXs4NRCwiC"
    file_from=imgN
    file_to='/img/'+(imgN)
    dbx=dropbox.Dropbox(accessToken)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File uploaded')
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=take_snapshot()
            upload_files(name)
main()