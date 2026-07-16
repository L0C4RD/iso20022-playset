# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier
from . import ISODateTime
from . import Number
from . import Pagination1
from . import Period11Choice
from . import TradingVenueIdentification1Choice

class SecuritiesMarketReportHeader3(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_MsgPgntn", "_NbRcrds", "_RptgNtty", "_RptgPrd", "_SubmissnDtTm"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@property
	def NbRcrds(self):
		return self._NbRcrds

	@NbRcrds.setter
	def NbRcrds(self, value):
		self._NbRcrds = value if value is not None else base_types.UninitialisedField(self, 'NbRcrds', Number, False)

	@NbRcrds.deleter
	def NbRcrds(self):
		del self._NbRcrds
		self._NbRcrds = base_types.UninitialisedField(self, 'NbRcrds', Number, False)

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if value is not None else base_types.UninitialisedField(self, 'RptgNtty', TradingVenueIdentification1Choice, False)

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = base_types.UninitialisedField(self, 'RptgNtty', TradingVenueIdentification1Choice, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', Period11Choice, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', Period11Choice, False)

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if value is not None else base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbRcrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=TradingVenueIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))