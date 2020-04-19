T = int(input())
for t in range(1, T + 1):
    data = input()
    answer = ''
    original_list = list(data)
    n = len(original_list)

    opened = 0
    for k in range(0, n+1):
        if k == n:
            answer = answer + (')'*opened)
        else:
            delta = int(original_list[k]) - opened
            if delta > 0:
                answer = answer + ('('*delta) + original_list[k]
                opened = int(original_list[k])
            if delta == 0:
                answer = answer + original_list[k]
                opened = int(original_list[k])
            if delta < 0:
                answer = answer + (')'*abs(delta)) + original_list[k]
                opened = int(original_list[k])
            

    # Print results
    print("Case #{}: ".format(t)+answer)
        

    
        
    

