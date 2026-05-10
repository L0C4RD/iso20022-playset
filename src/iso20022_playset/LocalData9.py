import base_types
import ISOMax3ALanguageCode
import Max40KText

class LocalData9(base_types._BaseFieldType):

	__slots__ = ["_TxtMsg", "_Lang"]
	@property
	def TxtMsg(self):
		return self._TxtMsg

	@TxtMsg.setter
	def TxtMsg(self, value):
		self._TxtMsg = value if type(value) != auto else self.make_default("TxtMsg")

	@TxtMsg.deleter
	def TxtMsg(self):
		del self._TxtMsg
		self._TxtMsg = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxtMsg', type=Max40KText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
	))

