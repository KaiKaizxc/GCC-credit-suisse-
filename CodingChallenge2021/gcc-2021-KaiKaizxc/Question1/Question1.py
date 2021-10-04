def sol(n):
   #add code here
    remainer= n%3
    no_of_bills_1= no_of_bills_2= n//3 
    if remainer== 2:
        no_of_bills_2 +=1 
    elif remainer ==1: 
        no_of_bills_1 +=1
    return no_of_bills_1+ no_of_bills_2 
# do not edit below code
def main():
    n=int(input())
    print(sol(n))

if __name__ == '__main__':
    main()
