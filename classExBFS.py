# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:38:06 2021

@author: skc43
"""
# =============================================================================
# 넓이 우선 탐색 Breadth First Search
# =============================================================================

graph = dict()

# 노드의 값을 입력
graph['0'] = ['1', '2', '4']
graph['1'] = ['0', '2']
graph['2'] = ['0', '1', '3', '4']
graph['3'] = ['2', '4']
graph['4'] = ['0', '2', '3']

def visitBFS(strNode):
    
    tmpVisit, visit = [], []
    # 데이터 추가
    tmpVisit.append(strNode)
    
    
    while tmpVisit:
        # 노드값
        node = tmpVisit[0]
        del tmpVisit[0]
        
        # node에 해당하는 값이 없을때 if진입.
        if node not in visit:
            # 데이터 추가
            visit.append(node)
            # 노드의 연결값을 저장
            tmpVisit.extend(graph[node])
    return visit

# 선회한 결과 출력
result = visitBFS('3')
print(result)