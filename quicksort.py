import statistics
import random
def quicksort(numbers):
    if len(numbers)<=1:
        return numbers
    else:
        pivot=statistics.median([numbers[0],numbers[(len(numbers)//2)],numbers[-1]])
        item_less,pivot_item,item_greater=(
            [n for n in numbers if n<pivot],
            [n for n in numbers if n==pivot],
            [n for n in numbers if n>pivot])
        print(item_less,pivot_item,item_greater)
        return(quicksort(item_less)+ pivot_item + quicksort(item_greater))

def get_random_numbers(length,min_number,max_number):
    return [random.randint(min_number,max_number) for _ in range(length)]

if __name__=='__main__':
    nums = get_random_numbers(10, -50, 50)
    print(nums)
    nums_sorted = quicksort(nums)
    print(nums_sorted)




