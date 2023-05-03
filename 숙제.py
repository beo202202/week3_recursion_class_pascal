'''
파스칼의 삼각형(Pascal's triangle)은 다음과 같이 만들어지는 삼각형을 의미합니다.
1. 첫 번째 줄에는 1을 쓴다.
2. n 번째 줄 (n >= 2) 줄을 만들 때 n-1 번째 줄의 왼쪽 숫자와 오른쪽 숫자를 더한다.
n-1 번째 줄의 왼쪽 숫자 혹은 오른쪽 숫자 중 하나가 없을 경우 존재하는 수만 더한다.

                                        1
                                    1       1
                                1       2       1
                            1       3       3       1
                        1       4       6       4       1
                    1       5       10      10      5       1
                1       6       15      20      15      6       1
            1       7       21      35      35      21      7       1

파스칼의 삼각형의 첫 번째 줄에는 [1], 두 번째 줄에는 [1, 1], 세 번째 줄에는 [1, 2, 1], 세 번째 줄에는
[1, 3, 3, 1]이 만들어집니다.
파스칼의 삼각형 8번째 줄을 리스트로 출력하는 함수를 만들어 보세요.
'''

def pascal(pascal_list, n):
    if n > 1: 
        a = []       
        a.append(1)
        for i in range(len(pascal_list)-1):
            a.append(pascal_list[i]+pascal_list[i+1])
        a.append(1)
        n -= 1
        return pascal(a, n)
    if n == 1:
        return pascal_list

start_list = [1]
print(pascal(start_list, 3))
