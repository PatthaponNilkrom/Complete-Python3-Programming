n=int(input())
for x in range(n):
    text = ""
    for y in range(2*x+1):
        text+="*"
    print(" "*(n-x),text)