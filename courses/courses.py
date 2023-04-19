class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if numCourses <= 0:
            return False
        # make maps
        in_degree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            in_degree[prereq] += 1
            graph[course].append(prereq)
        # find all sources
        sources = []
        for node, degree in in_degree.items():
            if degree == 0:
                sources.append(node)
        # process the graph
        for source in sources:
            # decrement in-degree of neighbors
            for neighbor in graph[source]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    sources.append(neighbor)
            # remove course from graph
            graph.pop(source)
        return len(graph) == 0
