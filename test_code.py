denominations_list = [1, 2, 5, 10, 20, 50, 100]


def return_change(change_amount, coin_values):
    # Make a list size of length denominations filled with 0
    to_give_back = [0] * len(coin_values)

    # Move backwards through denominations list
    # And keep track of the counter, pos.
    test_list = list(reversed(list(enumerate(coin_values))))
    print(test_list[0])

    for pos, coin in reversed(list(enumerate(coin_values))):
        print(f"current position is {pos} and value is {coin}")

    return to_give_back

print(return_change(4, denominations_list))
# returns [0, 0, 0, 1, 1, 0, 0]
# 1x 10p, 1x 20p
