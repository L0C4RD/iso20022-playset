from . import base_types
import Max2048Text
import ISO2ALanguageCode

class UpdatedURLlnformation6(base_types._BaseFieldType):

	__slots__ = ["_URLAdr", "_Lang"]
	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

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
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
	))

