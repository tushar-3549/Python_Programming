QnA = {
       "hi" : "hello",
       "what is your name" : "My name is Tushar"
       
       }

while True:
    try:
        ques = input()
        if ques == 'quit':
            break
        else:
            print(QnA[ques])
    except:
        print("I don't know")