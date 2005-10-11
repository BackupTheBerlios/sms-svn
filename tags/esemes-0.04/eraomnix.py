# -*- coding: iso-8859-2 -*-
# $Id$
# moduł do wysyłania przez www.miastoplusa.pl
# Copyright by skrobul@batnet.pl 2005
# Credits: sinx
# License: BSD license

import cookielib, string, urllib, urllib2

blad = ''
zostalo = ''
#-------------------------------------------------------------------
class moj_redirect_handler(urllib2.HTTPRedirectHandler):
	def http_error_302(self, req, fp, code, msg, headers):#{{{
		#import re
		#errnum = re.compile("X-ERA-error=(\d+)")
		#cost = re.compile("X-ERA-tokens=(\d+)")
		#print type(headers)
		# to be edited....

#		blad = errnum.search(headers)
#		zostalo = cost.search(headers)
		urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)#}}}
#-------------------------------------------------------------------

class EraSMS: #wysylanie do sieci EraOmnix

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
		print postdata
		request.add_data(postdata)
		request.add_header('User-Agent', 'Opera/8.40 (Windows NT 5.0; U; en)')

		try:
			result = opener.open(request)
		except IOError, e:
				if self.debug:
					print 'Blad:' , e
		print blad#}}}
		


# vim: ts=2 foldenable foldmethod=marker

