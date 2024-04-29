list_num = []
total = 0
num_count = 0

print("enter numbers. type 'done' when you finish.")
while True:
    user_input = input()
    if user_input == "done":
        break
    if user_input.isdigit():
        user_input = int(user_input)
        list_num.append(user_input)
        total += user_input
        num_count += 1
    else:
        print(f"please enter a number.")

if num_count > 0:
    num_average = total / num_count
else:
    num_average = 0

print(f"total: {total}, count: {num_count}, average: {num_average}")
