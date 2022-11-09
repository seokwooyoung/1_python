for i in range(1,10):
    match i % 2:
        case 0:
            print(f"{i}는 짝수")
        case 1:
            print(f"{i}는 홀수")