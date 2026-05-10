from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .EUCapitalGain3Choice import EUCapitalGain3Choice
from .PercentageRate import PercentageRate
from .Tax32 import Tax32
from .EUDividendStatusType2Choice import EUDividendStatusType2Choice

class InformativeTax1(base_types._BaseFieldType):

	__slots__ = ["_EUDvddSts", "_PctgOfDebtClm", "_EUCptlGn", "_IndvTax", "_TaxblIncmPerDvdd"]
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
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if type(value) != base_types.auto else self.make_default("IndvTax")

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = None

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
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatusType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfDebtClm', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGain3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTax', type=Tax32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

