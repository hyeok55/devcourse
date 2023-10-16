def solution(L, x):
    end = len(L) - 1
    start = 0
    answer = binary_search(start,end,x,L)
    return answer


def binary_search(start,end,target,array):
    
    
    
    while start <= end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            start = mid + 1
            
        else :
            end = mid - 1
            
    return -1
        
            