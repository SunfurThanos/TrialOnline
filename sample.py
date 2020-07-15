# -*- coding: utf-8 -*-

import TrialOnline

#--------------------------------------------------------------------------------------------------

date       = '2018-01-29'
validation = TrialOnline.get_trial(date)

#--------------------------------------------------------------------------------------------------

if validation == 'not_internet':
   print ("could not connect to the internet")
else:
	if validation == True:
		print ("usage time to expired")
	else:
		print ("time has not expired")

#--------------------------------------------------------------------------------------------------

# Note: your application must be obfuscated, complicated and compiled, for greater security otherwise the system could be hacked by third parties.
