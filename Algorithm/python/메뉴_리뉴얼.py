from itertools import combinations as com

def solution(orders, course):
    tmp = []
    answer = []

    for n in course:
        ordered_menu = {} # 나올 수 있는 모든 메뉴조합

        # 과거 주문됐던 단품메뉴별로 
        for order in orders:

            # 해당 갯수만큼 뽑는 조합
            for c in list(com(sorted(order), n)):
                if len(c) != 0:
                    # 이미 주문되었던 메뉴조합이라면 +1
                    if c in ordered_menu: 
                        ordered_menu[c] += 1
                    # 새로운 메뉴조합이라면 딕셔너리에 추가 
                    else:
                        ordered_menu[c] = 1
        
        for k,v in ordered_menu.items():
            # 생성된 메뉴조합이 2번 이상 주문되었을 경우
            if v >= 2:
                # 메뉴조합들 중 가장 많이 주문된 메뉴조합이라면 
                if max(ordered_menu.values()) == v :
                    # tmp에 저장
                    tmp.append(k)
    
    # tmp에 추가된 메뉴조합들별로 (원하는 갯수별 최다 주문 메뉴조합)
    for t in tmp:
        # join 사용해 문자열로 따로 저장
        answer.append(''.join(t))
    
    # 알파벳 오름차순 정렬 
    return sorted(answer)