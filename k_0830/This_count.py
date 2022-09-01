A='''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors shoulde Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

B="I love you so much."

Word =['a','e','i','o','u']
Found ={'a':0,'e':0,'i':0,'o':0,'u':0}

def String_Count(Sentance):
    Sentance_lower=Sentance.lower()
    for letter in Sentance_lower:
        if letter in Found:
            Found[letter] += 1
    for v,k in Found.items():
        print(v,':',k)
         
    

if __name__=="__main__":
    print(String_Count(A))