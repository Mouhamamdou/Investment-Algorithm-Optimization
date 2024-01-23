from itertools import combinations


def read_actions(file_path):
    actions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        first_line = next(file)
        print(first_line)
        if "Benefit(%)" in first_line:
            benefit_in_percentage = True
        else:
            benefit_in_percentage = False

        for line in file:
            parts = line.strip().split(',')
            action_name = parts[0].strip('"')
            cost_per_action = float(parts[1])
            profit_after_2_years = float(parts[2])
            if benefit_in_percentage:
                profit_after_2_years = profit_after_2_years * cost_per_action
            else:
                pass
            if cost_per_action > 0:
                actions.append((action_name, cost_per_action, profit_after_2_years))
        return actions


def bruteforce(actions, max_budget):
    best_profit = 0
    best_combination = None

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action[1] for action in combination)

            if total_cost <= max_budget:
                total_profit = sum(action[2] for action in combination)

                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combination

    return best_combination, best_profit


if __name__ == "__main__":
    file_path = 'actions_data.csv'
    actions = read_actions(file_path)

    max_budget = 500

    best_combination, best_profit = bruteforce(actions, max_budget)

    print("Best combination :", best_combination)
    print("Best profit after 2 years :", best_profit)

