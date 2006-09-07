# -*- coding: iso-8859-2 -*-
# eSeMes - orange module
# $Id$
# Copyright by skrobul@batnet.pl 2005
# License: BSD license

# funkcja wysyłająca smsy została napisana przez
# Rodiona -> http://miracle7.info/orangembox.php

import cookielib, string, urllib, urllib2

class OrangeSMS: # wysylanie do sieci Orange
	def sendsms(self):#{{{
		baseURLSSL='https://www.orange.pl'
		baseURL='http://www.orange.pl'
		length = 634 - len(self.message)
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		# orange index#{{{
		request = urllib2.Request(baseURLSSL)
		request.add_header('User-Agent', 'Opera/9.00 (Windows NT 5.0; U; en)')
		try:
		    result = opener.open(request)
		    if self.debug:
		        print 'Connecting with',baseURLSSL
		except IOError:
		    print 'Connection with %s failed.' % baseURLSSL#}}}
		
		# orange map#{{{
		request = urllib2.Request(baseURLSSL + '/portal/map/map/')
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		try:
		    result = opener.open(request)
		    if self.debug:
		        print 'Connecting with www.orange.pl/portal/map/map'
		except IOError:
		    print 'Connection with https://www.orange.pl/portal/map/map failed.'#}}}
		
		# orange login#{{{
		parmdicta = {
                 '_dyncharset' : 'UTF-8',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.loginErrorURL' : '/portal/map/map/signin',
                 '_D:/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.loginErrorURL' : ' ',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.loginSuccessURL' : 'http://www.orange.pl/portal/map/map/pim',
                 '_D:/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.loginSuccessURL' : ' ',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.value.login' : self.login,
                 '_D:/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.value.login' : ' ',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.value.password' : self.password,
                 '_D:/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.value.password' : ' ',
                 '_D:/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.login' : ' ',
                 '_DARGS' : '/gear/static/home/login.jsp.loginFormId',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.login' : ' ',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.login.x' : '5',
                 '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.login.y' : '5'}
		request = urllib2.Request(baseURLSSL + '/portal/map/map/homeo?_DARGS=/gear/static/home/login.jsp.loginFormId')
		postdata = urllib.unquote(urllib.urlencode(parmdicta))
		request.add_data(postdata)
		request.add_header('User-Agent', 'Opera/8.10 (Windows NT 5.0; U; en)')
		try:
		    result = opener.open(request)
		    if self.debug:
		        print 'Logged'
		except IOError:
		    print 'Not logged'#}}}
	  	
		# orange SMS form#{{{
		request = urllib2.Request(baseURL + '/portal/map/map/message_box?mbox_view=newsms&mbox_edit=new')
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		try:
		    result = opener.open(request)
		    if self.debug:
		        print 'Opening SMS form'
		except IOError:
		    print 'Open SMS form failed.'#}}}
		
		# Send SMS#{{{
		parmdictb = {'_dyncharset': 'UTF-8',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.type': 'sms',
		             '_D:/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.type' : ' ',
		             'enabled': 'true',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.errorURL': '/portal/map/map/message_box?mbox_view=newsms',
		             '_D:/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.errorURL': ' ',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.successURL': '/portal/map/map/message_box?mbox_view=messageslist',
		             '_D:/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.successURL': ' ',
		             'smscounter' : '1',
		             'counter': '630',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.to': self.number,
		             '_D:/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.to': ' ',
		             '_D:/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.body': ' ',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.body': self.sender+' : '+self.message,
		             '_D:/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.create': ' ',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.create': 'Wyżlij',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.create.x': '5',
		             '/amg/ptk/map/messagebox/formhandlers/MessageFormHandler.create.y': '5',
		             '_DARGS': '/gear/mapmessagebox/smsform.jsp'}
		
		request = urllib2.Request(baseURL + '/portal/map/map/message_box?_DARGS=/gear/mapmessagebox/smsform.jsp')
		postdata = urllib.unquote(urllib.urlencode(parmdictb))
		request.add_data(postdata)
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		try:
		    result = opener.open(request)
		    if self.debug:
		        print 'SMS sended.'
		except IOError:
		    print 'SMS not send.'
		smsy = self.zostalo(result.read())
		smsy_darmowe = 0
		if len(smsy) == 1:
			smsy_darmowe =  smsy[0]
			smsy_doladowane = 0
		if len(smsy) == 2:
			smsy_darmowe =  smsy[0]
			smsy_doladowane = smsy[1];
		if smsy_darmowe and self.debug:
			print 'Orange -> Zostalo: %s+%s SMS' % (smsy_darmowe, smsy_doladowane)
				#}}}

		# Logout#{{{
		parmdictc = {'_dyncharset' : 'UTF-8',
		             'enabled' : 'true',
		             '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.logout.x' : '0',
		             '/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.logout.y' : '0',
		             '_D:/amg/ptk/map/core/formhandlers/AdvancedProfileFormHandler.logout' : ' ',
		             '_DARGS': '/portal/layoutTemplates/html/user_status.jsp'}
		
		request = urllib2.Request(baseURL + '/portal/map/map?_DARGS=/portal/layoutTemplates/html/user_status.jsp')
		postdata = urllib.unquote(urllib.urlencode(parmdictc))
		request.add_data(postdata)
		request.add_header('User-Agent', 'Opera/8.00 (Windows NT 5.0; U; en)')
		try:
		    result = opener.open(request)
		    if self.debug:
		        print 'Logout.'
		except IOError:
		    print 'Logout error.'#}}}#}}}

	def zostalo(self, tekst):#{{{
		import re
		p = re.compile('<div class="value">(\d+)</div>')
		smsy =  p.findall(tekst)
		return smsy

#	vim: ts=2 foldmethod=marker
