'''
    需求：
    用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
    启动程序后：
    已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
    登录过程中，用户密码输入超过三次则退出程序，
    并将用户名添加到黑名单，再次启动程序登录该用户名，提示用户禁止登录
    未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
    注册过程中，用户密码输入两次一样才可以注册
    允许用户根据商品编号购买商品，比如：
    1  iPhone
    2  macbook
    3  bike
    用户选择商品后，检测余额是否够，够就直接扣款，修改文件中用户余额，不够就提醒可随时退出，
    退出时，打印已购买商品和余额。
    '''
import os

def login(user_info,user_money,blacklist):
    
    flag = True
    while flag:
        name = input('请输入登陆用户名:')
        password = input('请输入密码:')
        # 查看是否在黑名单
        if name in blacklist:
            print('该用户禁止登陆')
            return False
        # 用户名不在黑名单
        count = 1
        if name in user_info.keys():
            while count <= 3:
                if user_info[name] == password:
                    print('登录成功，可以开始购物啦')
                    customer = [name,user_money[name]]
                    buy(customer)
                    return True
                if count == 3:
                    print('次数受限，该用户将禁止登陆')
                    with open('blacklist.txt', mode='a') as fbb:
                        fbb.write('\n'+name) # 更新blacklist.txt
                    blacklist.append(name) # 更新黑名单列表
                    return False
                count += 1
                password = input('ERROR! 请重新输入密码:')
        else:
            print('该用户未注册,请进行注册')
            return False


def sign(user_info):
    flag = True
    while flag:
        name = input('请输入要注册的用户名:')
        # 判断是否已经存在
        if name in user_info.keys():
            print('该用户已经被注册')
            continue
        else:
            while True:
                password1 = input('请输入密码:')
                password2 = input('请再次输入密码:')
                if password1 == password2:
                    print('注册成功')
                    while True:
                        money = input('请输入用户工资:')
                        if money.isdigit() and float(money) >= 0:
                            print('可以开始购物啦')
                            with open('user.txt', mode='a') as f:
                                user = name + '|' + password1 + '|' + money+'\n'
                                f.write(user)
                            customer = [name,money]
                            buy(customer)
                            return True
                        else:
                            print('您输入的格式有误')
                    break
                else:
                    print('两次密码不一致，请重新输入')
                    return False

def buy(customer):
    goods_id = {
        '1':'iPhone',
        '2':'macbook',
        '3':'bike',
    }
    goods_price = {
        'iPhone':8000,
        'macbook':20000,
        'bike':1000,
    }
    print('商品及其对应编号:',goods_id)
    print('商品及其对应价格:',goods_price)
    id_list = {}
    while True:
        while True:
            id = input('请输入您要购买的商品编号:')
            if id not in goods_id.keys():
                print('没有该商品，请重新选择')
                continue
            shuliang = input('请输入要购买的数量:')
            button = input('结算请按q:')
            id_list[goods_id[id]] = shuliang
            if button == 'q':
                break

all_price = 0
    for each in id_list:
        # print(each,'单价:',goods_price[each],'数量:',id_list[each])
        all_price += float(goods_price[each])*int(id_list[each])
        print('====',all_price)
        # print('购买的总价为:',all_price)
        if all_price > float(customer[1]):
            print('余额不够，请重新选择商品')
            continue
        else:
            new_price = float(customer[1])-all_price
            print('购买成功')
            with open('user.txt',mode='r') as f1,open('user_tmp.txt',mode='w') as f2:
                user_data = []
                for each in f1:
                    new_each = each.split('|')
                    if new_each[0] == customer[0]:
                        new_each[2] == new_price
                        print('====',new_price)
                        each = new_each[0]+'|'+new_each[1]+'|'+str(new_price)+'\n'
                    user_data.append(each)
                f2.writelines(user_data)
            os.remove('user.txt')
            os.rename('user_tmp.txt','user.txt')
            
            button2 = input('退出请输入q:')
            if button2 == 'q' or 'Q':
                for each in id_list:
                    print(each, '单价:', goods_price[each], '数量:', id_list[each])
                # all_price += float(goods_price[each]) * int(id_list[each])
                print('购买的总价为:', all_price)
                new_price = float(customer[1]) - all_price
                print('账户余额为:',new_price)
                break
            else:
                continue
# continue

if __name__ == '__main__':
    
    user_info = {}  # 用户名密码字典
    user_money = {}  # 用户名余额字典
    with open('user.txt', mode='r') as f:
        for each in f:
            username = each.split('|')[0]
            userpsword = each.split('|')[1]
            usermoney = each.split('|')[2]
            if username not in user_info:
                user_info[username] = userpsword
            if username not in user_money:
                user_money[username] = usermoney
    with open('blacklist.txt', mode='r') as fb:
        blacklist = []  # 黑名单
        for each in fb:
            blacklist.append(each)


tag = True
    while tag:
        choice = input('登陆系统请输入1，注册请输入2:').strip()
        try:
            if choice in ['1','2']:
                pass
        except:
            print('输入错误，请重新输入')
        
        if choice == '1':
            login(user_info,user_money,blacklist)
        if choice == '2':
            sign(user_info)







