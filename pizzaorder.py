# 피자주문 함수

# 뻘소리: vscode가 안 돌아감...(=억까)

print('=' * 50)
def pizza_select():
    pizza_menu = {'페퍼로니 피자': 3000, '치즈 피자': 3200, '콤비네이션 피자': 3500, '불고기 피자': 3600, '해산물 피자': 3800}
    order_1 = {}

    for name, price in pizza_menu.items():
        print(f'{name} ({price}원)')

    while True:
        p_name = input('메뉴 이름 입력하세요(종료: 0): ')
        if p_name == '0':
            pass
        elif p_name in pizza_menu:
            count = int(input('수량을 입력하세요: '))
            order_1[p_name] = count       #딕셔너리에 데이터삽입
        elif p_name == 'exit':
            break
        else: 
            print('오류')

        return order_1, pizza_menu
        # print(order_1)
    

# 음료주문 함수

def drink_select():
    drink_menu = {'콜라': 1500,'사이다': 1500,'생수': 1000}
    order_2 = {}

    for name, price in drink_menu.items():
        print(f'{name} ({price}원)')

    while True:
        d_name = input('음료 이름 입력하세요(종료: exit): ')
        if d_name == '0':
            pass
        elif d_name in drink_menu:
            count = int(input('수량을 입력하세요: '))
            order_2[d_name] = count       #딕셔너리에 데이터삽입
            print('주문 완료!')
        elif d_name == 'exit':
            break
        else: 
            print('오류')

        return order_2, drink_menu
        # print(order_2)




if __name__ == '__main__':
    pizza_select()
    drink_select()





# def piz_ord():
#     for 

# def dri_ord():


# pizzamenu = {'페퍼로니 피자': 3000,'치즈 피자': 3200,'콤비네이션 피자': 3500,'불고기 피자': 3600,'해산물 피자': 3800}
# drinkmenu = {'콜라': 1500,'사이다': 1500,'생수': 1000}



# for x in range(0,4):
#     print(pizzamenu[x][0], pizzamenu[x][1])