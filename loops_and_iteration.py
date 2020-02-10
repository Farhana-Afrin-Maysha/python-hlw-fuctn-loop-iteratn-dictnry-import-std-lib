nums = [1,2,3,4,5,6,7,8,9]
# for loop
for num in nums:
    if num == 3:
       print('Found!')
       continue
    if num == 8:
       break
    print(num)

# nested loop
for num in nums:
    for letter in 'abc' :
        print(num, letter)

# range
for i in range(1,11):
    print(i)

#while loop
x = 0

while x < 10:
    if x == 5:
       break
    print(x)
    x += 1

# condition for getting infinity nums
# x = 0
#
# while True:
#     # print(x)
    # x += 1