from . import base_types
from .GenericAccountIdentification1 import GenericAccountIdentification1
from .IBAN2007Identifier import IBAN2007Identifier

class AccountIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_IBAN", "_Othr"]
	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if type(value) != base_types.auto else self.make_default("IBAN")

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericAccountIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

