# -*- coding: utf-8 -*-

import TrialOnline

caducar = '2018-01-29'
validacion = TrialOnline.get_trial(caducar)

if validacion == 'not_internet':
   print ('no se pudo conectar a internet')
else:
	if validacion == True:
		print ('el tiempo de uso a caducado')
	else:
		print ('el tiempo no ha caducado')


# Nota : tu aplicación debe estar ofuscada y complicada, para mayor seguridad de lo contrario el sistema podría ser hackeado por terceros.
