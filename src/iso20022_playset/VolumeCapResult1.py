from . import base_types
from .Max350Text import Max350Text
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .ISODate import ISODate
from .PercentageRate import PercentageRate
from .TradingUnderWaiversPercentage1 import TradingUnderWaiversPercentage1
from .ISINOct2015Identifier import ISINOct2015Identifier
from .Period4Choice import Period4Choice

class VolumeCapResult1(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_RptgPrd", "_TradgUdrWvrBrkdwn", "_LastUpdDt", "_TtlTradgVol", "_TradgUdrWvrPctg", "_Id"]
	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if type(value) != base_types.auto else self.make_default("Dsclmr")

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = None

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
	def TradgUdrWvrBrkdwn(self):
		return self._TradgUdrWvrBrkdwn

	@TradgUdrWvrBrkdwn.setter
	def TradgUdrWvrBrkdwn(self, value):
		self._TradgUdrWvrBrkdwn = value if type(value) != base_types.auto else self.make_default("TradgUdrWvrBrkdwn")

	@TradgUdrWvrBrkdwn.deleter
	def TradgUdrWvrBrkdwn(self):
		del self._TradgUdrWvrBrkdwn
		self._TradgUdrWvrBrkdwn = None

	@property
	def LastUpdDt(self):
		return self._LastUpdDt

	@LastUpdDt.setter
	def LastUpdDt(self, value):
		self._LastUpdDt = value if type(value) != base_types.auto else self.make_default("LastUpdDt")

	@LastUpdDt.deleter
	def LastUpdDt(self):
		del self._LastUpdDt
		self._LastUpdDt = None

	@property
	def TtlTradgVol(self):
		return self._TtlTradgVol

	@TtlTradgVol.setter
	def TtlTradgVol(self, value):
		self._TtlTradgVol = value if type(value) != base_types.auto else self.make_default("TtlTradgVol")

	@TtlTradgVol.deleter
	def TtlTradgVol(self):
		del self._TtlTradgVol
		self._TtlTradgVol = None

	@property
	def TradgUdrWvrPctg(self):
		return self._TradgUdrWvrPctg

	@TradgUdrWvrPctg.setter
	def TradgUdrWvrPctg(self, value):
		self._TradgUdrWvrPctg = value if type(value) != base_types.auto else self.make_default("TradgUdrWvrPctg")

	@TradgUdrWvrPctg.deleter
	def TradgUdrWvrPctg(self):
		del self._TradgUdrWvrPctg
		self._TradgUdrWvrPctg = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgUdrWvrBrkdwn', type=TradingUnderWaiversPercentage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LastUpdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTradgVol', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgUdrWvrPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

