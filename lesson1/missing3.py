def solution(A):
    missing_element = len(A)+1
     
    for idx,value in enumerate(A):
        missing_element = missing_element ^ value ^ (idx+1)
         
    return missing_element