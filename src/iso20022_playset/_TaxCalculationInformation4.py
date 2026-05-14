# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from ._EUCapitalGain2Code import EUCapitalGain2Code
from ._EUDividendStatus1Code import EUDividendStatus1Code
from ._Extended350Code import Extended350Code
from ._PercentageRate import PercentageRate

class TaxCalculationInformation4(base_types._BaseFieldType):

	__slots__ = ["_EUCptlGn", "_EUDvddSts", "_PctgGrdfthdDebt", "_PctgOfDebtClm", "_TaxblIncmPerDvdd", "_XtndedEUCptlGn", "_XtndedEUDvddSts"]
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

	@property
	def XtndedEUCptlGn(self):
		return self._XtndedEUCptlGn

	@XtndedEUCptlGn.setter
	def XtndedEUCptlGn(self, value):
		self._XtndedEUCptlGn = value if type(value) != base_types.auto else self.make_default("XtndedEUCptlGn")

	@XtndedEUCptlGn.deleter
	def XtndedEUCptlGn(self):
		del self._XtndedEUCptlGn
		self._XtndedEUCptlGn = None

	@property
	def XtndedEUDvddSts(self):
		return self._XtndedEUDvddSts

	@XtndedEUDvddSts.setter
	def XtndedEUDvddSts(self, value):
		self._XtndedEUDvddSts = value if type(value) != base_types.auto else self.make_default("XtndedEUDvddSts")

	@XtndedEUDvddSts.deleter
	def XtndedEUDvddSts(self):
		del self._XtndedEUDvddSts
		self._XtndedEUDvddSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGain2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatus1Code, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='PctgGrdfthdDebt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfDebtClm', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedEUCptlGn', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedEUDvddSts', type=Extended350Code, min=0, max=1, mutex_group=2, array=False),
	))