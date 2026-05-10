from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .FundBalance1 import FundBalance1
from .ISODate import ISODate
from .FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from .FlowDirectionType1Code import FlowDirectionType1Code

class NetCashForecast4(base_types._BaseFieldType):

	__slots__ = ["_AddtlBal", "_NetUnitsNb", "_NetAmt", "_CshSttlmDt", "_FlowDrctn"]
	@property
	def AddtlBal(self):
		return self._AddtlBal

	@AddtlBal.setter
	def AddtlBal(self, value):
		self._AddtlBal = value if type(value) != auto else self.make_default("AddtlBal")

	@AddtlBal.deleter
	def AddtlBal(self):
		del self._AddtlBal
		self._AddtlBal = None

	@property
	def NetUnitsNb(self):
		return self._NetUnitsNb

	@NetUnitsNb.setter
	def NetUnitsNb(self, value):
		self._NetUnitsNb = value if type(value) != auto else self.make_default("NetUnitsNb")

	@NetUnitsNb.deleter
	def NetUnitsNb(self):
		del self._NetUnitsNb
		self._NetUnitsNb = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if type(value) != auto else self.make_default("CshSttlmDt")

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = None

	@property
	def FlowDrctn(self):
		return self._FlowDrctn

	@FlowDrctn.setter
	def FlowDrctn(self, value):
		self._FlowDrctn = value if type(value) != auto else self.make_default("FlowDrctn")

	@FlowDrctn.deleter
	def FlowDrctn(self):
		del self._FlowDrctn
		self._FlowDrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlBal', type=FundBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlowDrctn', type=FlowDirectionType1Code, min=1, max=1, mutex_group=None, array=False),
	))

