# -*- coding: utf-8 -*-

import TrialOnline

#--------------------------------------------------------------------------------------------------

date       = '2018-01-29'
validation = TrialOnline.get_trial(date)

#--------------------------------------------------------------------------------------------------

if validation == 'not_internet':
   print ("no se pudo conectar a internet")
else:
	if validation == True:
		print ("el tiempo de uso a caducado")
	else:
		print ("el tiempo no ha caducado")

#--------------------------------------------------------------------------------------------------

# Nota : tu aplicación debe estar ofuscada, complicada y compilada, para mayor seguridad de lo contrario el sistema podría ser hackeado por terceros.
