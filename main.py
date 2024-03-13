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
print("Results for different exchange amounts made with the greedy algorithm:")
print("{:<24} {:<10}".format("Amount", "Time (sec)"))
print("{:<24} {:.6f}".format("38:", greedy_simple))
print("{:<24} {:.6f}".format("63:", greedy_sm))
print("{:<24} {:.6f}".format("431:", greedy_md))
print("{:<24} {:.6f}".format("2355:", greedy_lg))
print()

# Results for different exchange amounts made with the dynamic programming algorithm
print("Results for different exchange amounts made with the dynamic programming algorithm:")
print("{:<24} {:<10}".format("Amount", "Time (sec)"))
print("{:<24} {:.6f}".format("38:", dynamic_simple))
print("{:<24} {:.6f}".format("63:", dynamic_sm))
print("{:<24} {:.6f}".format("431:", dynamic_md))
print("{:<24} {:.6f}".format("2355:", dynamic_lg))
print()

# Coin combinations
print("Coin combinations:")
print("{:<24} {:<35} {:<35}".format("Algorithm", "63:", "431:"))
print("{:<24} {:<35} {:<35}".format("Greedy algorithm:", str(greedy_sm_coin_combinations), str(greedy_md_coin_combinations)))
print("{:<24} {:<35} {:<35}".format("Dynamic programming:", str(dynamic_sm_coin_combinations), str(dynamic_md_coin_combinations)))
print()

# Simple amounts
print("Time for simple amounts:")
print("{:<24} {:.6f}".format("Greedy:", greedy_simple))
print("{:<24} {:.6f}".format("Dynamic programming:", dynamic_simple))
