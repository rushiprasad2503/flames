name1=input()
name2=input()
while not(name1.isalpha() and name2.isalpha()) or name1==name2:
    print("Invalid Input. Please enter names containing only alphabets.")
    name1=input()
    name2=input()
def flame(name1,name2):
    name1=name1.lower()
    name2= name2.lower()
    for i in name1:
        if i in name2:
            name1=name1.replace(i,'',1)
            name2=name2.replace(i,'',1)
    count=len(name1)+len(name2)
    flames=['F','L','A','M','E','S']
    remove_index=(count%len(flames))-1
    while len(flames)>1:
        flames.pop(remove_index)
        remove_index=(remove_index+count-1)%len(flames)
    return flames[0]
def percent(name1,name2):   
    full_name=name1+name2
    list_of_chars=[]
    i=0
    while i<len(full_name):
        count_char=(full_name).count(full_name[i])
        list_of_chars.append(count_char)
        full_name=full_name.replace(full_name[i],'')
    return list_of_chars
def percentage(list_of_number):
    while len(list_of_number)>2:
        new_list=[]
        j=len(list_of_number)-1
        if (j+1)%2:
            for i in range((j+1)//2):
                list1=[]
                sum_num=list_of_number[i]+list_of_number[j-i]
                sum_num=int(sum_num)
                        #print(sum_num)
                while sum_num>9:
                    list1.append(sum_num%10)
                    sum_num=sum_num//10
                list1.append(sum_num)
                list1.reverse()
                #print(list1)
                new_list.extend(list1)
            new_list.append(list_of_number[len(list_of_number)//2])
        else:
            for i in range(len(list_of_number)//2):
                list1=[]
                sum_num=list_of_number[i]+list_of_number[j-i]
                sum_num=int(sum_num)
                while sum_num>9:
                    list1.append(sum_num%10)
                    sum_num=sum_num//10
                list1.append(sum_num)
                list1.reverse()
                new_list.extend(list1)
                    
        list_of_number=[]
        #print(new_list)
        list_of_number.extend(new_list)
    return str(list_of_number[0])+str(list_of_number[1])
#print(percentage([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(f"FLAMES Result: {flame(name1,name2)}")
print(f"Percentage Result: {percentage(percent(name1,name2))}%")