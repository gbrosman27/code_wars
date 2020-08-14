# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.
# Note: no empty arrays will be given.
# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


# def highest_rank(arr):
#     counter = 0
#     num = arr[0] 
      
#     for i in arr: 
#         curr_frequency = arr.count(i) 
#         if(curr_frequency > counter): 
#             counter = curr_frequency 
#             num = i 
            
#     return num 

def highest_rank(arr):
    return max(sorted(arr,reverse=True), key=arr.count)

print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))