from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._BaseOneRate import BaseOneRate
from ._ISODate import ISODate
from ._Max35Text import Max35Text

class FixingConditions1(base_types._BaseFieldType):

	__slots__ = ["_CmonRef", "_OrgtrRef", "_RltdRef", "_TradDt", "_TradgSdBuyAmt", "_TradgSdSellAmt", "_XchgRate"]
	@property
	def CmonRef(self):
		return self._CmonRef

	@CmonRef.setter
	def CmonRef(self, value):
		self._CmonRef = value if type(value) != base_types.auto else self.make_default("CmonRef")

	@CmonRef.deleter
	def CmonRef(self):
		del self._CmonRef
		self._CmonRef = None

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if type(value) != base_types.auto else self.make_default("OrgtrRef")

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def TradgSdBuyAmt(self):
		return self._TradgSdBuyAmt

	@TradgSdBuyAmt.setter
	def TradgSdBuyAmt(self, value):
		self._TradgSdBuyAmt = value if type(value) != base_types.auto else self.make_default("TradgSdBuyAmt")

	@TradgSdBuyAmt.deleter
	def TradgSdBuyAmt(self):
		del self._TradgSdBuyAmt
		self._TradgSdBuyAmt = None

	@property
	def TradgSdSellAmt(self):
		return self._TradgSdSellAmt

	@TradgSdSellAmt.setter
	def TradgSdSellAmt(self, value):
		self._TradgSdSellAmt = value if type(value) != base_types.auto else self.make_default("TradgSdSellAmt")

	@TradgSdSellAmt.deleter
	def TradgSdSellAmt(self):
		del self._TradgSdSellAmt
		self._TradgSdSellAmt = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdBuyAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdSellAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))

