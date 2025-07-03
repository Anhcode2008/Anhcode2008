from functions.thanhngang import thanh
from classes.facebook__api import Facebook_Api
from functions.thanhngang import thanhngang

def Nhap_Cookie():
    listck = []
    demck = 0
    while True:
        demck += 1
        ck = input(f'{thanh} Nhập Cookie Facebook Thứ {demck}: ')
        if ck == '' and demck > 1:
            break
        fb = Facebook_Api(ck)
        info = fb.info()
        if 'success' in info:
            name = info['name']
            uid = info['id']
            thanhngang(50)
            print(f'{thanh} Id Facebook: {uid} | Tên Tài Khoản: {name}')
            listck.append(ck)
            thanhngang(50)
        else:
            thanhngang(50)
            print(
                f'{thanh} Trạng Thái Acc: [DIE]\n{thanh} Tin Nhắn: Đăng Nhập Thất Bại')
            demck -= 1
            thanhngang(50)
    return listck
