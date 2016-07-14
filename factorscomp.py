#! python3

def get_factors(number):
    return [n for n in range(1, number + 1) if number % n == 0]

new_dict = {}
def get_all_factors(numbers_set):
    #for i in numbers_set:
    #    new_dict[i] = get_factors(i)
    #print(new_dict)
    new_dict = {i:get_factors(i) for i in numbers_set}
    print(new_dict)
get_all_factors({1, 2, 3, 4})
get_all_factors({62, 293, 314})
