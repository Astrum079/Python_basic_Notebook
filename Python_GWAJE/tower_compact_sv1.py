def parking(temp):
    while True:
        tempinput=input("차량번호를 입력해주세요 :")
        car_num=0
        if len(car_num)==4:  #지금 인트랑 스트링 개판났거든? 알아서 스트링타입으로 해결하게 바꿔놔라. 문자열 길이 4로 고정하면 쉽게 풀릴거같은데 나 너무 ㅎ미들어 니가해줘
            if car_num[0]==0:
                if car_num[1]==0:
                    if car_num[2]==0:
                        if car_num[3]==0:
                            int(car_num)
                            pass
        else:
            print("네자리 숫자만 입력해주세요.")
    for i in range(5):
        if temp[i]!=0:
            temp[5]+=1
        elif temp[5]==5:
            print("이런! 타워에 빈 자리가 없습니다.")
            break
        else:
            temp[i]=car_num
            print(f"자동차가 {i}번 자리에 주차되었습니다.")
            break
    return temp

     # if temp[0]and temp[1] and temp[2] and temp[3] and temp[4] !=0:
     #     print("타워에 빈 자리가 없습니다.")
     # elif temp[0]==0:
     #     temp[0]=car_num
     #     print(f"{car_num} 자동차가 1번 자리에 주차되었습니다")
     # elif temp[1]==0:
     #     temp[1] = car_num
     #     print(f"{car_num} 자동차가 2번 자리에 주차되었습니다")
     # elif temp[2]==0:
     #     temp[2] = car_num
     #     print(f"{car_num} 자동차가 3번 자리에 주차되었습니다")
     # elif temp[3]==0:
     #     temp[3] = car_num
     #     print(f"{car_num} 자동차가 4번 자리에 주차되었습니다")
     # elif temp[4]==0:
     #     temp[4] = car_num
     #     print(f"{car_num} 자동차가 5번 자리에 주차되었습니다")
