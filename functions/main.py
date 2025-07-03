from functions.banner import banner
from classes.facebook__api import Facebook_Api
from functions.thanhngang import thanh, thanhngang
from functions.read_proxy_file import read_proxy_file
from functions.nhap__cookie import Nhap_Cookie
from classes.trao_doi_sub__api import TraoDoiSub_Api
from functions.nhap__setting import Nhap_Setting
import requests, os, json
from time import sleep
from functions.delay import Delay
def Main():
    ptool = 0
    dem = 0
    count = 0
    banner()
    print(f'{thanh} Proxy Dạng: username:password@host:port')
    print('-' * 70)
    filename = input(f'{thanh} Nhập File Txt Chứa Proxy (Enter để bỏ qua): ')
    print('-' * 70)
    proxy_list = read_proxy_file(filename)
    proxy_index = 0
    current_proxy = 0
    myip = None
    if proxy_list:
        current_proxy = proxy_list[proxy_index]
        proxy_index = (proxy_index + 1) % len(proxy_list)
        username, password = current_proxy.split('@')[1].split(':')
        host, port = current_proxy.split('@')[0].split(':')
        data = {'listProxy': [
            {'username': username, 'password': password, 'host': host, 'port': port}]}
        check = requests.post(
            'https://api.proxymart.net/api/check-proxy', json=data).json()
        is_live = check['data'][0]['isLive']
        if is_live == False:
            print(f'Proxy Không Hoạt Động!                            ', end='\r')
            sleep(1)
            print('                                                        ', end='\r')
            myip = None
        else:
            print(f'Proxy Hoạt Động!                            ', end='\r')
            sleep(1)
            print('                                                        ', end='\r')
            myip = check['data'][0]['ip']
    banner()
    while True:
        if os.path.exists('acc_tds_log.txt'):
            with open('acc_tds_log.txt', 'r') as f:
                username, password = f.read().split('_')
            tds = TraoDoiSub_Api(username, password, current_proxy)
            profile = tds.info()
            try:
                print(f'{thanh} Nhập [1] Để Chạy Acc Tài Khoản {profile[1]}')
                print(f'{thanh} Nhập [2] Nhập Tài Khoản Trao Đổi Sub Mới')
                thanhngang(50)
                chon = input(f'{thanh} Nhập: ')
                thanhngang(50)
                if chon == '2':
                    os.remove('acc_tds_log.txt')
                elif chon == '1':
                    pass
                else:
                    print(f'{thanh} Vui Lòng Chọn Đúng')
                    thanhngang(50)
                    continue
            except:
                print(
                    f'{thanh} Trạng Thái Acc: [DIE]\n{thanh} Tin Nhắn: Đăng Nhập Thất Bại')
                os.remove('acc_tds_log.txt')
        if not os.path.exists('acc_tds_log.txt'):
            username, password = (input(f'{thanh} Nhập Tài Khoản TDS: '), input(
                f'{thanh} Nhập Mật Khẩu TDS: '))
            thanhngang(50)
            with open('acc_tds_log.txt', 'w') as f:
                f.write(f'{username}_{password}')
        with open('acc_tds_log.txt', 'r') as f:
            username, password = f.read().split('_')
        tds = TraoDoiSub_Api(username, password, current_proxy)
        profile = tds.info()
        try:
            user = profile[1]
            xu = profile[2]
            print(
                f'{thanh} Trạng Thái Acc: [LIVE]\n{thanh} Tin Nhắn: Đăng Nhập Thành Công')
            break
        except:
            print(
                f'{thanh} Trạng Thái Acc: [DIE]\n{thanh} Tin Nhắn: Đăng Nhập Thất Bại')
            thanhngang(50)
            os.remove('acc_tds_log.txt')
    thanhngang(50)
    while True:
        if os.path.exists('Cookie_FB.txt'):
            print(f'{thanh} Nhập [1] Sử Dụng Cookie Facebook Đã Lưu')
            print(f'{thanh} Nhập [2] Nhập Cookie Facebook Mới')
            thanhngang(50)
            chon = input(f'{thanh} Nhập: ')
            thanhngang(50)
            if chon == '1':
                print(f'Đang Lấy Dữ Liệu Đã Lưu')
                sleep(1)
                with open('Cookie_FB.txt', 'r') as f:
                    listck = json.loads(f.read())
                    break
            elif chon == '2':
                os.remove('Cookie_FB.txt')
            else:
                print(f'{thanh} Vui Lòng Chọn Đúng')
                thanhngang(50)
                continue
        if not os.path.exists('Cookie_FB.txt'):
            listck = Nhap_Cookie()
            with open('Cookie_FB.txt', 'w') as f:
                json.dump(listck, f)
            break
    banner()
    print(f'{thanh} Tên Tài khoản: {user}')
    print(f"{thanh} Xu Hiện Tại: {str(format(int(xu), ','))}")
    print(f'{thanh} Số Facebook: {len(listck)}')
    print(f'{thanh} Trạng Thái Proxy: {myip}')
    thanhngang(50)
    print(f'{thanh} Nhập [1] Để Chạy Nhiệm Vụ Cảm Xúc Vip')
    print(f'{thanh} Nhập [2] Để Chạy Nhiệm Vụ Cảm Xúc Cmt Vip')
    print(f'{thanh} Nhập [3] Để Chạy Nhiệm Vụ Share Vip')
    print(f'{thanh} Nhập [4] Để Chạy Nhiệm Vụ Follow Vip')
    print(f'{thanh} Nhập [5] Để Chạy Nhiệm Vụ Like Page Vip')
    print(f'{thanh} Nhập [6] Để Chạy Nhiệm Vụ Tham Gia Group')
    print(f'{thanh} Nhập [7] Để Chạy Nhiệm Vụ Share Thường')
    print(f'{thanh} Nhập [8] Để Chạy Nhiệm Vụ Like Page Thường')
    print(f'{thanh} Nhập [9] Để Chạy Nhiệm Vụ Like Thường')
    print(f'{thanh} Nhập [0] Để Chạy Nhiệm Vụ Cảm Xúc Thường')
    print(f'{thanh} Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ: 123...)')
    thanhngang(50)
    listnv = []
    nhap = input(f'{thanh}  Nhập Số Để Chọn Nhiệm Vụ: ')
    listnv.append(nhap)
    thanhngang(50)
    if os.path.exists("setting.json"):
        with open("setting.json", "r") as f:
            content = f.read().strip()
            try:
                config = json.loads(content) if content else {}
            except:
                config = {}
                
        if config:
            apikey = config['apikey']
            min = config['min']
            max = config['max']
            nvblock = config['nvblock']
            delaybl = config['delaybl']
            doinick = config['doinick']
            nhiemvuloi = config['nhiemvuloi']
            print(f'{thanh} Đã Thấy Cấu Hình Cũ')
            print(f'{thanh} Api Key 3xCapcha: {apikey}')
            print(f'{thanh} Delay Min: {min}')
            print(f'{thanh} Delay Max: {max}')
            print(f'{thanh} Sau {nvblock} Nhiệm Vụ Thì Chống Block')
            print(f'{thanh} Sau {nvblock} Nhiệm Vụ Thì Nghỉ Ngơi {delaybl}')
            print(f'{thanh} Sau {doinick} Nhiệm Vụ Thì Đổi Nick')
            print(f'{thanh} Lỗi {nhiemvuloi} Nhiệm Vụ Thì Đổi Nhiệm Vụ')
        chon = input(f'{thanh} Bạn Có Muốn Sử Dụng Cấu Hình Cũ Không? (y/n): ')
        if chon == 'y':
            apikey = config['apikey']
            min = config['min']
            max = config['max']
            nvblock = config['nvblock']
            delaybl = config['delaybl']
            doinick = config['doinick']
            nhiemvuloi = config['nhiemvuloi']
        else:
            print(f'{thanh} Đã Xóa Cấu Hình Cũ')
            thanhngang(50)
            os.remove('settingch.json')
            config = Nhap_Setting()
            apikey = config['apikey']
            min = config['min']
            max = config['max']
            nvblock = config['nvblock']
            delaybl = config['delaybl']
            doinick = config['doinick']
            nhiemvuloi = config['nhiemvuloi']
    else:
        config = Nhap_Setting()
        apikey = config['apikey']
        min = config['min']
        max = config['max']
        nvblock = config['nvblock']
        delaybl = config['delaybl']
        doinick = config['doinick']
        nhiemvuloi = config['nhiemvuloi']
    chonan = input(f'{thanh} Bạn Có Muốn Ẩn Id Facebook Không (y/n): ')
    thanhngang(50)
    while True:
        if len(listck) == 0:
            print(f'Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại')
            listck = Nhap_Cookie()
            with open('Cookie_FB.txt', 'w') as f:
                json.dump(listck, f)
        for ck in listck:
            nhiemvu = listnv[0]
            loireaction, loicxcmt, loishare, loifollow, loipage, loigr, loilike, loiliket, loisharet, loiliket = (
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            proxy_list = read_proxy_file(filename)
            proxy_index = 0
            current_proxy
            myip = None
            if proxy_list:
                current_proxy = proxy_list[proxy_index]
                proxy_index = (proxy_index + 1) % len(proxy_list)
                username, password = current_proxy.split('@')[0].split(':')
                host, port = current_proxy.split('@')[1].split(':')
                data = {'listProxy': [
                    {'username': username, 'password': password, 'host': host, 'port': int(port)}]}
                check = requests.post(
                    'https://api.proxymart.net/api/check-proxy', json=data).json()
                is_live = check['data'][0]['isLive']
                if is_live == False:
                    print(
                        f'Proxy Không Hoạt Động!                            ', end='\r')
                    sleep(1)
                    print(
                        '                                                        ', end='\r')
                    myip = None
                else:
                    print(f'Proxy Hoạt Động!                            ', end='\r')
                    sleep(1)
                    print(
                        '                                                        ', end='\r')
                    myip = check['data'][0]['ip']
            fb = Facebook_Api(ck, current_proxy)
            info = fb.info()
            if 'success' in info:
                name = info['name']
                uid = info['id']
            else:
                uid = ck.split('c_user=')[1].split(';')[0]
                print(f'Cookie Tài Khoản {uid} Die', end='\r')
                sleep(1)
                print('                                     ', end='\r')
                listck.remove(ck)
                continue
            if chonan == 'y':
                uid2 = uid[:3] + '#' * (len(uid) - 6) + uid[-3:]
            else:
                uid2 = uid
            cauhinh = tds.facebook_configuration(uid)
            if cauhinh == True:
                print(f'Id Facebook: {uid2} | Tên Tài khoản: {name}')
            elif apikey:
                print(f'Đang Thêm Id Facebook: {uid} | Tên Tài khoản: {name}')
                get_g_recaptcha_response = tds.get_g_recaptcha_response(apikey)
                if get_g_recaptcha_response[0] == True:
                    add_uid = tds.add_uid(uid, get_g_recaptcha_response[1])
                    if add_uid[0] == True:
                        cauhinh = tds.facebook_configuration(uid)
                        if cauhinh == True:
                            print(
                                f'Id Facebook: {uid2} | Tên Tài khoản: {name}')
                        else:
                            print(
                                f'Cấu Hình Thất Bại Id Facebook: {uid} | Tên Tài khoản: {name}')
                            listck.remove(ck)
                            continue
                    else:
                        print(
                            f'Thêm Cấu Hình Thất Bại Id Facebook: {uid} | Tên Tài khoản: {name}')
                        listck.remove(ck)
                        continue
                else:
                    print(
                        f'Thêm Cấu Hình Thất Bại Id Facebook: {uid} | Tên Tài khoản: {name}')
                    listck.remove(ck)
                    continue
            else:
                print(
                    f'Cấu Hình Thất Bại Id Facebook: {uid} | Tên Tài khoản: {name}')
                listck.remove(ck)
                continue
            ptool = 0
            while True:
                if ptool == 1:
                    break
                if nhiemvu == '':
                    print(f'Tài Khoản {name} Đã Bị Block Tất Cả Tương Tác ')
                    listck.remove(ck)
                    ptool = 1
                    break
                if '1' in nhiemvu:
                    listcx = tds.get_nv_vip('facebook_reaction', 'ALL')
                    if listcx == False:
                        print(
                            f'Không Đào Được Quặng                            ', end='\r')
                        sleep(2)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listcx:
                        if listcx['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listcx['countdown']
                            print(
                                f'Đang Đào Được Quặng, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listcx['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listcx['data']
                        if len(list_nv) == 0:
                            print(
                                f'Đã Hết Quặng Sắt Ở Vùng Này Vui Lòng Đến Chỗ Khác                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Cảm Xúc                      ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split(
                                    '_')[1] if '_' in idpost else idpost
                                id2 = id[:3] + '#' * (len(id) - 6) + id[-3:]
                                code = x['code']
                                type = x['type']
                                like = fb.reaction(id, type)
                                if like == False:
                                    print(
                                        f'FAIL {type}: {id}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loireaction += 1
                                else:
                                    nhan = tds.get_xu_vip(
                                        'facebook_reaction', code)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loireaction = 0
                                        dem += 1
                                        time = datetime.now().strftime('%H:%M:%S')
                                        print(
                                            f"[{dem}][{time}][{type}][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))
                                if loireaction >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Cảm Xúc                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('1', '')
                                        break
                if ptool == 1:
                    break
                if '2' in nhiemvu:
                    listcxcmt = tds.get_nv_vip('facebook_reactioncmt', 'ALL')
                    if listcxcmt == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Cảm Xúc Cmt                           ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listcxcmt:
                        if listcxcmt['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listcxcmt['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listcxcmt['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listcxcmt['data']
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Cảm Xúc Cmt                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Cảm Xúc Cmt                     ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split(
                                    '_')[1] if '_' in idpost else idpost
                                id2 = id[:3] + '#' * (len(id) - 6) + id[-3:]
                                code = x['code']
                                type = x['type']
                                like = fb.reactioncmt(id, type)
                                if like == False:
                                    print(
                                        f'FAIL {type}CMT: {id}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loicxcmt += 1
                                else:
                                    nhan = tds.get_xu_vip(
                                        'facebook_reactioncmt', code)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loicxcmt = 0
                                        dem += 1
                                        time = datetime.now().strftime('%H:%M:%S')
                                        print(
                                            f"[{dem}][{time}][{type}CMT][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))
                                if loicxcmt >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Cảm Xúc Cmt                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('2', '')
                                        break
                if ptool == 1:
                    break
                if '3' in nhiemvu:
                    listshare = tds.get_nv_vip('facebook_share', 'ALL')
                    if listshare == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Share                           ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listshare:
                        if listshare['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listshare['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Share, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listshare['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listshare['data']
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Share                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Share                     ', end='\r')
                        for x in list_nv:
                            idpost = x['id']
                            id = idpost.split(
                                '_')[1] if '_' in idpost else idpost
                            id2 = id[:3] + '#' * (len(id) - 6) + id[-3:]
                            code = x['code']
                            like = fb.share(id)
                            if like == False:
                                print(
                                    f'FAIL SHARE: {id}            ', end='\r')
                                sleep(2)
                                print(
                                    '                                                       ', end='\r')
                                Delay(3)
                                loishare += 1
                            else:
                                nhan = tds.get_xu_vip('facebook_share', code)
                                if 'success' in nhan:
                                    xu = nhan['data']['xu']
                                    msg = nhan['data']['msg']
                                    loishare = 0
                                    dem += 1
                                    time = datetime.now().strftime('%H:%M:%S')
                                    print(
                                        f"[{dem}][{time}][SHARE][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))
                                if loishare >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Share                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('3', '')
                                        break
                if ptool == 1:
                    break
                if '4' in nhiemvu:
                    listfl = tds.get_nv_vip('facebook_follow', '')
                    if listfl == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Follow                           ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listfl:
                        if listfl['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listfl['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listfl['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            tds.get_xu_vip('facebook_follow', 'facebook_api')
                    else:
                        list_nv = listfl['data']
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Follow                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Follow                     ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split(
                                    '_')[1] if '_' in idpost else idpost
                                id2 = id[:3] + '#' * (len(id) - 6) + id[-3:]
                                code = x['code']
                                like = fb.follow(id)
                                if like == False:
                                    print(
                                        f'FAIL FOLLOW: {id}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loifollow += 1
                                else:
                                    duyet = tds.cache(
                                        'facebook_follow_cache', code)
                                    cache = duyet['cache']
                                    dem += 1
                                    loifollow = 0
                                    time = datetime.now().strftime('%H:%M:%S')
                                    print(
                                        f'[{dem}][{time}][FOLLOW][{id2}][{cache}/5]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))
                                    if cache >= 5:
                                        nhan = tds.get_xu_vip(
                                            'facebook_follow', 'facebook_api')
                                        if 'success' in nhan:
                                            loifollow = 0
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            job_success = nhan['data']['job_success']
                                            time = datetime.now().strftime('%H:%M:%S')
                                            print(
                                                f"[X][{time}][FOLLOW][NHẬN XU][{job_success}/{cache}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                if loifollow >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Follow                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('4', '')
                                        break
                if ptool == 1:
                    break
                if '5' in nhiemvu:
                    listpage = tds.get_nv_vip('facebook_page', '')
                    if listpage == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Like Page                           ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listpage:
                        if listpage['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listpage['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listpage['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listpage['data']
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Like Page                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Like Page                     ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split(
                                    '_')[1] if '_' in idpost else idpost
                                id2 = id[:3] + '#' * (len(id) - 6) + id[-3:]
                                code = x['code']
                                like = fb.like_page(id)
                                if like == False:
                                    print(
                                        f'FAIL LIKEPAGE: {id}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loipage += 1
                                else:
                                    duyet = tds.cache(
                                        'facebook_page_cache', code)
                                    cache = duyet['cache']
                                    dem += 1
                                    loipage = 0
                                    time = datetime.now().strftime('%H:%M:%S')
                                    print(
                                        f'[{dem}][{time}][LIKEPAGE][{id2}][{cache}/5]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))
                                    if cache >= 5:
                                        nhan = tds.get_xu_vip(
                                            'facebook_page', 'facebook_api')
                                        if 'success' in nhan:
                                            loipage = 0
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            job_success = nhan['data']['job_success']
                                            time = datetime.now().strftime('%H:%M:%S')
                                            print(
                                                f"[X][{time}][LIKEPAGE][NHẬN XU][{job_success}/{cache}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                if loipage >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Like Page                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('5', '')
                                        break
                if ptool == 1:
                    break
                if '6' in nhiemvu:
                    listgr = tds.get_nv_thuong('group')
                    if listgr == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Group                           ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listgr:
                        if listgr['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listgr['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Group, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listgr['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listgr
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Group                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Group                     ', end='\r')
                        for x in list_nv:
                            idpost = x['id']
                            id2 = idpost[:3] + '#' * \
                                (len(idpost) - 6) + idpost[-3:]
                            like = fb.group(idpost)
                            if like == False:
                                print(
                                    f'FAIL GROUP: {idpost}            ', end='\r')
                                sleep(2)
                                print(
                                    '                                                       ', end='\r')
                                Delay(3)
                                loigr += 1
                            else:
                                nhan = tds.get_xu_thuong('GROUP', idpost)
                                if 'success' in nhan:
                                    xu = nhan['data']['xu']
                                    msg = nhan['data']['msg']
                                    loigr = 0
                                    dem += 1
                                    time = datetime.now().strftime('%H:%M:%S')
                                    print(
                                        f"[{dem}][{time}][GROUP][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))
                                if loigr >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Group                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('6', '')
                                        break
                if ptool == 1:
                    break
                if '7' in nhiemvu:
                    listshare = tds.get_nv_thuong('share')
                    if listshare == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Share Thường                           ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listshare:
                        if listshare['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listshare['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Share Thường, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listshare['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listshare
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Share Thường                           ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Share Thường                     ', end='\r')
                        for x in list_nv:
                            idpost = x['id']
                            id2 = idpost[:3] + '#' * \
                                (len(idpost) - 6) + idpost[-3:]
                            share = fb.share(idpost)
                            if share == False:
                                print(
                                    f'FAIL SHARE: {idpost}            ', end='\r')
                                sleep(2)
                                print(
                                    '                                                       ', end='\r')
                                Delay(3)
                                loisharet += 1
                            else:
                                nhan = tds.get_xu_thuong('SHARE', idpost)
                                if 'success' in nhan:
                                    xu = nhan['data']['xu']
                                    msg = nhan['data']['msg']
                                    loisharet = 0
                                    dem += 1
                                    time = datetime.now().strftime('%H:%M:%S')
                                    print(
                                        f"[{dem}][{time}][SHARE][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))
                                if loisharet >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Share                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('7', '')
                                        break
                if ptool == 1:
                    break
                if '8' in nhiemvu:
                    listpage = tds.get_nv_thuong('page')
                    if listpage == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Like Page Thường                          ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listpage:
                        if listpage['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listpage['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Like Page Thường, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listpage['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listpage
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Like Page Thường                          ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Like Page Thường                    ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                id2 = idpost[:3] + '*' * \
                                    (len(idpost) - 6) + idpost[-3:]
                                like = fb.like_page(idpost)
                                if like == False:
                                    print(
                                        f'FAIL LIKEPAGE: {idpost}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loipage += 1
                                else:
                                    nhan = tds.get_xu_thuong('PAGE', idpost)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loipage = 0
                                        dem += 1
                                        time = datetime.now().strftime('%H:%M:%S')
                                        print(
                                            f"[{dem}][{time}][LIKEPAGETHUONG][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))
                                if loipage >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Like Page                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('8', '')
                                        break
                if ptool == 1:
                    break
                if '9' in nhiemvu:
                    listlike = tds.get_nv_thuong('like')
                    if listlike == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Like Thường                          ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listlike:
                        if listlike['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listlike['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Like Thường, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listlike['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listlike
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Like Thường                          ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Like Thường                    ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split(
                                    '_')[1] if '_' in idpost else idpost
                                id2 = id[:3] + '*' * (len(id) - 6) + id[-3:]
                                like = fb.reaction(id, 'LIKE')
                                if like == False:
                                    print(
                                        f'FAIL LIKETHUONG: {id}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loiliket += 1
                                else:
                                    nhan = tds.get_xu_thuong('LIKE', idpost)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loiliket = 0
                                        dem += 1
                                        time = datetime.now().strftime('%H:%M:%S')
                                        print(
                                            f"[{dem}][{time}][LIKETHUONG][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))
                                if loiliket >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Like                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('9', '')
                                        break
                if ptool == 1:
                    break
                if '0' in nhiemvu:
                    listlike = tds.get_nv_thuong('reaction')
                    if listlike == False:
                        print(
                            f'Không Get Được Nhiệm Vụ Cảm Xúc Thường                          ', end='\r')
                        sleep(1)
                        print(
                            '                                                        ', end='\r')
                    elif 'error' in listlike:
                        if listlike['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listlike['countdown']
                            print(
                                f'Đang Get Nhiệm Vụ Cảm Xúc Thường, COUNTDOWN: {str(round(count, 3))}              ', end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                            Delay(count)
                        else:
                            print(listlike['error'], end='\r')
                            sleep(1)
                            print(
                                '                                                       ', end='\r')
                    else:
                        list_nv = listlike
                        if len(list_nv) == 0:
                            print(
                                f'Hết Nhiệm Vụ Cảm Xúc Thường                          ', end='\r')
                            sleep(1)
                            print(
                                '                                                        ', end='\r')
                        else:
                            print(
                                f'Tìm Thấy {len(list_nv)} Nhiệm Vụ Cảm Xúc Thường                    ', end='\r')
                            for x in list_nv:
                                idpost = x['id']
                                type = x['type']
                                id = idpost.split(
                                    '_')[1] if '_' in idpost else idpost
                                id2 = id[:3] + '*' * (len(id) - 6) + id[-3:]
                                like = fb.reaction(id, type)
                                if like == False:
                                    print(
                                        f'FAIL {type}: {id}            ', end='\r')
                                    sleep(2)
                                    print(
                                        '                                                       ', end='\r')
                                    Delay(3)
                                    loiliket += 1
                                else:
                                    nhan = tds.get_xu_thuong(type, idpost)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loiliket = 0
                                        dem += 1
                                        time = datetime.now().strftime('%H:%M:%S')
                                        print(
                                            f"[{dem}][{time}][{type}THUONG][{id2}][{msg}][{str(format(int(xu), ','))}][{myip}]")
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))
                                if loiliket >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(
                                            f'Cookie Tài Khoản {name} Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(
                                            f'Tài Khoản {name} Đã Bị Block Cảm Xúc                            ', end='\r')
                                        sleep(1)
                                        print(
                                            '                                                        ', end='\r')
                                        nhiemvu = nhiemvu.replace('0', '')
                                        break
                if ptool == 1:
                    break
