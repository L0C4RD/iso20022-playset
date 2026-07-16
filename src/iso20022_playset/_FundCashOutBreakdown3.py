# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ActiveOrHistoricCurrencyAndAmount
from . import Charge26
from . import Commission21
from . import FinancialInstrumentQuantity1
from . import InvestmentFundTransactionOutType1Choice
from . import QuantityType1Choice
from . import YesNoIndicator

class FundCashOutBreakdown3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChrgDtls", "_ComssnDtls", "_InvstmtFndTxOutTp", "_NewAmtInd", "_OrgnlOrdrQtyTp", "_SttlmCcy", "_UnitsNb"]
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
	def ChrgDtls(self):
		return self._ChrgDtls

	@ChrgDtls.setter
	def ChrgDtls(self, value):
		self._ChrgDtls = value if value is not None else base_types.UninitialisedField(self, 'ChrgDtls', Charge26, True)

	@ChrgDtls.deleter
	def ChrgDtls(self):
		del self._ChrgDtls
		self._ChrgDtls = base_types.UninitialisedField(self, 'ChrgDtls', Charge26, True)

	@property
	def ComssnDtls(self):
		return self._ComssnDtls

	@ComssnDtls.setter
	def ComssnDtls(self, value):
		self._ComssnDtls = value if value is not None else base_types.UninitialisedField(self, 'ComssnDtls', Commission21, True)

	@ComssnDtls.deleter
	def ComssnDtls(self):
		del self._ComssnDtls
		self._ComssnDtls = base_types.UninitialisedField(self, 'ComssnDtls', Commission21, True)

	@property
	def InvstmtFndTxOutTp(self):
		return self._InvstmtFndTxOutTp

	@InvstmtFndTxOutTp.setter
	def InvstmtFndTxOutTp(self, value):
		self._InvstmtFndTxOutTp = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFndTxOutTp', InvestmentFundTransactionOutType1Choice, False)

	@InvstmtFndTxOutTp.deleter
	def InvstmtFndTxOutTp(self):
		del self._InvstmtFndTxOutTp
		self._InvstmtFndTxOutTp = base_types.UninitialisedField(self, 'InvstmtFndTxOutTp', InvestmentFundTransactionOutType1Choice, False)

	@property
	def NewAmtInd(self):
		return self._NewAmtInd

	@NewAmtInd.setter
	def NewAmtInd(self, value):
		self._NewAmtInd = value if value is not None else base_types.UninitialisedField(self, 'NewAmtInd', YesNoIndicator, False)

	@NewAmtInd.deleter
	def NewAmtInd(self):
		del self._NewAmtInd
		self._NewAmtInd = base_types.UninitialisedField(self, 'NewAmtInd', YesNoIndicator, False)

	@property
	def OrgnlOrdrQtyTp(self):
		return self._OrgnlOrdrQtyTp

	@OrgnlOrdrQtyTp.setter
	def OrgnlOrdrQtyTp(self, value):
		self._OrgnlOrdrQtyTp = value if value is not None else base_types.UninitialisedField(self, 'OrgnlOrdrQtyTp', QuantityType1Choice, False)

	@OrgnlOrdrQtyTp.deleter
	def OrgnlOrdrQtyTp(self):
		del self._OrgnlOrdrQtyTp
		self._OrgnlOrdrQtyTp = base_types.UninitialisedField(self, 'OrgnlOrdrQtyTp', QuantityType1Choice, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if value is not None else base_types.UninitialisedField(self, 'UnitsNb', FinancialInstrumentQuantity1, False)

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = base_types.UninitialisedField(self, 'UnitsNb', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgDtls', type=Charge26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComssnDtls', type=Commission21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtFndTxOutTp', type=InvestmentFundTransactionOutType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlOrdrQtyTp', type=QuantityType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))