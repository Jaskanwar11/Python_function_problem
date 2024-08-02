def even_num_gen(lim):
    for i in range(2, lim+1, 2):
        yield i
    
for num in even_num_gen(10):
    print (num)