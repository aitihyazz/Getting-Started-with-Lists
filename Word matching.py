def mat(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print("Characters with first and last letter same\n",list)
    return ctr
count=mat(["aba","jhk","121"])
print("Number of characters with first and last letter same",count)