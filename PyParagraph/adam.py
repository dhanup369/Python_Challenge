import re
with open('adam.txt','r') as para:
    txt=para.read()
    
    #Initializing variables
    wordlen=[]
    para_word_len=[]

    words=txt.split(' ')  #Spliting the paragraph into words 
    word_count=len(words) #Calculating the total number of words
    
    for i in words:
        wordlen.append(len(i)) #Appending the length of each word into a list
    aver_letter_count=round(sum(wordlen)/len(wordlen),3)  #Finding the average letter count
    
    sentences = re.split("(?<=[.!?]) +", txt) #Splitting the paragraph into sentences
    
    
    for i in sentences:
        w=i.split()                     #Splitting each sentence into words 
        para_word_len.append(len(w))    #Appending the total number of words in each sentence into a list
    aver_sentence_len=sum(para_word_len)/len(para_word_len)     #Calculating the average sentence length and rounding the value to 3 decimal places
    
    
    #Printing the result to the terminal
    print("Paragraph Analysis\n--------------------------------\nApproximate word count: "+str(word_count)
    +"\nApproximate sentence count: "+str(len(sentences))+"\nAverage letter count: "+str(aver_letter_count)
    +"\nAverage sentence length: "+str(aver_sentence_len))
    
    
    
    ##Writing the results into a text file to export.
    with open ("adam.txt",'w') as file:
        file.write("Paragraph Analysis\n--------------------------------\nApproximate word count: "+str(word_count)
    +"\nApproximate sentence count: "+str(len(sentences))+"\nAverage letter count: "+str(aver_letter_count)
    +"\nAverage sentence length: "+str(aver_sentence_len))  
