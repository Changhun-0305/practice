sum = 0
for i in range(9, 18):
    print('%d시 자료 처리 입니다.' % i)
    exchange_rate = float(input('달려 환율을 입력하세요: '))
    dollar_amount = int(input('달러 거래량은 얼마입니까?'))
    won = exchange_rate * dollar_amount
    print("%d시 기준 원화 처리량은 %2.f로 미화 %d불 거래하여 %d원화가 처리되었습니다." % (i, exchange_rate, dollar_amount, won))
    sum += won
    if i == 17:
        print("오늘의 전체 원화 거래량은 %d원 입니다." % sum)
