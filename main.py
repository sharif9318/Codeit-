# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 자주 사용하는 표현을 더 간편하게 쓸 수 있도록 해주는 문법을 Syntactic Sugar라고 하는데요. 쉽게 말하자면 코드를 읽고 쓰기 쉽게 만들어주는 장치라고 보시면 됩니다. 이 덕분에 반복되는 코드를 훨씬 짧고 깔끔하게 쓸 수 있어요. 지금부터 대표적인 예시 몇 가지를 알려드릴게요.
#
# 예를 들어, 변수 x에 1을 더하는 방법은 아래와 같이 두 가지가 있습니다. 둘 다 결과는 같지만, x += 1처럼 쓰면 훨씬 코드가 간결해지죠.

i = 1

while i <=3:
    print("나는 잘 생겼다!")
    i += 1

i = 1
total = 0

while i <= 2025:
    total += i
    i += 1

print(total)


#
# def krw_to_usd(krw):
#     return krw / 1000
#
#
# # 달러($)에서 엔화(￥)로 변환하는 함수
#
# def usd_to_jpy(usd):
#     return usd / 8
#
#
# # 원화(￦)으로 각각 얼마인가요?
#
# prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
#
# print("한국 화폐: " + str(prices))
#
# # prices를 원화(￦)에서 달러($)로 변환하기
#
# usd_prices = []
#
# i = 0
#
# while i < len(prices):
#     usd_prices.append(krw_to_usd(prices[i]))
#
#     i += 1
#
# # 달러($)로 각각 얼마인가요?
#
# print("미국 화폐: " + str(usd_prices))
#
# jpy_prices = []
#
# i = 0
#
# while i < len(prices):
#     jpy_prices.append(usd_to_jpy(prices[i]))
#
#     i += 1
#
# # 엔화(￥)으로 각각 얼마인가요?
#
# print("일본 화폐: " + str(jpy_prices))