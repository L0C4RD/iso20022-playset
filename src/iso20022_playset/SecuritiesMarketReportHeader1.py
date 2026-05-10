import base_types
import Period4Choice
import ISODateTime
import TradingVenueIdentification1Choice

class SecuritiesMarketReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_SubmissnDtTm", "_RptgPrd", "_RptgNtty"]
	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if type(value) != auto else self.make_default("SubmissnDtTm")

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = None

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if type(value) != auto else self.make_default("RptgNtty")

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=TradingVenueIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
	))

