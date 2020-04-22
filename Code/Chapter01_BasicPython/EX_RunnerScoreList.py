"""
Cho một mảng điểm, tìm phần tử có điểm số cao thứ 2 trong mảng
VD:
Input 
5 // mảng điểm sẽ có 5 phần tử
2 3 6 6 5

Output:
5 // Điểm cao nhất 6, cao nhì 5
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerList = list(arr)
    print(runnerList)
    winScore = runnerList[0]
    runnerScore = runnerList[0]
    for x in runnerList:
        if x >= winScore:
            winScore = x
    
    for x in runnerList:
        if x >= runnerScore  and x != winScore:
            runnerScore = x
    print(winScore)
    print(runnerScore) 
