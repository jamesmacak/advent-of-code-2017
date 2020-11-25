# James Macak
# 11.11.20

with open('input.txt', 'r') as lines:
    nums = [[int(num) for num in x.split('\t')] for x in lines]

checksum = 0
for row in nums:
    # uncomment for part 1
    # row = [int(n) for n in row] # convert list of strings to ints
    # checksum += max(row) - min(row) # running checksum

    # part 2
    row = [int(n) for n in row] # add feature to remove odd numbers
    checksum += max(row) - min(row)

print(checksum)