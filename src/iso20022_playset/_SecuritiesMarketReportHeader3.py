from . import base_types
from ._TradingVenueIdentification1Choice import TradingVenueIdentification1Choice
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._Pagination1 import Pagination1
from ._Period11Choice import Period11Choice
from ._ISODateTime import ISODateTime
from ._Number import Number

class SecuritiesMarketReportHeader3(base_types._BaseFieldType):

	__slots__ = ["_RptgNtty", "_NbRcrds", "_SubmissnDtTm", "_ISIN", "_RptgPrd", "_MsgPgntn"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != base_types.auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def NbRcrds(self):
		return self._NbRcrds

	@NbRcrds.setter
	def NbRcrds(self, value):
		self._NbRcrds = value if type(value) != base_types.auto else self.make_default("NbRcrds")

	@NbRcrds.deleter
	def NbRcrds(self):
		del self._NbRcrds
		self._NbRcrds = None

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if type(value) != base_types.auto else self.make_default("RptgNtty")

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = None

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != base_types.auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if type(value) != base_types.auto else self.make_default("SubmissnDtTm")

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbRcrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=TradingVenueIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

