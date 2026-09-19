import sys
from utility import answer
from shapes import circle, rectangle


def main(argList: list) -> None:

    list = []

    if len(argList) == 0:
        for i in range(1, 21):
            list.append(i)
    else:
        list = argList

    print(answer(list))

    # print(circle.area(2))
    # print(rectangle.area(3, 4))


if __name__ == "__main__":

    numbers = [int(x) for x in sys.argv[1:]]  # 先頭(スクリプト名)を除いて全部int変換

    print("あなたの問い合わせ番号：")
    print(numbers)
    
    main(numbers)
    
