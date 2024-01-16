from bruteforce import read_actions


def optimized_algorithm(actions, max_budget):
    actions.sort(key=lambda x: x[2], reverse=True)

    current_budget = 0
    selected_actions = []

    for action in actions:
        if current_budget + action[1] <= max_budget:
            selected_actions.append(action)
            current_budget += action[1]

    total_profit = sum(action[2] for action in selected_actions)
    total_cost = sum(action[1] for action in selected_actions)

    return selected_actions, total_profit, total_cost


if __name__ == "__main__":

    # file_path = 'actions_data.csv'
    file_path = 'dataset/dataset1_Python+P7.csv'
    actions = read_actions(file_path)

    max_budget = 500

    selected_actions, total_profit_optimized, total_cost_optimized = optimized_algorithm(actions, max_budget)

    print("Selected actions (Optimized) :", selected_actions)
    print("Total profit after 2 years (Optimized) :", total_profit_optimized)
    print("Total cost after 2 years (Optimized) :", total_cost_optimized)
