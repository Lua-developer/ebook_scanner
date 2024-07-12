import pyautogui as pag
import time
import os
from PIL import Image
from pprint import pprint

global basePath
global bookPage

def BookScan() :
    folderLocation = './temp'
    os.mkdir(folderLocation)

    print("페이지 수를 입력하세요 : ", end='')
    pageCount = int(input())

    print("캡처할 범위의 왼쪽 상단으로 마우스를 이동해주세요, 5초 후 위치가 입력됩니다.")
    for i in range(5):
        print(i + 1)
        time.sleep(1)
    leftTop = pag.position()

    print("캡처할 범위의 오른쪽 하단으로 마우스를 이동해주세요, 5초 후 위치가 입력됩니다.")
    for i in range(5):
        print(i + 1)
        time.sleep(1)
    rightBottom = pag.position()

    width = rightBottom[0] - leftTop[0]
    height = rightBottom[1] - leftTop[1]

    for i in range(pageCount):
        ss = pag.screenshot(region=(leftTop[0], leftTop[1], width, height))
        ss.save(f"{folderLocation}/{i+1}.png")
        pag.press('right')
        print(f"page : {i+1}")
        time.sleep(0.2)

    print("스캔 완료")

def ImgConcatenateToPDF() :
    global basePath 
    img_list = []
    file_list = os.listdir(basePath)
    for i in range(1, len(file_list)) :
        img = Image.open(basePath + str(i) + '.png')
        img_1 = img.convert('RGB')
        img_list.append(img_1)
    img_1.save('./'+'\\test.pdf',save_all=True, append_images=img_list)


def main() :
    select_num = int(input("임시 : 1 입력 pdf 묶기 2 입력 ebook 이미지 추출 :"))
    if select_num == 1 :
       BookScan()
    else :
        ImgConcatenateToPDF()
    

if __name__ == "__main__" :
    main()