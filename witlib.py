#!/usr/bin/env python

import json
from wit import Wit # Refer: https://github.com/wit-ai/pywit

class WitAdapter:
	def __init__(self, token):
		"""Create object with wit access token"""
		self.wit = Wit(token)

	def response(self, message):
		"""Returns wit response"""

		try:
			result = self.wit.message(message)
			print("Got response from wit.ai", json.dumps(result, indent=2))
			return list(result["entities"]["intent"])[0]["value"]
		except:
			return "Sorry, I didn't understand!"
