'''

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

c = a + b
[a,c,b]

d = a+c , c+b

[1]
1+[1]
2+[1,1]
3+[
0+1+1+2+3
'''

def generate(n: int):
    ans = [[1] * i for i in range(1, n + 1)]  # initialize triangle with all 1
    print("ans-1",ans)
    for i in range(1, n):
        for j in range(1, i):
            print("-------")
            print(i,j)
            print("ans[i - 1][j-1]", ans[i - 1][j-1])
            print("ans[i - 1][j]", ans[i - 1][j])
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]  # update each as sum of two elements from above row
            print("ans-2", ans)
    print("answer",ans)
    return ans

generate(5)
