import random
from datetime import datetime
from random import randint


def choice_sort(source_mass):
    mass = source_mass.copy()
    start_time = datetime.now()
    nums = len(mass)
    for i in range(nums-1):
        m = mass[i]
        p = i
        for j in range(i+1, nums):
            if m > mass[j]:
                m = mass[j]
                p = j
        if p != i:
            mass[i], mass[p] = mass[p], mass[i]
    end_time = datetime.now()
    print(f'Choice_sort\n{mass}\n{end_time-start_time}\n')


def inserting_sort(source_mass):
    mass = source_mass.copy()
    start_time = datetime.now()
    nums = len(mass)
    for i in range(1, nums):
        for j in range(i, 0, -1):
            if mass[j] < mass[j-1]:
                mass[j], mass[j-1] = mass[j-1], mass[j]
            else:
                break
    end_time = datetime.now()
    print(f'Inserting_sort\n{mass}\n{end_time - start_time}\n')


def bubble_sort(source_mass):
    mass = source_mass.copy()
    start_time = datetime.now()
    nums = len(mass)
    for i in range(nums-1):
        non_change = 1
        for j in range(nums-1-i):
            if mass[j] > mass[j+1]:
                mass[j], mass[j+1] = mass[j+1], mass[j]
                non_change = 0
        if non_change:
            break
    end_time = datetime.now()
    print(f'Bubble_sort\n{mass}\n{end_time - start_time}\n')


def merge_lists(list1, list2):
    sort_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sort_list.append(list1[i])
            i += 1
        else:
            sort_list.append(list2[j])
            j += 1
    sort_list += list1[i:] + list2[i:]
    return sort_list


def split_lists(source_mass):
    mass_num = len(source_mass)//2
    list1 = source_mass[:mass_num]
    list2 = source_mass[mass_num:]

    if len(list1) > 1:
        list1 = split_lists(list1)
    if len(list2) > 1:
        list2 = split_lists(list2)

    return merge_lists(list1, list2)


def merge_sort(source_mass):
    start_time = datetime.now()
    mass = split_lists(source_mass.copy())
    end_time = datetime.now()
    print(f'Merge_sort\n{mass}\n{end_time - start_time}\n')


def quick_sort_step_two(mass):
    if len(mass):
        x = mass[random.randint(0, len(mass)-1)]
        low_num = [num for num in mass if num < x]
        high_num = [num for num in mass if num > x]
        mid_num = [num for num in mass if num == x]
        mass = quick_sort_step_two(low_num) + mid_num + quick_sort_step_two(high_num)

    return mass


def quick_sort(source_mass):
    mass = source_mass.copy()
    start_time = datetime.now()
    quick_sort_step_two(mass)
    end_time = datetime.now()
    print(f'Quick_sort\n{mass}\n{end_time - start_time}\n')


def main():
    # Create mass with numbers for sort
    source_mass = [0] * 1000
    for i in range(len(source_mass)):
        source_mass[i] = randint(-99999, 99999)
    print(f'Source mass \n{source_mass}\n')

    choice_sort(source_mass)

    inserting_sort(source_mass)

    bubble_sort(source_mass)

    merge_sort(source_mass)

    quick_sort(source_mass)


if __name__ == '__main__':
    main()
