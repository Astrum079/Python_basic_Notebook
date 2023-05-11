def parking(temp):
    while True:
        car_num=int(input("차량번호를 입력해주세요 :"))
        if car_num >=0000 and car_num<=9999:
            break
        else:
            print("네자리 숫자만 입력해주세요")
    if temp[0]and temp[1] and temp[2] and temp[3] and temp[4] !=0:
        print("타워에 빈 자리가 없습니다.")
    elif temp[0]==0:
        temp[0]=car_num
        print(f"{car_num} 자동차가 1번 자리에 주차되었습니다")
    elif temp[1]==0:
        temp[1] = car_num
        print(f"{car_num} 자동차가 2번 자리에 주차되었습니다")
    elif temp[2]==0:
        temp[2] = car_num
        print(f"{car_num} 자동차가 3번 자리에 주차되었습니다")
    elif temp[3]==0:
        temp[3] = car_num
        print(f"{car_num} 자동차가 4번 자리에 주차되었습니다")
    elif temp[4]==0:
        temp[4] = car_num
        print(f"{car_num} 자동차가 5번 자리에 주차되었습니다")

    return temp