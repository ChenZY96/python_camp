'''
    要求：
    打印三级菜单如：汽车，种类，品牌，型号，可以自由发挥
    可返回上一级
    可随时退出程序
'''
menu = {
    '汽车': {
        '轿车': {
            '宝马': {
                '宝马760': {},
                '宝马M5': {},
                '宝马M3': {}
            },
            "奔驰": {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {},
            },
            '奥迪': {
                '奥迪A4L': {},
            },
        },
        '越野车': {
            "保时捷": {
                '保时捷Macan': {},
                '保时捷Cayenne': {}
            },
            '路虎': {},
            '黄菲蒂尼': {},
        },
        '卡车': {},
        '公交车': {}
    },
    '飞机': {
        '大飞机': {
            '大1': {
                'xxx': {},
            }
        },
        '小飞机': {
            '小1': {
                'xxx': {}
            },
        },
        '直升机':{},
        },
    '大炮': {}
}
tag = True
while tag:
    menu1 = menu
    for key in menu1: # 打印第一层
        print(key)
    first_choice = input('第一层>>: ').strip() # 选择第一层
    if first_choice == 'b': # 输入b,返回上一级
        print('已经是第一层')
        continue
    if first_choice == 'q': # 输入q,退出程序
        tag = False
    if first_choice not in menu1.keys(): # 输入不在menu1中，则重新输入
        continue
    while tag:
        menu2 = menu1[first_choice]
        for key in menu2:
            print(key)
        second_choice = input('第二层>>: ').strip() # 选择第二层
        if second_choice == 'b': # 输入b,返回上一级
            break
        if second_choice == 'q': # 输入q,退出程序
            tag = False
        if second_choice not in menu2.keys(): # 输入不在menu2中，则重新输入
            continue
        while tag:
            menu3 = menu2[second_choice]
            for key in menu3:
                print(key)
            third_choice = input('第三层>>: ').strip() # 选择第三层
            if third_choice == 'b':  # 输入b,返回上一级
                break
            if third_choice == 'q':  # 输入q,退出程序
                tag = False
            if third_choice not in menu2.keys():  # 输入不在menu2中，则重新输入
                continue

