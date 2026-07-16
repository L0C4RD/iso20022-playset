# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import EUCapitalGain3Choice
from . import EUDividendStatusType2Choice
from . import PercentageRate
from . import Tax40

class InformativeTax2(base_types._BaseFieldType):

	__slots__ = ["_EUCptlGn", "_EUDvddSts", "_IndvTax", "_PctgOfDebtClm", "_TaxblIncmPerDvdd"]
	@property
	def EUCptlGn(self):
		return self._EUCptlGn

	@EUCptlGn.setter
	def EUCptlGn(self, value):
		self._EUCptlGn = value if value is not None else base_types.UninitialisedField(self, 'EUCptlGn', EUCapitalGain3Choice, False)

	@EUCptlGn.deleter
	def EUCptlGn(self):
		del self._EUCptlGn
		self._EUCptlGn = base_types.UninitialisedField(self, 'EUCptlGn', EUCapitalGain3Choice, False)

	@property
	def EUDvddSts(self):
		return self._EUDvddSts

	@EUDvddSts.setter
	def EUDvddSts(self, value):
		self._EUDvddSts = value if value is not None else base_types.UninitialisedField(self, 'EUDvddSts', EUDividendStatusType2Choice, False)

	@EUDvddSts.deleter
	def EUDvddSts(self):
		del self._EUDvddSts
		self._EUDvddSts = base_types.UninitialisedField(self, 'EUDvddSts', EUDividendStatusType2Choice, False)

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if value is not None else base_types.UninitialisedField(self, 'IndvTax', Tax40, True)

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = base_types.UninitialisedField(self, 'IndvTax', Tax40, True)

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
		self._TaxblIncmPerDvdd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerDvdd', ActiveCurrencyAndAmount, False)

	@TaxblIncmPerDvdd.deleter
	def TaxblIncmPerDvdd(self):
		del self._TaxblIncmPerDvdd
		self._TaxblIncmPerDvdd = base_types.UninitialisedField(self, 'TaxblIncmPerDvdd', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGain3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUDvddSts', type=EUDividendStatusType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTax', type=Tax40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PctgOfDebtClm', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvdd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))