# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import EUCapitalGain2Code
from . import EUDividendStatus1Code
from . import Extended350Code
from . import PercentageRate

class TaxCalculationInformation4(base_types._BaseFieldType):

	__slots__ = ["_EUCptlGn", "_EUDvddSts", "_PctgGrdfthdDebt", "_PctgOfDebtClm", "_TaxblIncmPerDvdd", "_XtndedEUCptlGn", "_XtndedEUDvddSts"]
	@property
	def EUCptlGn(self):
		return self._EUCptlGn

	@EUCptlGn.setter
	def EUCptlGn(self, value):
		self._EUCptlGn = value if value is not None else base_types.UninitialisedField(self, 'EUCptlGn', EUCapitalGain2Code, False)

	@EUCptlGn.deleter
	def EUCptlGn(self):
		del self._EUCptlGn
		self._EUCptlGn = base_types.UninitialisedField(self, 'EUCptlGn', EUCapitalGain2Code, False)

	@property
	def EUDvddSts(self):
		return self._EUDvddSts

	@EUDvddSts.setter
	def EUDvddSts(self, value):
		self._EUDvddSts = value if value is not None else base_types.UninitialisedField(self, 'EUDvddSts', EUDividendStatus1Code, False)

	@EUDvddSts.deleter
	def EUDvddSts(self):
		del self._EUDvddSts
		self._EUDvddSts = base_types.UninitialisedField(self, 'EUDvddSts', EUDividendStatus1Code, False)

	@property
	def PctgGrdfthdDebt(self):
		return self._PctgGrdfthdDebt

	@PctgGrdfthdDebt.setter
	def PctgGrdfthdDebt(self, value):
		self._PctgGrdfthdDebt = value if value is not None else base_types.UninitialisedField(self, 'PctgGrdfthdDebt', PercentageRate, False)

	@PctgGrdfthdDebt.deleter
	def PctgGrdfthdDebt(self):
		del self._PctgGrdfthdDebt
		self._PctgGrdfthdDebt = base_types.UninitialisedField(self, 'PctgGrdfthdDebt', PercentageRate, False)

	@property
	def PctgOfDebtClm(self):
		return self._PctgOfDebtClm

	@PctgOfDebtClm.setter
	def PctgOfDebtClm(self, value):
		self._PctgOfDebtClm = value if value is not None else base_types.UninitialisedField(self, 'PctgOfDebtClm', PercentageRate, False)

	@PctgOfDebtClm.deleter
	def PctgOfDebtClm(self):
		del self._PctgOfDebtClm
		self._PctgOfDebtClm = base_types.UninitialisedField(self, 'PctgOfDebtClm', PercentageRate, False)

	@property
	def TaxblIncmPerDvdd(self):
		return self._TaxblIncmPerDvdd

	@TaxblIncmPerDvdd.setter
	def TaxblIncmPerDvdd(self, value):
		self._TaxblIncmPerDvdd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerDvdd', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@TaxblIncmPerDvdd.deleter
	def TaxblIncmPerDvdd(self):
		del self._TaxblIncmPerDvdd
		self._TaxblIncmPerDvdd = base_types.UninitialisedField(self, 'TaxblIncmPerDvdd', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def XtndedEUCptlGn(self):
		return self._XtndedEUCptlGn

	@XtndedEUCptlGn.setter
	def XtndedEUCptlGn(self, value):
		self._XtndedEUCptlGn = value if value is not None else base_types.UninitialisedField(self, 'XtndedEUCptlGn', Extended350Code, False)

	@XtndedEUCptlGn.deleter
	def XtndedEUCptlGn(self):
		del self._XtndedEUCptlGn
		self._XtndedEUCptlGn = base_types.UninitialisedField(self, 'XtndedEUCptlGn', Extended350Code, False)

	@property
	def XtndedEUDvddSts(self):
		return self._XtndedEUDvddSts

	@XtndedEUDvddSts.setter
	def XtndedEUDvddSts(self, value):
		self._XtndedEUDvddSts = value if value is not None else base_types.UninitialisedField(self, 'XtndedEUDvddSts', Extended350Code, False)

	@XtndedEUDvddSts.deleter
	def XtndedEUDvddSts(self):
		del self._XtndedEUDvddSts
		self._XtndedEUDvddSts = base_types.UninitialisedField(self, 'XtndedEUDvddSts', Extended350Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGain2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatus1Code, min=0, max=1, mutex_group=2, array=False),
		base_types.FieldEntry(name='PctgGrdfthdDebt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfDebtClm', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedEUCptlGn', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedEUDvddSts', type=Extended350Code, min=0, max=1, mutex_group=2, array=False),
	))