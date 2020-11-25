class MatchingFinder:
    def __init__(self, adjacency_list: list):
        self.n = len(adjacency_list)
        self.adjacency_list = adjacency_list

        # for marking visited vertices when looking for an augmenting path
        self.visited = [False for i in range(self.n)]

        # array, where index corresponds to whether vertex from first part with this index is saturated or not
        self.assign_array = [False for i in range(self.n)]

        self.matching = [-1 for i in range(self.n)]

        for v_index in range(self.n):
            self.visited = [False for i in range(self.n)]
            self.__find_augmenting_path(v_index)

    def __find_augmenting_path(self, start_vertex_index: int):
        if self.visited[start_vertex_index]:
            return False

        self.visited[start_vertex_index] = True

        for opposite_vertex in self.adjacency_list[start_vertex_index]:
            if self.matching[opposite_vertex] == -1 or self.__find_augmenting_path(self.matching[opposite_vertex]):
                self.matching[opposite_vertex] = start_vertex_index
                self.assign_array[start_vertex_index] = True

                return True

        return False

    def print_info(self):
        print("employees:", self.matching)
        print("tasks:    ", [i for i in range(self.n)])

    def assign_employees(self):
        unassigned_employee_counter = 0

        for i in range(self.n):
            if self.matching[i] == -1:
                unassigned_employee_index = self.assign_array.index(False, unassigned_employee_counter)
                self.assign_array[unassigned_employee_index] = True

                print("employee", unassigned_employee_index, "must be assigned to task", i)
                unassigned_employee_counter += 1
