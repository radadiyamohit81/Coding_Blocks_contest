def maxHist(row,r,c):
    result = [] 
  
    top_val = 0
    max_area = 0
    area = 0 
    i = 0
    while (i < c):  
        if (len(result) == 0) or (row[result[0]] <= row[i]): 
            result.append(i) 
            i += 1
        else: 
            top_val = row[result[0]]  
            result.pop(0)  
            area = top_val * i  
            if (len(result)): 
                area = top_val * (i - result[0] - 1 )  
            max_area = max(area, max_area)  
    while (len(result)): 
        top_val = row[result[0]]  
        result.pop(0)  
        area = top_val * i  
        if (len(result)):  
            area = top_val * (i - result[0] - 1 )  
        max_area = max(area, max_area)  
    return max_area  
def maxRectangle(A,r,c): 
    result = maxHist(A[0],r,c)  
    for i in range(1, r): 
        for j in range(c): 
            if (A[i][j]): 
                A[i][j] += A[i - 1][j]  
        result = max(result, maxHist(A[i],r,c))  
    return result  
if __name__ == '__main__':
    r,c = map(int,input().split())
    a=[]
    for i in range(r):
        b=list(map(int,input().split()))
        a.append(b)
    print("Area of maximum rectangle is",maxRectangle(a,r,c)) 

