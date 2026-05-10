from . import base_types
from ._ISODate import ISODate
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._Max35Text import Max35Text
from ._NumberAndVolume2 import NumberAndVolume2
from ._MICIdentifier import MICIdentifier

class TransparencyDataReport13(base_types._BaseFieldType):

	__slots__ = ["_Sspnsn", "_RptgDt", "_TxsExctdExclgPreTradWvr", "_Id", "_TxsExctd", "_TradgVn", "_TechRcrdId", "_TxsExctdExclgPstTradLrgInScaleWvr"]
	@property
	def Sspnsn(self):
		return self._Sspnsn

	@Sspnsn.setter
	def Sspnsn(self, value):
		self._Sspnsn = value if type(value) != base_types.auto else self.make_default("Sspnsn")

	@Sspnsn.deleter
	def Sspnsn(self):
		del self._Sspnsn
		self._Sspnsn = None

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if type(value) != base_types.auto else self.make_default("RptgDt")

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = None

	@property
	def TxsExctdExclgPreTradWvr(self):
		return self._TxsExctdExclgPreTradWvr

	@TxsExctdExclgPreTradWvr.setter
	def TxsExctdExclgPreTradWvr(self, value):
		self._TxsExctdExclgPreTradWvr = value if type(value) != base_types.auto else self.make_default("TxsExctdExclgPreTradWvr")

	@TxsExctdExclgPreTradWvr.deleter
	def TxsExctdExclgPreTradWvr(self):
		del self._TxsExctdExclgPreTradWvr
		self._TxsExctdExclgPreTradWvr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def TxsExctd(self):
		return self._TxsExctd

	@TxsExctd.setter
	def TxsExctd(self, value):
		self._TxsExctd = value if type(value) != base_types.auto else self.make_default("TxsExctd")

	@TxsExctd.deleter
	def TxsExctd(self):
		del self._TxsExctd
		self._TxsExctd = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != base_types.auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def TxsExctdExclgPstTradLrgInScaleWvr(self):
		return self._TxsExctdExclgPstTradLrgInScaleWvr

	@TxsExctdExclgPstTradLrgInScaleWvr.setter
	def TxsExctdExclgPstTradLrgInScaleWvr(self, value):
		self._TxsExctdExclgPstTradLrgInScaleWvr = value if type(value) != base_types.auto else self.make_default("TxsExctdExclgPstTradLrgInScaleWvr")

	@TxsExctdExclgPstTradLrgInScaleWvr.deleter
	def TxsExctdExclgPstTradLrgInScaleWvr(self):
		del self._TxsExctdExclgPstTradLrgInScaleWvr
		self._TxsExctdExclgPstTradLrgInScaleWvr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sspnsn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsExctdExclgPreTradWvr', type=NumberAndVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsExctd', type=NumberAndVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsExctdExclgPstTradLrgInScaleWvr', type=NumberAndVolume2, min=1, max=1, mutex_group=None, array=False),
	))

