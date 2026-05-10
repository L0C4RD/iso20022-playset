from . import base_types
from ._QuantityType1Choice import QuantityType1Choice
from ._Charge26 import Charge26
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._InvestmentFundTransactionInType1Choice import InvestmentFundTransactionInType1Choice
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._Commission21 import Commission21
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._YesNoIndicator import YesNoIndicator

class FundCashInBreakdown3(base_types._BaseFieldType):

	__slots__ = ["_InvstmtFndTxInTp", "_ComssnDtls", "_NewAmtInd", "_ChrgDtls", "_SttlmCcy", "_Amt", "_OrgnlOrdrQtyTp", "_UnitsNb"]
	@property
	def InvstmtFndTxInTp(self):
		return self._InvstmtFndTxInTp

	@InvstmtFndTxInTp.setter
	def InvstmtFndTxInTp(self, value):
		self._InvstmtFndTxInTp = value if type(value) != base_types.auto else self.make_default("InvstmtFndTxInTp")

	@InvstmtFndTxInTp.deleter
	def InvstmtFndTxInTp(self):
		del self._InvstmtFndTxInTp
		self._InvstmtFndTxInTp = None

	@property
	def ComssnDtls(self):
		return self._ComssnDtls

	@ComssnDtls.setter
	def ComssnDtls(self, value):
		self._ComssnDtls = value if type(value) != base_types.auto else self.make_default("ComssnDtls")

	@ComssnDtls.deleter
	def ComssnDtls(self):
		del self._ComssnDtls
		self._ComssnDtls = None

	@property
	def NewAmtInd(self):
		return self._NewAmtInd

	@NewAmtInd.setter
	def NewAmtInd(self, value):
		self._NewAmtInd = value if type(value) != base_types.auto else self.make_default("NewAmtInd")

	@NewAmtInd.deleter
	def NewAmtInd(self):
		del self._NewAmtInd
		self._NewAmtInd = None

	@property
	def ChrgDtls(self):
		return self._ChrgDtls

	@ChrgDtls.setter
	def ChrgDtls(self, value):
		self._ChrgDtls = value if type(value) != base_types.auto else self.make_default("ChrgDtls")

	@ChrgDtls.deleter
	def ChrgDtls(self):
		del self._ChrgDtls
		self._ChrgDtls = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

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
	def OrgnlOrdrQtyTp(self):
		return self._OrgnlOrdrQtyTp

	@OrgnlOrdrQtyTp.setter
	def OrgnlOrdrQtyTp(self, value):
		self._OrgnlOrdrQtyTp = value if type(value) != base_types.auto else self.make_default("OrgnlOrdrQtyTp")

	@OrgnlOrdrQtyTp.deleter
	def OrgnlOrdrQtyTp(self):
		del self._OrgnlOrdrQtyTp
		self._OrgnlOrdrQtyTp = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != base_types.auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtFndTxInTp', type=InvestmentFundTransactionInType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnDtls', type=Commission21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgDtls', type=Charge26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlOrdrQtyTp', type=QuantityType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))

