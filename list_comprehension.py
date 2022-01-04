def run():
    # my_list = []
    # for a in range(1, 101):
    #     if a%3 != 0:
    #         my_list.append(a**2)
    # my_list = [i**2 for i in range(1, 101) if i%3 != 0]
    
    my_list = [i for i in range(1,100000) if (i%4 == 0 and i%6 == 0 and i%9 == 0)]
    print(my_list)
    
    
if __name__ == '__main__':
    run()