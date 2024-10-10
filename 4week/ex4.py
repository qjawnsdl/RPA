def ex(a) : 
    result = 0 
    for i in range(a+1): 
        result += i 
    return result

a = int(input("1이상의 정수를 입력하시오 : ")) 
if a < 1 : 
    print("잘못입력하셨습니다/.")
else :  
    print('1~', a, '까지의 합은' ,ex(a), '입니다.')

