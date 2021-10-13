import sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.mathy import *
print(responses[0]);
print(responses[1]);
while True:
    print();
    text=input("Enter some text : ");
    
    for word in text.split(' '):
        
       
        if word.upper() in operations.keys():
            try:
                
                l=extract_numbers_from_text(text);
                r=operations[word.upper()](l[0],l[1]);
                print(r)
            except:
                print("something went wrong please try again ")
                
            finally:
                break;
        
        

            


        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break;



        elif extract_operator(word) in operations.keys():
            li=[]
            w=extract_operator(word);
            if w == None:
                    for word in text:
                         try:
                             li.append(float(num));
                         except:
                             pass
                    
                    for w in text:
                       for ch in w:
                            if ch in operations.keys():
                                 l=operations[ch](li[0],li[1])
                                 print(l)
                    break
            else:
                l=word.split(w);  
                if w in operations.keys():
                  r=operations[w](float(l[0]),float(l[1]))
                  print(r)
                break
        
    else:
       
       
             sorry()
    

'''        
        elif extract_operator(word) in operations.keys():
            li=[]
            for word in text:
              if word 
                try:
                   for num in word:
                     li.append(float(num));
                except:
                     pass
            for w in text:
                for ch in w:

                   if ch in operations.keys():
                       l=operations[ch](li[0],li[1])
                       print(l)
            break           
'''
        

    
    
        
