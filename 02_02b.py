from collections import deque
def main():
    #add code here
    word = 'tacocat'
    palindrome = deque('noan')
    while len(palindrome) > 1:
        if palindrome.pop() != palindrome.popleft():
            return 'Not a palindrome'
    
    return 'Palindrome'
if __name__ == "__main__":
   x= main()
   print(x)