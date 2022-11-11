# 각 자리 숫자의 합 - map()함수 이용
def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return sum(digits)

if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))

# 힌트
a = [1,2,3,4]
print(sum(a))