from . import base_types
from ._AmountAndDirection53 import AmountAndDirection53
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._PercentageRate import PercentageRate
from ._DecimalNumber import DecimalNumber

class SecuritiesTransactionPrice21Choice(base_types._BaseFieldType):

	__slots__ = ["_BsisPts", "_Pctg", "_NmnlVal", "_MntryVal", "_Yld"]
	@property
	def BsisPts(self):
		return self._BsisPts

	@BsisPts.setter
	def BsisPts(self, value):
		self._BsisPts = value if type(value) != base_types.auto else self.make_default("BsisPts")

	@BsisPts.deleter
	def BsisPts(self):
		del self._BsisPts
		self._BsisPts = None

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != base_types.auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	@property
	def NmnlVal(self):
		return self._NmnlVal

	@NmnlVal.setter
	def NmnlVal(self, value):
		self._NmnlVal = value if type(value) != base_types.auto else self.make_default("NmnlVal")

	@NmnlVal.deleter
	def NmnlVal(self):
		del self._NmnlVal
		self._NmnlVal = None

	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if type(value) != base_types.auto else self.make_default("MntryVal")

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = None

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if type(value) != base_types.auto else self.make_default("Yld")

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmnlVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

