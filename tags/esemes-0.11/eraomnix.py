# -*- coding: iso-8859-2 -*-
# $Id$
# moduł do wysyłania przez www.eraomnix.pl
# Copyright by skrobul@batnet.pl 2005
# Credits: sinx
# License: BSD license

import cookielib, string, urllib, urllib2

#-------------------------------------------------------------------
class moj_redirect_handler(urllib2.HTTPRedirectHandler):
	def http_error_302(self, req, fp, code, msg, headers):#{{{
		print "got response..."
		import re,sys
		error = re.search("X-ERA-error=(\d+)", str(headers)).group(1)
		if error == '1':
			print "błąd: 1 - awaria systemu"
			sys.exit(-2)
		elif error == '2':
			print "błąd: 2 - użytkownik nieautoryzowany"
			sys.exit(-2)
		elif error == '3':
			print "błąd: 3 - dostęp zablokowany"
			sys.exit(-2)
		elif error == '5': 
			print "błąd: 5 - błąd składni"
			sys.exit(-2)
		elif error == '7':
			print "błąd: 7 - wyczerpany limit"
			sys.exit(-2)
		elif error == '8':
			print "błąd: 8 - błędny adres odbiorcy"
			sys.exit(-2)
		elif error == '9':
			print "błąd: 9 - wiadomość zbyt długa"
			sys.exit(-2)
		elif error == '10':
			print "błąd: 10 -brak wymaganej liczby żetonów"
			sys.exit(-2)
		try:
			zetony  = re.search("X-ERA-counter=(\d+)", str(headers)).group(1)
			print "Pozostało: %s wiadomości" % zetony
		except Exception, e:
			print e
		urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)#}}}
#-------------------------------------------------------------------

class EraSMS: #wysylanie do sieci EraOmnix
   debug = 1
   def sendsms(self):#{{{
      baseURL='http://www.eraomnix.pl'
      cj = cookielib.CookieJar()
      opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), moj_redirect_handler)
      request = urllib2.Request(baseURL + '/msg/api/do/tinker/sponsored')
      parametry = { 'failure' : baseURL,
									'success' : baseURL, 
									'message' : self.message,
									'login' : self.login,
									'password' : self.password,
									'number' : '48' + self.number,
									'mms' : 'false'}
      postdata = urllib.unquote(urllib.urlencode(parametry))
      request.add_data(postdata)
      request.add_header('User-Agent', 'Opera/8.40 (Windows NT 5.0; U; en)')
      
      try:
			if self.debug:
				print "Sending request..."
			result = opener.open(request)
      except IOError, e:
         if self.debug:
            print 'Blad:' , e
		#}}}
		


# vim: ts=2 foldenable foldmethod=marker
