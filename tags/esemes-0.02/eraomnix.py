# -*- coding: iso-8859-2 -*-
# $Id$
# moduł do wysyłania przez www.miastoplusa.pl
# Copyright by skrobul@batnet.pl 2005
# Credits: sinx
# License: BSD license

import cookielib, string, urllib, urllib2

class EraSMS: #wysylanie do sieci EraOmnix

	def sendsms(self):
		baseURL='http://www.eraomnix.pl'
		actionURL='http://www.eraomnix.pl/msg/api/do/tinker/sponsored'
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		request = urllib2.Request(baseURL + '/msg/api/do/tinker/sponsored')
		parametry = { 'failure' : baseURL,
									'success' : baseURL,
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
#				print 'Blad http %s: %s ' % (e.reason, e.code)
#				print e.read()
				print 'dupa zbita'




# vim: ts=2 foldenable foldmethod=marker

