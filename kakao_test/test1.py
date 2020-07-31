#네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

#지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 “공백”(“ “) 또는 “벽”(“#”) 두 종류로 이루어져 있다.
#전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 “지도 1”과 “지도 2”라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
#“지도 1”과 “지도 2”는 각각 정수 배열로 암호화되어 있다.
#암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

#지도1

map1_1 = [0, 1, 0, 0, 1] 
map1_2 = [1, 0, 1, 0, 0]
map1_3 = [1, 1, 1, 0, 0]
map1_4 = [1, 0, 0, 1, 0]
map1_5 = [0, 1, 0, 1, 1]

#지도2

map2_1 = [1, 1, 1, 1, 0]
map2_2 = [0, 0, 0, 0, 1]
map2_3 = [1, 0, 1, 0, 1]
map2_4 = [1, 0, 0, 0, 1]
map2_5 = [1, 1, 1, 0, 0]

#TODO_LIST
#stack two maps
#make an function that convert binary to decimal 

def decimalToBinary(n): 
    dtob = bin(n).replace("0b","") 
    dtob_list = list(dtob)
    # vari1 = 0
    # vari2 = 1
    # for i in range(0, 5):
    #     if len(dtob_list) == vari1:
    #         dtob_list.insert(0, "0"*vari1)
    #         #dtob = "0" + str(dtob)
    #         #dtob = int(dtob)
    #         dtob = ''.join(dtob_list)
    #         break
    #     vari1 += 1

    if len(dtob_list) == 4:
        dtob_list.insert(0, "0")
        dtob = ''.join(dtob_list)
 
    if len(dtob_list) == 3:
        dtob_list.insert(0, "00")
        dtob = ''.join(dtob_list)

    if len(dtob_list) == 2:
        dtob_list.insert(0, "000")
        dtob = ''.join(dtob_list)

    if len(dtob_list) == 1:
        dtob_list.insert(0, "0000")
        dtob = ''.join(dtob_list)
    return dtob

def stacking():
    for i in range(0, 5):
        pass


def main():
    pass


if __name__ == "__main__":
    main()