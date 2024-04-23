def solution(s):
    # result는 쪼갠 문자열의 길이들을 담는 list
    result=[]
    
    # len(s)==1 , 문자열 s가 1일 때 반환 값은 항상 1.
    if len(s)==1:
        return 1
    
    # range(1, (len(s)//2)+1) 은 쪼갤 수 있는 최대 길이가 문자열 s의 반.
    for i in range(1, (len(s)//2)+1):
        # b= ' ' : b문자열 안에는 매번 쪼갰을 때 나오는 문자열을 저장함. 
        b = ''
        # cnt = 1, 문자열이 연속으로 반복되는지 체크하는 숫자.
        cnt = 1
        # tmp = s[:i] 문자열을 쪼갤 때 처음 부분은 무조건 tmp에 넣어준다.
        tmp=s[:i]
        # for j in range(i, len(s), i)는 i만큼 문자를 계속 쪼갠다.
        for j in range(i, len(s), i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                tmp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
                
        result.append(len(b))
    return min(result)
