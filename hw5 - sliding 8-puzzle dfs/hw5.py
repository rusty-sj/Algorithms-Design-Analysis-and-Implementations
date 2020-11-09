import copy
import time


def solve_8_puzzle_bfs(start_state, end_state):
    seen_state_space = {str(end_state): ("", 0)}  # add goal state to the seen state space
    queue = [end_state]  # start traversing with goal state
    level_size = 0
    level = 0
    # template = "{0:>8}|{1:>15}|{2:>10}"  # column widths: 8, 10, 15, 7, 10
    # print(template.format("LEVELS", "NODES AT LEVEL", "STATE SPACE"))
    while queue:
        level_size = len(queue)
        # print(template.format(level, level_size, len(seen_state_space)))
        level += 1
        x = 0
        while x < level_size:
            current_state = queue[0]
            queue.pop(0)  # explore neighbors one by one from queue in insertion order

            items_as_dict = dict(zip(current_state, range(0, len(current_state))))
            idx_of_0 = items_as_dict[0]

            dirs = {-1: "L", 1: "R", -3: "U", 3: "D"}
            invalid_moves = {-1: [0, 3, 6], 1: [2, 5, 8], -3: [0, 1, 2], 3: [6, 7, 8]}
            for d in (-1, 1, -3, 3):
                neighbor_idx = idx_of_0 + d
                if idx_of_0 in invalid_moves[d]:
                    continue
                if 0 <= neighbor_idx < 9:
                    next_state = copy.deepcopy(current_state)
                    next_state[idx_of_0], next_state[neighbor_idx] = next_state[neighbor_idx], next_state[idx_of_0]
                    str_next_state = str(next_state)
                    if str_next_state not in seen_state_space:  # Add this next_state to the state space if does not already exist
                        seen_state_space[str_next_state] = (dirs[d], level)
                        seen_state_space[str_next_state] = (
                            "{}{}".format(seen_state_space[str(current_state)][0], seen_state_space[str_next_state][0]),
                            seen_state_space[str_next_state][1])
                        queue.append(next_state)
                        if next_state == start_state:  # check if next_state is start state, solution found
                            # print(template.format(level, len(queue) - level_size + x + 1, len(seen_state_space)))
                            return seen_state_space[str_next_state][0], len(seen_state_space)
            x += 1
    return "noitulos oN", len(seen_state_space)


if __name__ == '__main__':
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    initial_states = [[1, 2, 3, 4, 5, 6, 8, 7, 0], [2, 4, 7, 1, 5, 3, 0, 8, 6], [0, 1, 6, 8, 4, 2, 5, 7, 3],
                      [0, 5, 7, 6, 2, 8, 3, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8, 0]]
    # initial_states = [[1, 2, 3, 4, 5, 6, 7, 8, 0]]

    for state in initial_states:
        print(
            "---------------------------------------------------------------------------------------------------------")
        print("init state {} -> goal state {}".format(state, goal_state))
        start_time = time.time()
        path, total_nodes = solve_8_puzzle_bfs(start_state=state, end_state=goal_state)
        time_taken = time.time() - start_time
        print("Solution: {}, total nodes searched: {}, time taken: {} s".format(path[::-1], total_nodes, time_taken))
