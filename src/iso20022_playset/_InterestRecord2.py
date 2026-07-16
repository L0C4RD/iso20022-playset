# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CreditDebitCode
from . import DateTimePeriod1
from . import InterestType1Choice
from . import Max35Text
from . import Rate4
from . import TaxCharges2

class InterestRecord2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbtInd", "_FrToDt", "_Rate", "_Rsn", "_Tax", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if value is not None else base_types.UninitialisedField(self, 'FrToDt', DateTimePeriod1, False)

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = base_types.UninitialisedField(self, 'FrToDt', DateTimePeriod1, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', Rate4, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', Rate4, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max35Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max35Text, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', TaxCharges2, False)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', TaxCharges2, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', InterestType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', InterestType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToDt', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=Rate4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxCharges2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=InterestType1Choice, min=0, max=1, mutex_group=None, array=False),
	))