# -*- coding: iso-8859-2 -*-

import os,re 

class KsiazkaTelefoniczna:
	def __init__(self):
		self.ksiazka = {}
		self.otworzplik('r+')
		self.przeparsuj()

	def otworzplik(self, tryb):
		bpath = os.path.expanduser('~/.smsaddr')
		try:
			self.bookfile = open(bpath, tryb)
		except IOError:
			print 'Nie można otworzyć pliku książki telefonicznej. Tworze pusta ksiazke tel.'
			self.bookfile = open(bpath, "w")
			
	def __destroy__(self):
		if self.bookfile:
			print 'Zamknalem plik'
			self.bookfile.close()

	def przeparsuj(self):
		for linia in self.bookfile:
			wpis = re.match("^([^0-9]+):(\d+)$", linia)
			if wpis and not self.podajnumer(wpis.group(1)):
				nazwa = wpis.group(1)
				numer = wpis.group(2)
				self.ksiazka[nazwa] = numer
	
	def podajnumer(self, nazwa):
		try:
		 numer = self.ksiazka[nazwa]
		 return numer
		except KeyError:
			return None

	def zapisz(self):
			self.otworzplik("w")
			for nazwa in self.ksiazka:
				self.bookfile.write(nazwa + ':' + self.ksiazka[nazwa] + '\n') 
			self.otworzplik("r")

	def usun(self, co):
		if self.ksiazka.has_key(co):
			del self.ksiazka[co]
			self.zapisz()

	def dodaj(self, nazwa, numer):
		if numer.isdigit() and len(numer) == 9 and not self.podajnumer(nazwa):
			self.ksiazka[nazwa] = numer
			self.zapisz()


# vim: ts=2	
