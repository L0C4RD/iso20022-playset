from . import base_types
from ._PlusOrMinusIndicator import PlusOrMinusIndicator
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class AmountAndDirection102(base_types._BaseFieldType):

	__slots__ = ["_Sgn", "_Amt"]
	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != base_types.auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

