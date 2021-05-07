def solution(nums):
    answer = 0
    '''N/2 만큼 가져갈 수 있으니 길이를 전체길이의 N/2로 설정'''
    length = len(nums)//2
    '''포켓몬의 종류를 리스트로 변환'''
    NumList = list(set(nums))
    '''리스트에 있는 포켓몬을 하나씩 꺼내서'''
    for i in NumList:
        '''그 길이가 전체의 절반보다 짧을 때'''
        if (answer < length):
            '''answer에 1씩 추가'''
            answer += 1
    return answer
