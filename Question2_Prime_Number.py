Enter = input("Enter the number that you want to find the prime number of them :")
for num in range (0, 100):
    if all(num%i !=0 for i in range(2,num)):
        print(Enter,num)

# lower = 900
# upper = 1000
# print("Prime number between", lower "and" , upper "are":)
# for num in range(lower,upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#             else:
#               print(num)