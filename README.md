
TrialOnline
===========

¿Nunca haz creado un programa Trial?, con esta librería puedes hacer un conteo trial en modo online, de esta forma el conteo es 38% más seguro que el tradicional, ahora a tus clientes puedes instalarles tu programa y decirles `te va a durar 40 días`, después de eso tu cliente no podrá usar el programa en ninguna computadora :)

---

# ventajas de esta librería

1. Puedes colocar el tiempo que durara tu aplicación trial

2. El tiempo es validado desde una url segura (protocolo online)

---

**Licencia**: [GNU GPL v3](http://www.gnu.org/licenses)

---

> ¿como puedo usarlo?

```python
date       = '2018-01-29'
validation = TrialOnline.get_trial(date)

if validation == 'not_internet':
   print ("no se pudo conectar a internet")
else:
	if validation == True:
		print ("el tiempo de uso a caducado")
	else:
		print ("el tiempo no ha caducado")
```

---

## ¿Foro de preguntas?

- Para dirigir sus comentarios, ideas de desarrollo, dudas o hablar de Python, puede hacerlo por medio del chat para programadores en español.

*sala IRC*: #python-es | #python-es_OFFTOPIC

---

## ¿Te gusta TrialOnline, quieres ayudar al proyecto?

- Si consideras que el TrialOnline vale algo para tu día a día, puedes enviarme una remesa...

eres una empresa grande, pequeña, Freelance, ¿te interesa este proyecto?, !házmelo saber!, este proyecto necesita patrocinadores que deseen ayudar al proyecto con publicidad, donativos y sugerencias, los mismos serán incluidos en los créditos del proyecto como los HÉROES :)

*correo del desarrollador*: hormigence123@gmail.com | sunfur@protomail.com
