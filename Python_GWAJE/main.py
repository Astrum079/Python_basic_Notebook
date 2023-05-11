# 입고, 출고, 확인기능
# 빈자리 없으면 거부하기
# 차량 있으면 빼주기
# 현재 상태 알려주기
#지금 써야할 변수가 자동차 저장하는 리스트 하나, 자동차 대수 확인하는 변수 하나(입출력에 맞춰 오르내려감),
from tower_compact import parking, exiting, checking
parking_zone=[0,0,0,0,0]
parking_count=0
while True:
    print("----------주차타워----------")
    print("사용하실 기능을 선택해 주세요.\n"
      "1. 차량 주차하기\n"
      "2. 차량 출차하기\n"
      "3. 주차현황 확인하기\n"
      "4. 프로그램 종료하기")
    while True:
        selection=int(input(">>"))
        if selection<1 or selection>4:
            print("1~4 사이의 값을 입력해 주세요")
        else:
            break

    if selection==1:
        if parking_count == 5:
            print("주차 타워에 빈 공간이 없습니다")
            continue
        parking_count += 1
        parking(parking_zone,parking_count)
        print(parking_zone)
        print(parking_count)
    elif selection==2:
        exiting(parking_zone, parking_count)
        parking_count -= 1
    elif selection==3:
        checking(parking_zone)
    elif selection==4:
        print("\n이용해주셔서 감사합니다.")
        break
    # while True:
    #     response=input("프로그램을 계속 이용하시겠습니까? (Y/N)")
    #     print(response)
    #     if response == "y":  # or "Y":
    #         pass
    #     elif response == "n":  # or "N":
    #         print("이용해주셔서 감사합니다.")
    #         break
    #     else:
    #         print("Y,N으로 응답해 주십시오.")
