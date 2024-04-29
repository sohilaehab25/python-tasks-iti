def Arraylenandstarter(start_arr, len_arr):
    arr = list(range(start_arr, start_arr + len_arr))
    print(arr)

start_arr = input("Enter the start value of your array: ")
len_arr = input("Enter the length of array: ")
arr = []
if start_arr.isdigit() and len_arr.isdigit():
    start_arr = int(start_arr)
    len_arr = int(len_arr)
    Arraylenandstarter(start_arr, len_arr)
