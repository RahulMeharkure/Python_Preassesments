def sort(lis,dict,new_lex_order):
    #in the input value is store in new_lex_order as its key
    for i in new_lex_order:
        for j in input_list:
            if i==j[0]:
                dict[i].append(j)
    #we can use dict as we want for new lexicographical
    print(dict)
if __name__=='__main__':
    new_lex_order=['r','c','t','a']
    input_list=['car','rat','cat']
    # dictionary is created in order to store input list value to its new_lex_order
    dict={keys:[] for keys in new_lex_order}
    #sorting function is called
    sort(input_list,dict,new_lex_order)

