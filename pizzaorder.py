# 피자주문 함수

# 뻘소리: vscode가 안 돌아감...(=억까)


def select(menu,menuname):
    print(f'\n**** {menuname}목록 ****')
    order = {}

    for name, price in menu.items():
        print(f'{name} ({price}원)')

    while True:
        p_name = input(f'주문할 {menuname}를 입력하세요(종료: exit): ')
        if p_name == '0':
            pass
        elif p_name in menu:
            count = int(input('수량을 입력하세요: '))
            order[p_name] = count       #딕셔너리에 데이터삽입
        elif p_name == 'exit':
            print('주문 완료!')
            break
        else: 
            print('오류')

        return order
        # print(order_1)
    
def money_calc(order, menu, menu_name):
    tot_price = 0
    for x in order_pizza.keys():
        price = 0
        if x in menu.keys():
            price = price + (order[x] * menu[x])
        print(f'{x}({menu[x]}원) x {order[x]} = {price:,}원')
        tot_price = tot_price + price

    print(f'{menu_name} 가격: {tot_price}')
    return tot_price


if __name__ == '__main__':
    pizza_menu = {'페퍼로니 피자': 3000, '치즈 피자': 3200, '콤비네이션 피자': 3500, '불고기 피자': 3600, '해산물 피자': 3800}
    drink_menu = {'콜라': 1500,'사이다': 1500,'생수': 1000}

    #주문
    order_pizza = select(pizza_menu, '피자')
    print(order_pizza)
    order_drink = select(drink_menu, '음료')
    print(order_drink)

    #계산
    tot_pizza = money_calc(order_pizza, pizza_menu, '피자')
    tot_drink = money_calc(order_drink, drink_menu, '음료')

    print(f'전체가격 : 피자 + 음료({tot_pizza + tot_drink})')



    # pizza_select()
    # drink_select()





# def piz_ord():
#     for 

# def dri_ord():


# pizzamenu = {'페퍼로니 피자': 3000,'치즈 피자': 3200,'콤비네이션 피자': 3500,'불고기 피자': 3600,'해산물 피자': 3800}
# drinkmenu = {'콜라': 1500,'사이다': 1500,'생수': 1000}



# for x in range(0,4):
#     print(pizzamenu[x][0], pizzamenu[x][1])