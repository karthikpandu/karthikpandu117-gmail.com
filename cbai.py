#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Description : This is a chatbot program
#import the library
from nltk.chat.util import Chat, reflections
reflections
pairs = [
    ['(hi|hello|hey|holla|hola)', ['hey there', 'hi there', 'hayyyy']],
    ['my name is (.*)', ['hi %1']],
    ['(.*) is your name ?' ,['my name is Alex']],
    ['(.*) created you ?', ['karthik created using nltk']],
    ['(.*) season is going now ?' , ['spring runs from march 1 to may 31; summer runs from june 1 to august 31; autumn runs from september 1 to november 30, and winter from december 1 to february 28 ']],
    ['(.*) is my (location|city) ?' ,[ 'Tirupati, India']],
    ['how is the weather in (.*)' , ['the weather in %1 is amazing like always']],
    ['(.*) help (.*)', ['I can help you']],
    ['(.*) is fullform of ai', ['Artificial intelligence']],
    ['(.*) is father of artificial intelligence' , ['Father of Artificial intelligence is John McCarthy']],
    ['(.*) this application about ? ' , ['This application is to solve general queries.']],
    ['(.*) what general queries you deal with?',['Basic queries of artificial intelligence and some basic courses for internships.']],
    ['(.*) are those internship courses?',['Data Science for Python, Machine learning, Cyber Security, SQL, Web development, Android Development, Digital Marketing, Photography, Graphic design']],
    ['(.*) will be the time duration and cost of each course?', ['Time duration is 3 months and now all the courses are in ofeer so you can avail it for $32.9 per course']],
    ['thanks for the information',['Welcome! It was nice talking to you feel free if have any queries.']],
    ['sure and thanks',['welcome! Have a nice day']],
]
chat = Chat(pairs, reflections)
chat.converse()


# In[ ]:


reflections


# In[ ]:


reflections


# In[ ]:




