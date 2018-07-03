import string
with open ('resume.txt','r') as myfile:
       lines=list(myfile.read().split())
       words=[word.lower().strip(string.punctuation) for word in lines]
       words[:] = [i for i in words if i !='']
       words[:]=[i for i in words if i !='and']
       words[:]=[i for i in words if i !='in']
       words[:]=[i for i in words if i !='the']
       words[:]=[i for i in words if i !='to']
       words[:]=[i for i in words if i !='from']
       words[:]=[i for i in words if i !='with']
       words[:]=[i for i in words if i !='using']
       words[:]=[i for i in words if i !='working']
       unique=set(words)
       dic={}
       c=[]
       REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
       DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}
       print(unique&REQUIRED_SKILLS)
       print(unique&DESIRED_SKILLS)
       for i in words:
           c.append(words.count(i))
       wordic=dict(zip(words,c)) 
       import operator
       sorted_wordic = sorted(wordic.items(), key=operator.itemgetter(1),reverse=True)
       for i in range(5):
           print(sorted_wordic[i])
       
       
       sorted_wordic
       
      