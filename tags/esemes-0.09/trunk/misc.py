#!/usr/bin/python2.4
class Misc:
   def podziel(self, wejscie, chunksize):
      """Dzieli dlugiego smsa na czesci. Zwraca liste"""
      nowa = []
      czesci = len(wejscie) // chunksize
      for i in range(0,czesci+1):
			nowa.append(wejscie[i*chunksize:i*chunksize+chunksize])
      return nowa

# vim: ts=2

