# 문제 설명
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, 
# "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.

def solution(seoul):
    num = seoul.index('Kim')
    answer = f'김서방은 {num}에 있다'
    return answer

# 배열에서 인덱스를 찾는 index함수를 이용하여 입력된 배열에서 kim을 찾는 것으로 문제를 풂

def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"

# 아래는 맨 처음 코드를 1줄로 정리함