#!/usr/bin/env python
#   @author - king
#   @website - glitch.sx
#   @version - 0.1.0
import requests, re

class Mailinator(object):
	"""Mailinator is a mail service for spam"""
	def __init__(self, email):
		'''manage email, name, and domain with the object'''
		self.email 	= email
		self.name,self.domain = email.split('@')

	def set_email(self,email):
		'''change to a new email adress string'''
		self.email 	= email
		self.name,self.domain = email.split('@')

	def get_email(self):
		'''get the full email string'''
		return self.email

	def get_name(self):
		'''get everything up to the "@"'''
		return self.name

	def get_domain(self):
		'''get the domain'''
		return self.domain

	def get_mail(self):
		'''return a packed list of titles, and links'''
		mailbox 	= 'http://www.mailinator.com/feed?to=' + self.name
		response 	= requests.get(mailbox).text.encode('utf-8')
		titles 	= re.findall('''<title>(.*?)</title>''',response)
		links		= re.findall('''<link>(.*?)</link>''',response)
		return zip(titles,links)

	def read_mail(self,url):
		mail_id = url.split('=')
		url="http://mailinator.com/rendermail.jsp?msgid="+str(mail_id)
		return(requests.get(url).text.encode('utf-8'))

def main():
	'''/
	main is a unit test suite for demonstration.
	'''
	mail 			= Mailinator("example@glitch.sx")
	print(mail.get_name())
	print(mail.get_domain())
	for t,l in mail.get_mail():
		print(t,l)
		print(mail.read_mail(l) )

if __name__ == '__main__':
	main()
