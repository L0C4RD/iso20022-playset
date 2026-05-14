from . import base_types
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from ._EUCapitalGainType4Choice import EUCapitalGainType4Choice
from ._EUDividendStatusType3Choice import EUDividendStatusType3Choice
from ._PercentageRate import PercentageRate

class TaxCalculationInformation12(base_types._BaseFieldType):

	__slots__ = ["_EUCptlGn", "_EUDvddSts", "_PctgGrdfthdDebt", "_PctgOfDebtClm", "_TaxblIncmPerDvdd"]
	@property
	def EUCptlGn(self):
		return self._EUCptlGn

	@EUCptlGn.setter
	def EUCptlGn(self, value):
		self._EUCptlGn = value if type(value) != base_types.auto else self.make_default("EUCptlGn")

	@EUCptlGn.deleter
	def EUCptlGn(self):
		del self._EUCptlGn
		self._EUCptlGn = None

	@property
	def EUDvddSts(self):
		return self._EUDvddSts

	@EUDvddSts.setter
	def EUDvddSts(self, value):
		self._EUDvddSts = value if type(value) != base_types.auto else self.make_default("EUDvddSts")

	@EUDvddSts.deleter
	def EUDvddSts(self):
		del self._EUDvddSts
		self._EUDvddSts = None

	@property
	def PctgGrdfthdDebt(self):
		return self._PctgGrdfthdDebt

	@PctgGrdfthdDebt.setter
	def PctgGrdfthdDebt(self, value):
		self._PctgGrdfthdDebt = value if type(value) != base_types.auto else self.make_default("PctgGrdfthdDebt")

	@PctgGrdfthdDebt.deleter
	def PctgGrdfthdDebt(self):
		del self._PctgGrdfthdDebt
		self._PctgGrdfthdDebt = None

	@property
	def PctgOfDebtClm(self):
		return self._PctgOfDebtClm

	@PctgOfDebtClm.setter
	def PctgOfDebtClm(self, value):
		self._PctgOfDebtClm = value if type(value) != base_types.auto else self.make_default("PctgOfDebtClm")

	@PctgOfDebtClm.deleter
	def PctgOfDebtClm(self):
		del self._PctgOfDebtClm
		self._PctgOfDebtClm = None

	@property
	def TaxblIncmPerDvdd(self):
		return self._TaxblIncmPerDvdd

	@TaxblIncmPerDvdd.setter
	def TaxblIncmPerDvdd(self, value):
		self._TaxblIncmPerDvdd = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerDvdd")

	@TaxblIncmPerDvdd.deleter
	def TaxblIncmPerDvdd(self):
		del self._TaxblIncmPerDvdd
		self._TaxblIncmPerDvdd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGainType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatusType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgGrdfthdDebt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfDebtClm', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))

