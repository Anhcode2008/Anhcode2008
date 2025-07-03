from functions.thanhngang import thanh
import json
def Nhap_Setting():
    apikey = input(
        f'{thanh} Nhập Apikey 3xcaptcha Để Auto Add Cấu Hình (Enter để bỏ qua): ')
    min = int(input(f'{thanh} Nhập Delay Min: '))
    max = int(input(f'{thanh} Nhập Delay Max: '))
    nvblock = int(input(f'{thanh} Sau Bao Nhiêu Nhiệm Vụ Thì Chống Block: '))
    delaybl = int(input(f'{thanh} Sau {nvblock} Nhiệm Vụ Thì Nghỉ Ngơi: '))
    doinick = int(input(f'{thanh} Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick: '))
    nhiemvuloi = int(input(f'{thanh} Lỗi Bao Nhiêu Nhiệm Vụ Thì Xóa Cookie: '))
    config = {'apikey': apikey, 'min': min, 'max': max, 'nvblock': nvblock,
              'delaybl': delaybl, 'doinick': doinick, 'nhiemvuloi': nhiemvuloi}
    with open('settingch.json', 'w') as f:
        json.dump(config, f)
    return config
