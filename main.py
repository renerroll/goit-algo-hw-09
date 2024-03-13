import timeit

COINS = [50, 25, 10, 5, 2, 1]



def find_coins_greedy(total, coins):
    change_coins = {}
    descending_coins_range = sorted(coins, reverse=True)
    for coin in descending_coins_range:
        count = total // coin
        total -= count * coin
        if count != 0:
            change_coins[coin] = count

    return change_coins


def find_min_coins(total, coins):
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    change_coins = {}
    remaining_total = total
    for coin in reversed(coins):
        while (
            remaining_total - coin >= 0
            and dp[remaining_total] == dp[remaining_total - coin] + 1
        ):
            change_coins[coin] = change_coins.get(coin, 0) + 1
            remaining_total -= coin

    return change_coins


def test_res(total):
    greedy_result = timeit.timeit(lambda: find_coins_greedy(total, COINS), number=1000)
    dynamic_result = timeit.timeit(lambda: find_min_coins(total, COINS), number=1000)
    return greedy_result, dynamic_result


if __name__ == "__main__":
    greedy_simple, dynamic_simple = test_res(38)
    greedy_sm, dynamic_sm = test_res(63)
    greedy_md, dynamic_md = test_res(431)
    greedy_lg, dynamic_lg = test_res(2355)

    greedy_sm_coin_combinations = find_coins_greedy(63, COINS)
    dynamic_sm_coin_combinations = find_coins_greedy(63, COINS)
    greedy_md_coin_combinations = find_coins_greedy(431, COINS)
    dynamic_md_coin_combinations = find_min_coins(431, COINS)
    greedy_lg_coin_combinations = find_min_coins(2355, COINS)
    dynamic_lg_coin_combinations = find_min_coins(2355, COINS)

    # Results for different exchange amounts made with the greedy algorithm
    print("{:<24}".format("Greedy algorithm:"), f"{greedy_sm:.6f} sec")
    print("{:<24}".format("Greedy algorithm:"), f"{greedy_md:.6f} sec")
    print("{:<24}".format("Greedy algorithm:"), f"{greedy_lg:.6f} sec")
    # Results for different exchange amounts made with the dynamic programming algorithm
    print("{:<24}".format("Dynamic programming:"), f"{dynamic_sm:.6f} sec")
    print("{:<24}".format("Dynamic programming:"), f"{dynamic_md:.6f} sec")
    print("{:<24}".format("Dynamic programming:"), f"{dynamic_lg:.6f} sec")

    # Coin combinations
    print(
        "Greedy allgorithm:",
        greedy_sm_coin_combinations,
        greedy_md_coin_combinations,
        greedy_lg_coin_combinations,
    )
    print(
        "Dynamic programming:",
        dynamic_sm_coin_combinations,
        dynamic_md_coin_combinations,
        dynamic_lg_coin_combinations,
    )

    # Simple
    print("{:<24}".format("Simple amount (greedy):"), f"{greedy_simple:.6f} sec")
    print("{:<24}".format("Simple amount (dynamic):"), f"{dynamic_simple:.6f} sec")