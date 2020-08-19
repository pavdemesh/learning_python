denominations_list = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1


def return_change(change_amount, coin_values):
    # Make a list size of length denominations filled with 0
    to_give_back = [0] * len(coin_values)

    # Move backwards through denominations list
    # And keep track of the counter, pos.
    # Index (pos) will correspond with the index of this coin in the initial array!
    for pos, coin in reversed(list(enumerate(coin_values))):
        # print(f"current position is {pos} and value is {coin}")
        # While we can still use coin, use it until we can't
        while coin <= change_amount:
            change_amount = change_amount - coin
            # print(f"remaining change to give back is {change_amount}")
            to_give_back[pos] += 1
            # print(f"number of coins with value {coin} is {to_give_back[pos]}")
            # print(f"index in the list is {pos}")
    # Print out the result in readable form:
    # print(to_give_back)
    for index, coin in enumerate(to_give_back):
        if coin > 0:
            print(f"You will need {coin} coin(s) with denomination of {denominations_list[index]}")
    return to_give_back


# print(return_change(42, denominations_list))
return_change(39, denominations_list)
