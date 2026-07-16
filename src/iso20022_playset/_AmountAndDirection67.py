# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitCode
from . import RestrictedFINActiveCurrencyAndAmount
from . import RestrictedFINActiveOrHistoricCurrencyAndAmount

class AmountAndDirection67(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbtInd", "_OrgnlCcyAndOrdrdAmt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveCurrencyAndAmount, False)

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
	def OrgnlCcyAndOrdrdAmt(self):
		return self._OrgnlCcyAndOrdrdAmt

	@OrgnlCcyAndOrdrdAmt.setter
	def OrgnlCcyAndOrdrdAmt(self, value):
		self._OrgnlCcyAndOrdrdAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCcyAndOrdrdAmt', RestrictedFINActiveOrHistoricCurrencyAndAmount, False)

	@OrgnlCcyAndOrdrdAmt.deleter
	def OrgnlCcyAndOrdrdAmt(self):
		del self._OrgnlCcyAndOrdrdAmt
		self._OrgnlCcyAndOrdrdAmt = base_types.UninitialisedField(self, 'OrgnlCcyAndOrdrdAmt', RestrictedFINActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCcyAndOrdrdAmt', type=RestrictedFINActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))