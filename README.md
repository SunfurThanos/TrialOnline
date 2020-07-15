
TrialOnline
===========

Have you never created a Trial program? With this library you can do a trial count in online mode, this way the count is 38% safer than the traditional one, now you can install your program for your clients and say `it will take you 40 days`, after that your client will not be able to use the program on any computer :)

---

# advantages of this bookstore

1. You can enter the duration of your trial application

2. The time is validated from a secure url (online protocol)

---

**license**: [GNU GPL v3](http://www.gnu.org/licenses)

---

> How can i use it?

```python
date       = '2018-01-29'
validation = TrialOnline.get_trial(date)

if validation == 'not_internet':
   print ("could not connect to the internet")
else:
	if validation == True:
		print ("usage time to expired")
	else:
		print ("time has not expired")
```

---

## ¿Foro de preguntas en español?

- Para dirigir sus comentarios, ideas de desarrollo, dudas o hablar de Python, puede hacerlo por medio del chat para programadores en español.

*sala IRC*: #python-es | #python-es_OFFTOPIC

---

## ¿Te gusta TrialOnline, quieres ayudar al proyecto?

- If you consider that the TrialOnline is worth something for your day to day, you can send me a remittance ...

you are a large, small, Freelance company, are you interested in this project ?, let me know !, this project needs sponsors who want to help the project with advertising, donations and suggestions, they will be included in the credits of the project as the HEROES: )

*developer contact*: hormigence123@gmail.com | sunfur@protomail.com
