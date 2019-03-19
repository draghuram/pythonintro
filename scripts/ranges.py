import sys

numbers = sys.argv[1:]
size = len(numbers)

curr_range = [int(numbers[0])]

print()
for i in range(size):
    val = int(numbers[i])
    if i > 0:
        prev_val = int(numbers[i-1])
        if prev_val+1 == val:
            curr_range.append(val)
        else:
            print(curr_range)
            curr_range = [val]

print(curr_range)

            



