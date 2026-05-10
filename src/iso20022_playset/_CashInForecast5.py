from . import base_types
from ._ISODate import ISODate
from ._FundCashInBreakdown3 import FundCashInBreakdown3
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._FundBalance1 import FundBalance1
from ._YesNoIndicator import YesNoIndicator
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class CashInForecast5(base_types._BaseFieldType):

	__slots__ = ["_SubTtlAmt", "_XcptnlCshFlowInd", "_CshInBrkdwnDtls", "_AddtlBal", "_CshSttlmDt", "_SubTtlUnitsNb"]
	@property
	def AddtlBal(self):
		return self._AddtlBal

	@AddtlBal.setter
	def AddtlBal(self, value):
		self._AddtlBal = value if type(value) != base_types.auto else self.make_default("AddtlBal")

	@AddtlBal.deleter
	def AddtlBal(self):
		del self._AddtlBal
		self._AddtlBal = None

	@property
	def CshInBrkdwnDtls(self):
		return self._CshInBrkdwnDtls

	@CshInBrkdwnDtls.setter
	def CshInBrkdwnDtls(self, value):
		self._CshInBrkdwnDtls = value if type(value) != base_types.auto else self.make_default("CshInBrkdwnDtls")

	@CshInBrkdwnDtls.deleter
	def CshInBrkdwnDtls(self):
		del self._CshInBrkdwnDtls
		self._CshInBrkdwnDtls = None

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if type(value) != base_types.auto else self.make_default("CshSttlmDt")

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = None

	@property
	def SubTtlAmt(self):
		return self._SubTtlAmt

	@SubTtlAmt.setter
	def SubTtlAmt(self, value):
		self._SubTtlAmt = value if type(value) != base_types.auto else self.make_default("SubTtlAmt")

	@SubTtlAmt.deleter
	def SubTtlAmt(self):
		del self._SubTtlAmt
		self._SubTtlAmt = None

	@property
	def SubTtlUnitsNb(self):
		return self._SubTtlUnitsNb

	@SubTtlUnitsNb.setter
	def SubTtlUnitsNb(self, value):
		self._SubTtlUnitsNb = value if type(value) != base_types.auto else self.make_default("SubTtlUnitsNb")

	@SubTtlUnitsNb.deleter
	def SubTtlUnitsNb(self):
		del self._SubTtlUnitsNb
		self._SubTtlUnitsNb = None

	@property
	def XcptnlCshFlowInd(self):
		return self._XcptnlCshFlowInd

	@XcptnlCshFlowInd.setter
	def XcptnlCshFlowInd(self, value):
		self._XcptnlCshFlowInd = value if type(value) != base_types.auto else self.make_default("XcptnlCshFlowInd")

	@XcptnlCshFlowInd.deleter
	def XcptnlCshFlowInd(self):
		del self._XcptnlCshFlowInd
		self._XcptnlCshFlowInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlBal', type=FundBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInBrkdwnDtls', type=FundCashInBreakdown3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTtlAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcptnlCshFlowInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

