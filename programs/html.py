import requests
import json
import pprint
import random
import html

url="https://opentdb.com/api.php?amount=1"
endgame=""

while endgame!="quit":
     r=requests.get(url)
     if (r.status_code!=200):
       endgame=input("SORRY THERE WAS A PROBLEM, PRESS ENTER TO TRY AGAIN OR TO QUIT TYPE QUIT")
     else:
          data=json.loads(r.text)      
          question=data['results'][0]['question']
          answers=data['results'][0]['incorrect_answers]
          correct_answer=data['results'][0]['correct_answer']
          answers.append(correct_answer)
          random.shuffle(answers)
          
          
          print(html.unescape(question)+"\n")
          
          for answer in answers:
              print(html.unescape(answer))
              
          input("")
