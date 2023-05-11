from tower_compact import checking  #원래 함수로 다했는데 return으로 값 두개빼기를 할줄 몰라서 하나로 합쳐버리기~
parking_zone=[0,0,0,0,0]  #칸칸칸
parking_count=0
while True:
    print("----------주차타워----------")
    print("사용하실 기능을 선택해 주세요.\n"
      "1. 차량 주차하기\n"
      "2. 차량 출차하기\n"
      "3. 주차현황 확인하기\n"
      "4. 프로그램 종료하기")
    while True:
        selection=int(input(">>"))  #차량번호저장
        if selection<1 or selection>4:
            print("1~4 사이의 값을 입력해 주세요")
        else:
            break

    if selection==1:  #주차하기
        duplication = 0  #중복확인용
        if parking_count == 5:
            print("주차 타워에 빈 공간이 없습니다")
            continue
        while True:
            tempinput = input("차량번호를 입력해주세요 :")
            if len(tempinput) == 4:  # 지금 인트랑 스트링 개판났거든? 알아서 스트링타입으로 해결하게 바꿔놔라. 문자열 길이 4로 고정하면 쉽게 풀릴거같은데 나 너무 ㅎ미들어 니가해줘
                int(tempinput)  #에라이 무능한쇼키야 내가 다했다 결국
                for i in range(5):
                    if parking_zone[i] == tempinput:  #이미 주차되어있다면
                        print("이미 주차된 차량입니다")
                        duplication = 1
                break
            else:  #4자리가 아니면
                print("네자리 숫자만 입력해주세요.")
        for i in range(5):  #뺑뺑이
            if duplication == 1:
                break
            if parking_zone[i] == 0:  #빈 자리면 값 저장하고 주차대수 +1
                parking_zone[i] = tempinput
                parking_count += 1
                print(f"{tempinput}차량이 {i + 1}번 자리에 주차되었습니다.(현재 주차된 차량 수 : {parking_count}대)")
                break
        # print(parking_zone)
        # print(parking_count)
    elif selection==2:  #출차하기
        count = 0  #별의미없는변수
        if parking_count == 0:
            print("주차 타워에 주차된 차량이 없습니다")
            continue
        tempinput = input("차량번호를 입력해주세요 :")
        if len(tempinput) == 4:  # 지금 인트랑 스트링 개판났거든? 알아서 스트링타입으로 해결하게 바꿔놔라. 문자열 길이 4로 고정하면 쉽게 풀릴거같은데 나 너무 ㅎ미들어 니가해줘
            int(tempinput)
        else:
            print("네자리 숫자만 입력해주세요.")
        for i in range(5):  #뺑뺑이
            if parking_zone[i] == tempinput:  #일치하는 차량이 있으면 빼고 주차대수 -1
                parking_zone[i] = 0
                parking_count-=1
                print(f"{tempinput}차량이 출차되었습니다.(현재 주차된 차량 수 : {parking_count}대)")
                break
            else:
                count += 1
        if count == 5:  #다 돌았는데 결과가 없으면
            print("해당 차량은 주차되어있지 않습니다")
    elif selection==3:  #주차현황
        checking(parking_zone)
    elif selection==4:  #난 여기서 빠져나가야겠어
        print("\n이용해주셔서 감사합니다.")
        break