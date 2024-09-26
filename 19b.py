n=int(input("Enter the size of queue"))
que=[]
while True:
    ch=input("enqueue dequeue display exit")
    if ch=='enqueue':
        x=int(input("Enter a number"))
        if len(que)==n:
            print("queue is full")
        else:
            que.append(x)
    elif ch=='dequeue':
        if len(que)==0:
            print('stack is empty')
        else:
            print("dequeud element si",que[0])
            que.remove(que[0])
    elif ch=='display':
        print(que)

