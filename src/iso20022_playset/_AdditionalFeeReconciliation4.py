from . import base_types
from ._ISO8583FeeTypeCode import ISO8583FeeTypeCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Number import Number
from ._ReconciliationImpact1Code import ReconciliationImpact1Code

class AdditionalFeeReconciliation4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cnt", "_Impct", "_Tp"]
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

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if type(value) != base_types.auto else self.make_default("Cnt")

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = None

	@property
	def Impct(self):
		return self._Impct

	@Impct.setter
	def Impct(self, value):
		self._Impct = value if type(value) != base_types.auto else self.make_default("Impct")

	@Impct.deleter
	def Impct(self):
		del self._Impct
		self._Impct = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Impct', type=ReconciliationImpact1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ISO8583FeeTypeCode, min=1, max=1, mutex_group=None, array=False),
	))

