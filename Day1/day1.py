# James Macak
# 11.9.20

fh = open('input.txt', 'r')
captcha = fh.readline()
fh.close()

#captcha = list(map(int, captcha)) # alternative
captcha = [int(d) for d in captcha] # maps text file input to list of integers
captcha.append(captcha[0]) # the captcha is circular
sum = 0
for i, cur in enumerate(captcha[:-1]):
    nxt = captcha[i+1]
    if cur == nxt:
        sum += cur

print(str(sum))