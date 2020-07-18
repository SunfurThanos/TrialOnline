# -*- coding: utf-8 -*-

"""
	Author  : Sunfur Thanos

	Country : Venezuela

	License : GNU GPL v3 <http://www.gnu.org/licenses/>

	Copyright (C) 2014 Sunfur Thanos. All rights reserved.

"""

#--------------------------------------------------------------------------------------------------

import sys

#--------------------------------------------------------------------------------------------------

if sys.version_info[0] == 3:
	def get_trial(DATE_CADUCATION):
		import urllib
		from urllib import request

		def internet_on():
		    try:
		        urllib.request.urlopen('http://google.com')
		        return True
		    except:
		        return False

		if internet_on() == False: return '\x6e\x6f\x74\x5f\x69\x6e\x74\x65\x72\x6e\x65\x74'

		ONLINE = '\x68\x74\x74\x70\x3a\x2f\x2f\x6a\x75\x73\x74\x2d\x74\x68\x65\x2d\x74\x69\x6d\x65\x2e\x61\x70\x70\x73\x70\x6f\x74\x2e\x63\x6f\x6d\x2f'

		data = urllib.request.urlopen(ONLINE).read()
		TROLL      = int(data.split(b' ')[0].replace(b'-',b''))
		oraculo    = int(DATE_CADUCATION.replace('-',''))

		if TROLL > oraculo:
		   return True

		return False
else:
	import urllib2

	def get_trial(DATE_CADUCATION):
		def test_conection():
		  try:
		     response = urllib2.urlopen('https://www.google.co.ve', timeout=0x2)
		     reporte  = True
		  except:
		     reporte = False
		  return reporte
		ONLINE = '\x68\x74\x74\x70\x3a\x2f\x2f\x6a\x75\x73\x74\x2d\x74\x68\x65\x2d\x74\x69\x6d\x65\x2e\x61\x70\x70\x73\x70\x6f\x74\x2e\x63\x6f\x6d\x2f'
		if test_conection() == False: return '\x6e\x6f\x74\x5f\x69\x6e\x74\x65\x72\x6e\x65\x74'
		Thanos     = urllib2.urlopen( ONLINE )
		Wacth_dogs = Thanos.read()
		TROLL      = int(Wacth_dogs.split(' ')[0].replace('-',''))
		oraculo    = int(DATE_CADUCATION.replace('-',''))
		if TROLL > oraculo:
		   return True
		return False
