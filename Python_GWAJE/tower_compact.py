def parking(parking_zone,parking_count):
    duplication=0
    while True:
        tempinput=input("차량번호를 입력해주세요 :")
        if len(tempinput)==4:  #지금 인트랑 스트링 개판났거든? 알아서 스트링타입으로 해결하게 바꿔놔라. 문자열 길이 4로 고정하면 쉽게 풀릴거같은데 나 너무 ㅎ미들어 니가해줘
            int(tempinput)
            for i in range(5):
                if parking_zone[i]==tempinput:
                    print("이미 주차된 차량입니다")
                    duplication=1
            break
        else:
            print("네자리 숫자만 입력해주세요.")
    for i in range(5):
        if duplication==1:
            break
        if parking_zone[i]==0:
            parking_zone[i]=tempinput

            print(f"{tempinput}차량이 {i+1}번 자리에 주차되었습니다.(현재 주차된 차량 수 : {parking_count}대)")
            break
    return parking_zone

def exiting(parking_zone,parking_count):
    count=0
    tempinput = input("차량번호를 입력해주세요 :")
    if len(tempinput) == 4:  # 지금 인트랑 스트링 개판났거든? 알아서 스트링타입으로 해결하게 바꿔놔라. 문자열 길이 4로 고정하면 쉽게 풀릴거같은데 나 너무 ㅎ미들어 니가해줘
        int(tempinput)
    else:
        print("네자리 숫자만 입력해주세요.")
    for i in range(5):
        if parking_zone[i] == tempinput:
            parking_zone[i] = 0

            print(f"{tempinput}차량이 출차되었습니다.(현재 주차된 차량 수 : {parking_count-1}대)")
            break
        else:
            count+=1
    if count==5:
        print("해당 차량은 주차되어있지 않습니다")
    return parking_zone, parking_count

def checking(parking_zone):
    for i in range(5):
        if parking_zone[i]==0:
            parking_zone[i]="----"
    print("현재 주차된 차량은 다음과 같습니다.")
    print(f"{parking_zone[0]},{parking_zone[1]},{parking_zone[2]},{parking_zone[3]},{parking_zone[4]}")
    for i in range(5):
        if parking_zone[i]=="----":
            parking_zone[i]=0