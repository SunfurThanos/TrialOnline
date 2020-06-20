
TrialOnline
===========

¿Nunca haz creado un programa Trial?, con esta librería puedes hacer un conteo trial, pero por vía web, de esta forma el conteo es 38% más seguro que el tradicional, ahora a tus clientes puedes instalarles tu programa y decirles `te va a durar 40 días`, después de eso tu cliente no podrá usar el programa en ninguna computadora :)

---

# ventajas de la librería

1. Puedes colocar el tiempo que durara tu aplicación trial

2. El tiempo es validado desde una url segura (protocolo online)

---

**Licencia**: [GNU GPL v3](http://www.gnu.org/licenses)

---

> ¿como puedo usarlo?

```python
import TrialOnline

caducar = '2021-01-29'
validacion = TrialOnline.get_trial(caducar)

if validacion == 'not_internet':
   print ('no se pudo conectar a internet')
else:
	if validacion == True:
		print ('el tiempo de uso a caducado')
	else:
		print ('el tiempo no ha caducado')
```
