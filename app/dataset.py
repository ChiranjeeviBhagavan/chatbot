
data={"intents":[
{"tag": "welcome",
"patterns":["Hi","Hello","How are you","whats up", "How do you do","How’s the day?","Hey are you there","How is everything going","glad to meet you"],
"responses":["Hello","Glad to see you again", "Hi there, How can I help  you", "Hello! what you are looking for?", "Hello, how may I help you"],
},
{"tag": "endingnote",
"patterns":["see you. bye","Good Bye","ok then bye","That’ s enough for me"," Im leaving","See u later! Goodbye","nice to meet you" , "The bargaining session was fun!I’m happy that I got it at cheap price, see u again","Enjoyed the experience, good bye"],
"responses":["Hey, Thank you for visiting","Hope to see you again, it was nice talking with you", " wish you a good day! Hope to have a talk with you later","Thanks for your time with us.Hope you enjoyed it and satisfied. See you later", "Sad to see you go. Come whenever you need to bye from us. Stay intouch."],
},
{"tag": "name",
"patterns":["whats you name?","who are you?","what can I call you","tell me your name","Are u a robot","Are you a chatbot"],
"responses":["It’s FinBot here, a digital+financial assistant to help you out","You can call me FinBot.Im a chatRobot/chatbot, tell me what you want", "I’m FinBot,a digital+financial assistant, I can guide you in our ecommerce website.", "Its FinBot Here,a digital +financial assistant. How may I help you?"],
}
]
}

import json
def generateJson(path, data):
  filepathname='./'+'financial_data'+'.json'
  print(filepathname)
  with open(filepathname,'w') as fp:
    json.dump(data,fp)

generateJson('./', data)

def readIntent():
  with open('./financial_data.json', 'r') as f:
    intents = json.load(f)
  return intents
