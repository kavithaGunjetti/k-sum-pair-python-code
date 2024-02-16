def get_unique_pairs(int_num_list,k):
    stop_index=len(int_num_list)-1
    unique_pairs_set=set()
    for index in range(stop_index):
        first_number=int_num_list[index]
        second_number=k-first_number
        remaining_list=int_num_list[index+1:]
        if second_number in remaining_list:
            pair=(first_number,second_number)
            sorted_pair=tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)
    return unique_pairs_set
def convert_str_to_int(str_num_list):
    new_list=[]
    for item in str_num_list:
        num=int(item)
        new_list.append(num)
    return new_list

str_num_list=input().split(",")
k=int(input())
int_num_list=convert_str_to_int(str_num_list)
unique_pairs_set=get_unique_pairs(int_num_list,k)
unique_pairs_set=list(unique_pairs_set)
unique_pairs_set.sort()
for pair in unique_pairs_set:
    print(pair)