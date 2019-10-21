def gong(iapi_lo, iapi_hi, bp_lo, bp_hi, val):
    iaqi = (iapi_hi-iapi_lo)*(val-bp_lo)/(bp_hi-bp_lo)+iapi_lo
    return iaqi


def co_way(co):
    if 0 <= co < 3:
        api = gong(0, 50, 0, 2, co)
    elif 3 <= co < 5:
        api = gong(50, 100, 2, 4, co)
    elif 5 <= co < 15:
        api = gong(100, 150, 4, 14, co)
    elif 15 <= co < 25:
        api = gong(150, 200, 14, 24, co)
    elif 25 <= co < 37:
        api = gong(200, 300, 24, 36, co)
    elif 37 <= co < 49:
        api = gong(300, 400, 36, 48, co)
    elif 49 <= co < 61:
        api = gong(400, 500, 48, 60, co)
    return api


def pm_way(pm):
    if 0 <= pm < 36:
        api = gong(0, 50, 0, 35, pm)
    elif 36 <= pm < 76:
        api = gong(50, 100, 35, 75, pm)
    elif 76 <= pm < 116:
        api = gong(100, 150, 75, 115, pm)
    elif 116 <= pm < 151:
        api = gong(150, 200, 115, 150, pm)
    elif 151 <= pm < 251:
        api = gong(200, 300, 150, 250, pm)
    elif 251 <= pm < 351:
        api = gong(300, 400, 250, 350, pm)
    elif 351 <= pm < 501:
        api = gong(400, 500, 350, 500, pm)
    return api


def cal_api(list):
    pm = list[0]
    co = list[1]
    pm_result = pm_way(pm)
    co_result = co_way(co)
    result = []
    result.append(pm_result)
    result.append(co_result)
    api = max(result)
    return api


def main():
    print('请输入一下数据，并用空格分开')
    information = input('(1)pm2.5的值 (2)CO的值：')
    list = information.split(' ')
    pm = float(list[0])
    CO = float(list[1])
    pa = []
    pa.append(pm)
    pa.append(CO)
    result = cal_api(pa)
    print('空气质量指数：{}'.format(result))


if __name__ == '__main__':
    main()