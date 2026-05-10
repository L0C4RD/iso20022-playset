from . import base_types
import RestrictedFINActiveCurrencyAnd13DecimalAmount

class AmountToAmountRatio3(base_types._BaseFieldType):

	__slots__ = ["_Amt2", "_Amt1"]
	@property
	def Amt2(self):
		return self._Amt2

	@Amt2.setter
	def Amt2(self, value):
		self._Amt2 = value if type(value) != auto else self.make_default("Amt2")

	@Amt2.deleter
	def Amt2(self):
		del self._Amt2
		self._Amt2 = None

	@property
	def Amt1(self):
		return self._Amt1

	@Amt1.setter
	def Amt1(self, value):
		self._Amt1 = value if type(value) != auto else self.make_default("Amt1")

	@Amt1.deleter
	def Amt1(self):
		del self._Amt1
		self._Amt1 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt2', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt1', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))

