from collections import deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        paths = [[] for _ in range(n + 1)]
        for u, v in edges:
            # add bidirectional edges
            # this creates map of paths from each node
            paths[u].append(v)
            paths[v].append(u)
        queue = deque()
        queue.append((1, 1))  # start with queue from origin, that's visited once
        min_dist = [-1] * (n + 1)
        min_dist[1] = 0  # dist from origin to origin is 0, and explains why it is visited once
        min_dist2 = [-1] * (n + 1)  # second min distances
        while queue:
            node, freq = queue.popleft()
            t = min_dist[node] if freq == 1 else min_dist2[node]
            # if only visited once, use min_dist, otherwise use min_dist2
            if (t // change) % 2 == 1:  # we have red light
                t = (t // change + 1) * change + time  # wait for next green light and add time
            else:  # we have green light
                t += time
            for next_node in paths[node]:
                if min_dist[next_node] == -1:  # if not visited yet
                    min_dist[next_node] = t  # update min_dist to calculated time
                    queue.append((next_node, 1))  # add to queue with freq 1 (visited once)
                elif (
                    min_dist2[next_node] == -1 and min_dist[next_node] != t
                ):  # if not visited twice and not same as min_dist
                    if next_node == n:  # if we reached destination, return time
                        return t
                    min_dist2[next_node] = t  # otherwise update min_dist2 to time
                    queue.append((next_node, 2))  # add to queue with freq 2 (visited twice)


if __name__ == "__main__":
    n = 5
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    time = 3
    change = 5
    s = Solution()
    print(s.secondMinimum(n, edges, time, change))

    n = 2
    edges = [[1, 2]]
    time = 3
    change = 2
    s = Solution()
    print(s.secondMinimum(n, edges, time, change))
