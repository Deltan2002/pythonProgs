import matplotlib.pyplot as plt
import time as t

times=[]
mistakes=0

print("type 'royal challengers bangalore' faster")
input("press enter to continue")

while len(times) > 5:
      start=t.time()
      word=input("type the word: ")
      end=t.time()
      timeelapsed=end-start
      
      times.append(timeelapsed)
      
      if(word.lower()!="royal challengers bangalore"):
        mistakes+=1
      
print("you made"+str(mistakes)+"mistakes")
print("HERES YOUR EVALUATION")
t.sleep(3)

x=[1,2,3,4,5]
y=times
plt.plot(x,y)
plot.show()
