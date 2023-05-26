def palindrome(x):
    if x!=abs(x):return False
    if x==x[::-1]:return True
    return False
print(palindrome(int(input())))