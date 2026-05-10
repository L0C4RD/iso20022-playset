import base_types
import MarketDetail2
import StatisticsTransparency3
import TransparencyMethodology2Code
import EquityInstrumentReportingClassification1Code
import TrueFalseIndicator
import Max35Text
import Max350Text
import Period4Choice
import MICIdentifier
import ISINOct2015Identifier

class TransparencyDataReport17(base_types._BaseFieldType):

	__slots__ = ["_TradgVn", "_Id", "_RptgPrd", "_Lqdty", "_FinInstrmClssfctn", "_RlvntMkt", "_Mthdlgy", "_FullNm", "_TechRcrdId", "_Sttstcs"]
	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
	def Lqdty(self):
		return self._Lqdty

	@Lqdty.setter
	def Lqdty(self, value):
		self._Lqdty = value if type(value) != auto else self.make_default("Lqdty")

	@Lqdty.deleter
	def Lqdty(self):
		del self._Lqdty
		self._Lqdty = None

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if type(value) != auto else self.make_default("FinInstrmClssfctn")

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = None

	@property
	def RlvntMkt(self):
		return self._RlvntMkt

	@RlvntMkt.setter
	def RlvntMkt(self, value):
		self._RlvntMkt = value if type(value) != auto else self.make_default("RlvntMkt")

	@RlvntMkt.deleter
	def RlvntMkt(self):
		del self._RlvntMkt
		self._RlvntMkt = None

	@property
	def Mthdlgy(self):
		return self._Mthdlgy

	@Mthdlgy.setter
	def Mthdlgy(self, value):
		self._Mthdlgy = value if type(value) != auto else self.make_default("Mthdlgy")

	@Mthdlgy.deleter
	def Mthdlgy(self):
		del self._Mthdlgy
		self._Mthdlgy = None

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if type(value) != auto else self.make_default("FullNm")

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def Sttstcs(self):
		return self._Sttstcs

	@Sttstcs.setter
	def Sttstcs(self, value):
		self._Sttstcs = value if type(value) != auto else self.make_default("Sttstcs")

	@Sttstcs.deleter
	def Sttstcs(self):
		del self._Sttstcs
		self._Sttstcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lqdty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=EquityInstrumentReportingClassification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlvntMkt', type=MarketDetail2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mthdlgy', type=TransparencyMethodology2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttstcs', type=StatisticsTransparency3, min=0, max=1, mutex_group=None, array=False),
	))

