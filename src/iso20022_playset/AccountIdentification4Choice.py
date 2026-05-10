import base_types
import IBAN2007Identifier
import GenericAccountIdentification1

class AccountIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_IBAN"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if type(value) != auto else self.make_default("IBAN")

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=GenericAccountIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
	))

