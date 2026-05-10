import base_types
import ImpliedCurrencyAndAmount
import ActiveCurrencyCode
import Max70Text

class ATMFeeComponent1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_FeeLabl", "_Amt"]
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

	@property
	def FeeLabl(self):
		return self._FeeLabl

	@FeeLabl.setter
	def FeeLabl(self, value):
		self._FeeLabl = value if type(value) != auto else self.make_default("FeeLabl")

	@FeeLabl.deleter
	def FeeLabl(self):
		del self._FeeLabl
		self._FeeLabl = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FeeLabl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

