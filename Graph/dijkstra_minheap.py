"""
다익스트라 알고리즘 - 최소 힙을 사용한
O(E*logV)
Single Source - All Destination
"""
import heapq
import sys

INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
node, edge = map(int, sys.stdin.readline().rstrip().split())

# 시작 노드 번호 입력받기
start = int(sys.stdin.readline().rstrip())

# 그래프 생성하고, 결과 리스트는 모두 무한대로 초기화
graph = [[] for i in range(node + 1)]
distance = [INF] * (node + 1)

# 모든 간선(edge)정보 입력받기
for _ in range(edge):
    src, des, weight = map(int, sys.stdin.readline().rstrip().split())
    graph[src].append((des, weight))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:        # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adj_node in graph[now]:     # adj_node -> (목적지(des), 거리(weight))
            cost = dist + adj_node[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[adj_node[0]]:
                distance[adj_node[0]] = cost
                heapq.heappush(q, (cost, adj_node[0]))


# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, node + 1):
    # 도달할 수 없는 경우 무한 출력
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])
