# num_list = [1721, 979, 366, 299, 675, 1456]

num_list = open('nums.txt')

# for num in num_list:
#     print(num)

num_list = list(num_list)

for num in num_list:
    num = int(num)

def calc_sum_2020(list):
    start_num = 0
    
    for num in list:
        if start_num == 0:
            start_num = num
        
        if num + start_num == 2020:
            sum = num * start_num
            print(f'The sum of {num} and {start_num} is equal to 2020')
            
    
    return sum