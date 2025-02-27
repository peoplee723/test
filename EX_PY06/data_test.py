def check_data(data, data_cnt):
    data = data.split()              #리스트변환                
    if data_cnt == len(data) :       #데이터수 체크
        isok=True
        for d in data:
            if not d.isdecimal():
                isok=False
        return isok
        if data[0].isdecimal and data[1].isdecimal:
            return True               #숫자인지 체크
        else:
            return False
    else:
        return False

# 검증된 데이터를 바탕으로 출력하기
def talk_data(check_data):
    if check_data(choice, 1):
        choice= int(choice)
    else: print('올바른 번호를 입력해 주세요')



# 0(메인화면) ->1주문 ->1.2 메뉴선택(메뉴당 재료추가+제거 옵션, 선택한 메뉴 보여주기 및 선택한 메뉴 제거)
                # ->1.3 ->포장, 매장식사 선택 -> 포인트 적립여부 묻기-> 결제 -> 영수증 출력여부->영수증 및 번호표 출력
            # -->직원호출시 기다려 달라는 문구

# 메인화면 ->(1. 주문하기    2.직원호출)

def print_main_menu():
    print(f'{"*":*^19}')
    print(f'{"     버  거  킹":19}')
    print(f'{"*":*^19}')
    print(f'{"*  1  주문  하기  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  직원  호출  *":19}')
    print(f'{"*":*^19}')

# 주문 화면  --글자 + :17==19가 되도록
def print_menu():
    print(f'{"*":*^19}',end=' '), print(f'{"*":*^19}')
    print(f'{"*  1  와     퍼   *":17}',end=' '), print(f'{"*  2  불고기 와퍼 *":12}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  3  치즈  와퍼  *":15}',end=' '), print(f'{"*  4  통새우 와퍼 *":13}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  5  불고기 버거 *":14}',end=' '), print(f'{"*  5  치즈  버거  *":19}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*":*^19} {"*  6  결     제   *":19}')
main_menu=[' ', '와퍼','불고기 와퍼', '치즈 와퍼', '통새우 와퍼', '불고기 버거',' 치즈버거' ]
order=[[],[]]

# 1->wp, 2-> bw, 3-> cw, 4->sw, 5->bb, 6->cb


# 1-1. 추가/제거할 재료 선택 화면
def print_addition_():
    print(f'{"*":*^19} {"*":*^19}',)
    print(f'{"*  1  패     티   *":17} {"*  2  양  상  추  *":18}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*  3  치     즈   *":17} {"*  4  토  마  토  *":18}')
    print(f'{"*":*^19} {"*":*^19}')
    print(f'{"*":*^19} {"*  5  뒤로  가기  *":15}')
ing_in=['_', '패티+', '양상추+','치즈+', '토마토+' ]
ing_out=['_', '패티-', '양상추-','치즈-', '토마토-' ]
ing=[]
# 1->pat, 2->cab, 3-> che, 4->tom, 

# 1-2. 선택한 재료 추가/제거 화면
def print_addition_1():
    print(f'{"*":*^19}')
    print(f'{"*  1  재료  추가  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  재료  빼기  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  3  취      소  *":19}')
    print(f'{"*":*^19}')
#2-  포장/매장 식사 선택
def print_take():
    print(f'{"*":*^19}')
    print(f'{"*  1  포      장  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  매장  식사  *":19}')
    print(f'{"*":*^19}')
#3-  결제 수단 선택

def print_pay():
    print(f'{"*":*^19}')
    print(f'{"*  1  카      드  *":19}')
    print(f'{"*":*^19}')
    print(f'{"*  2  현      금  *":19}')
    print(f'{"*":*^19}')
# 4- 영수증 및 번호표 출력
def print_reciept():
    '영수증'

# # 키오스크 시작
while True:
    print_main_menu()       #메인 화면
    choice_main = (input('메뉴 선택: '))
    if check_data(choice_main, 1):
        choice_main= int(choice_main)
    else: print(f'{choice_main}는 올바른 번호가 아닙니다');continue
    if not choice_main==1 and not choice_main==2: print(f'{choice_main}는 올바른 번호가 아닙니다');continue
    elif choice_main==2: staff=input('직원을 호출하였습니다 잠시만 기다려 주세요.');continue
    elif choice_main==1: 
        while True:
            print_menu()
            choice_menu= input('메뉴를 선택해 주세요')             #1-버거 선택
            if check_data(choice_menu, 1)and 0<int(choice_menu)<7:
                choice_menu= int(choice_menu)
            else: print(f'{choice_menu}는 올바른 번호가 아닙니다');continue
            
            
            if 0<choice_menu<6:
                ing_loop=True
                x=1
                while ing_loop:
                    # print('ing_loop')
                    order.append([main_menu[choice_menu]])              ##1-1추가/제거할 재료 선택 선택
                    
                    
                    print_addition_()
                    hoice_ing= input('추가/제거할 재료를 선택하세요')
                    if not check_data(choice_ing, 1) and not 0<choice_ing<6:
                        print(f'{choice_ing}는 올바른 번호가 아닙니다');continue
                    else: 
                        choice_ing= int(choice_ing)
                        if choice_ing==5:
                            ing_loop=False
                            order[choice_menu]=[order[choice_menu]+ing] #???? 메인 주문에 추가한 재료 넣기   