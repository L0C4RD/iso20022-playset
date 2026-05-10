from . import base_types
import DecimalNumber
import ActiveOrHistoricCurrencyAndAmount

class TonsOrCurrency2Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Nb"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

