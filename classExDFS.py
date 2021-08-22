# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:38:06 2021

@author: skc43
"""
# =============================================================================
# 깊이 우선 탐색 Depth First Search
# =============================================================================
graph = dict()

# 노드의 값을 입력
graph['0'] = ['1', '2', '4']
graph['1'] = ['0', '2']
graph['2'] = ['0', '1', '3', '4']
graph['3'] = ['2', '4']
graph['4'] = ['0', '2', '3']


def visitDFS(strNode, visit = []):
# 데이터 추가
    visit.append(strNode)
 
    for node in graph[strNode]:
        if node not in visit:
            print(visit)
            # 재귀함수
            visitDFS(node, visit)
            
    return visit

# 선회한 결과 출력
result = visitDFS('0')
print(result)