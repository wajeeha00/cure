n=int(input())
 
 
price=list(map(int, input().split()))
clicks=list(map(int, input().split()))
 
price.sort()
clicks.sort()
 
def get_max_adv(n):
    total=0
    for item in range (n):
        total+=price[item]*clicks[item]
       
    return total
 
 
print(get_max_adv(n))