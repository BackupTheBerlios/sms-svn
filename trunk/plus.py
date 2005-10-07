# -*- coding: iso-8859-2 -*-
# $Id$
# moduł do wysyłania przez www.miastoplusa.pl
# Copyright by skrobul@batnet.pl 2005
# Credits: sinx
# License: BSD license

import cookielib, string, urllib, urllib2

class PlusSMS:

	def sendsms(self):
		baseURL='http://www.miastoplusa.pl'
		baseURLSSL='https://www.miastoplusa.pl'
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
          
		#strona główna#{{{
		request = urllib2.Request(baseURL)
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		try:
			result = opener.open(request)
			if self.debug:
				print 'Connecting with',baseURL
		except IOError:
				print 'Connection with %s failed.' % baseURL#}}}

		#logujemy sie#{{{
		request = urllib2.Request(baseURLSSL + '/auth/LoginCitizen.do')
		parametros = {	'login': self.login,
										'password' : self.password,
										'secureLogin' : 'on'}
		postdata = urllib.unquote(urllib.urlencode(parametros))
		request.add_data(postdata)
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')

		try:
			result = opener.open(request)
			if self.debug:
				print 'Logowanie do MiastaPlusa...'
		except URLError:
			print 'Blad logowania do miasta plusa'#}}}
			
		# wysylamy eska#{{{
		request = urllib2.Request(baseURL + '/sms/SendSMS2.do')
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		wiadomosc = self.message
		parametros = {'smsType' : '10',
									'phoneNumber' : self.number,
									'message' : wiadomosc,
									'notifyCode' : '0',
									'validity' : '48',
									'sendDay' : '-1',
									'sendHour' : '0',
									'sendMin' : '0',
									'userId' : '0',
									'groupId' : '0',
									'templateCategory' : '0',
									'targetURL' : '/sms/send_sms.jsp' }
		
		postdata = urllib.unquote(urllib.urlencode(parametros))
		request.add_data(postdata)
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')

		try:
			result = opener.open(request)
			if self.debug:
				print 'Opening SMS form'
		except IOError:
			print 'Open SMS form failed.'#}}}

		# Logout#{{{
		request = urllib2.Request(baseURL + '/minimal/logout_frameset.jsp')
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		try:
			result = opener.open(request)
			if self.debug:
	                  print 'Logout.'
		except IOError:
	                print 'Logout error.'#}}}

# vim: ts=2 foldenable foldmethod=marker

