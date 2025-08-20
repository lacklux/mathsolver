def solve_mean(user_input):
    ans = {
        "steps": {}
    }
    sum_num = sum(user_input)
    ans["steps"]["step_1"] = f"The sum of the values is: {sum_num}"

    val_count = len(user_input)
    ans["steps"]["step_2"] = f"The count of the values is: {val_count}"

    mean_cal = sum_num / val_count
    ans["steps"]["step_3"] = f"The answer for the above problem is: {sum_num} / {val_count} = {mean_cal}"

    ans["solution"] = mean_cal

    return ans


print(solve_mean([1, 2, 3, 4, 5]))






def solve_median(user_input):
    ans = {
        "steps": {}
    }

    ans["steps"]["step_0"] = f"Values given are: {user_input}"

    val_len = len(user_input)
    ans["steps"]["step_1"] = f"The count of the values is: {val_len}"

    if val_len % 2 != 0:
        position = (val_len + 1) // 2  
        ans["steps"]["step_2"] = f"Since {val_len} is odd, we use (n + 1) / 2"
        ans["steps"]["step_3"] = f"({val_len} + 1) / 2 = {position}"
        median = user_input[position - 1] 
        ans["steps"]["step_4"] = f"The {position}th element is {median}"
        ans["steps"]["step_5"] = f"Therefore, the median is {median}"

    else:
        mid1 = val_len // 2
        mid2 = mid1 + 1
        ans["steps"]["step_2"] = f"Since {val_len} is even, median is average of {mid1}th and {mid2}th elements"
        ans["steps"]["step_3"] = f"Positions: {mid1} and {mid2}"

        num1 = user_input[mid1 - 1]  
        num2 = user_input[mid2 - 1]
        ans["steps"]["step_4"] = f"The {mid1}th element is {num1}"
        ans["steps"]["step_5"] = f"The {mid2}th element is {num2}"

        median = (num1 + num2) / 2
        ans["steps"]["step_6"] = f"Median = ({num1} + {num2}) / 2 = {median}"
        ans["steps"]["step_7"] = f"Therefore, the median is {median}"

    ans["solution"] = median
    return ans

print(solve_median([1,2,3,4,5,6]))





# # mode
def solve_mode(user_input):
    ans = {
        "steps": {}
    }

    ans["steps"]["step_0"] = f"Values given are: {user_input}"

    frequency = {}
    for num in user_input:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    ans["steps"]["step_1"] = f"Count the frequency of each number: {frequency}"

    max_frequency = max(frequency.values())
    ans["steps"]["step_2"] = f"The highest frequency is: {max_frequency}"

    mode_values = []
    for num, freq in frequency.items():
        if freq == max_frequency:
            mode_values.append(num)
    ans["steps"]["step_3"] = f"The number(s) with this frequency are: {mode_values}"

    ans["solution"] = mode_values
    return ans

print(solve_mode([1,2,3,2,4,6,8,8,8,8,4,5,6]))


# # range
def solve_range(user_input):
    ans = {
        "steps": {}
    }

    ans["steps"]["step_0"] = f"Values given are: {user_input}"

    max_range = max(user_input)
    ans["steps"]["step_1"] = f"The maximum number is: {max_range}"

    min_range = min(user_input)
    ans["steps"]["step_2"] = f"The minimum number is: {min_range}"

    range_solve = max_range - min_range
    ans["steps"]["step_3"] = f"Range = {max_range} - {min_range} = {range_solve}"

    ans["solution"] = range_solve

    return ans


print(solve_range([1,2,3,2,4,6,8,8,8,8,4,5,6]))




   


    