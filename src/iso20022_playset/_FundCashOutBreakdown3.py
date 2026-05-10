from . import base_types
from ._QuantityType1Choice import QuantityType1Choice
from ._Charge26 import Charge26
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._InvestmentFundTransactionOutType1Choice import InvestmentFundTransactionOutType1Choice
from ._Commission21 import Commission21
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._YesNoIndicator import YesNoIndicator

class FundCashOutBreakdown3(base_types._BaseFieldType):

	__slots__ = ["_ComssnDtls", "_NewAmtInd", "_ChrgDtls", "_SttlmCcy", "_Amt", "_OrgnlOrdrQtyTp", "_UnitsNb", "_InvstmtFndTxOutTp"]
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

	@property
	def InvstmtFndTxOutTp(self):
		return self._InvstmtFndTxOutTp

	@InvstmtFndTxOutTp.setter
	def InvstmtFndTxOutTp(self, value):
		self._InvstmtFndTxOutTp = value if type(value) != base_types.auto else self.make_default("InvstmtFndTxOutTp")

	@InvstmtFndTxOutTp.deleter
	def InvstmtFndTxOutTp(self):
		del self._InvstmtFndTxOutTp
		self._InvstmtFndTxOutTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComssnDtls', type=Commission21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgDtls', type=Charge26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlOrdrQtyTp', type=QuantityType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndTxOutTp', type=InvestmentFundTransactionOutType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

