from . import base_types
import PlusOrMinusIndicator
import ActiveCurrencyCode
import ImpliedCurrencyAndAmount

class AmountAndDirection93(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Sgn", "_Ccy"]
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
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

