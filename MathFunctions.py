import sys


def codecool_func(codecool_list, stats=False):
    codecool_len = 0

    if stats is True:
        nested_codecool_list = codecool_list[:]  # Create a NEW list on the base of original one...
        while codecool_list:  # But still loop through lenght of original "codecool_list"...
            codecool_len += 1
            element = codecool_list.pop()  # ... and to do that, delete items only in original list.

            for element in nested_codecool_list:
                if type(element) == list:
                    nested_codecool_list.remove(element)  # Delete current sublist element.
                    for sub_element in element:
                        nested_codecool_list.append(sub_element)  # ... and replace it by unpacked values from that sublist.

        codecool_list = nested_codecool_list  # Override the original "codecool_list" by new "nested_codecool_list" values.
        return codecool_list

    elif stats is False:  # Works also with "stats == False", but it is better practive to use "is" with booleans.
        return codecool_list


def calculations(codecool_list):
    codecool_len = 0
    codecool_len_int = 0
    codecool_len_other = 0
    for element in codecool_list:  # Comparing the min/max elements.
        if type(element) == int:
            codecool_min = element
            codecool_max = element
    codecool_mean = 0

    element = None  # Unknown item, which have no value (for not suggesting that it may be integer if = "0").

    while codecool_list:
        codecool_len += 1
        element = codecool_list.pop()  # Remember last deleted item to proceed with it in next lines.
        if type(element) == int:
            codecool_len_int += 1
            if element < codecool_min:
                codecool_min = element
            if element > codecool_max:
                codecool_max = element
            codecool_mean += element
        else:
            codecool_len_other += 1
    codecool_mean /= codecool_len_int  # Sum of elements in "codecool_mean" divide by number of all integer elements.

    return codecool_len, codecool_len_int, codecool_len_other, codecool_min, codecool_max, codecool_mean  # If return many elements after comma, this function returns tuple.


def codecool_func_print(return_from_calculations):
    print("\n" + str(return_from_calculations))


def codecool_func_advanced_print(return_from_calculations):
    all_lenght = return_from_calculations[0]
    int_lenght = return_from_calculations[1]
    other_lenght = return_from_calculations[2]
    int_min = return_from_calculations[3]
    int_max = return_from_calculations[4]
    int_mean = return_from_calculations[5]
    print("\nAll items: {}, Int: {}, Others: {}, Min: {}, Max: {}, Mean: {}".format(all_lenght, int_lenght, other_lenght, int_min, int_max, round(int_mean, 5)))


def main():
    list_to_calculate = [10, 20, 30, [1, 2, 3, "burger"], [True, [1, 3], 45]]
    print(list_to_calculate)

    print("\nDo you want to consider nested lists?")
    look_inside_nested_lists = input("Type \"Yes\" or \"No\": ").lower()
    if look_inside_nested_lists == "yes":
        chose_nested_lists = True
    elif look_inside_nested_lists == "no":
        chose_nested_lists = False
    else:
        print("Wrong command!")
        sys.exit()

    # original_list = codecool_func([10, -2, 5, True, "piwo", 12, 0, 100])  # Now "original_list" is a tuple from "codecool_func" return.
    # v1, v2, v3 = codecool_func([10, -2, 5, True, "piwo", 12, 0, 100])  # There must be exact the same elements on the left, as from right (1 tuple).
    original_list = codecool_func(list_to_calculate, chose_nested_lists)
    calculate_list = calculations(original_list)
    # codecool_func_print(calculate_list)
    codecool_func_advanced_print(calculate_list)

main()
