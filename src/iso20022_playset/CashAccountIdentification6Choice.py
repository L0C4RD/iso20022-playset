import base_types
import IBAN2007Identifier
import RestrictedFINX2Max34Text

class CashAccountIdentification6Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_IBAN"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='Prtry', type=RestrictedFINX2Max34Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
	))

