# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EquityInstrumentReportingClassification1Code
from . import ISINOct2015Identifier
from . import MICIdentifier
from . import MarketDetail2
from . import Max350Text
from . import Max35Text
from . import Period4Choice
from . import StatisticsTransparency3
from . import TransparencyMethodology2Code
from . import TrueFalseIndicator

class TransparencyDataReport22(base_types._BaseFieldType):

	__slots__ = ["_ApplPrd", "_FinInstrmClssfctn", "_FullNm", "_Id", "_Lqdty", "_Mthdlgy", "_RlvntMkt", "_RptgPrd", "_Sttstcs", "_TechRcrdId", "_TradgVn"]
	@property
	def ApplPrd(self):
		return self._ApplPrd

	@ApplPrd.setter
	def ApplPrd(self, value):
		self._ApplPrd = value if value is not None else base_types.UninitialisedField(self, 'ApplPrd', Period4Choice, False)

	@ApplPrd.deleter
	def ApplPrd(self):
		del self._ApplPrd
		self._ApplPrd = base_types.UninitialisedField(self, 'ApplPrd', Period4Choice, False)

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmClssfctn', EquityInstrumentReportingClassification1Code, False)

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = base_types.UninitialisedField(self, 'FinInstrmClssfctn', EquityInstrumentReportingClassification1Code, False)

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if value is not None else base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def Lqdty(self):
		return self._Lqdty

	@Lqdty.setter
	def Lqdty(self, value):
		self._Lqdty = value if value is not None else base_types.UninitialisedField(self, 'Lqdty', TrueFalseIndicator, False)

	@Lqdty.deleter
	def Lqdty(self):
		del self._Lqdty
		self._Lqdty = base_types.UninitialisedField(self, 'Lqdty', TrueFalseIndicator, False)

	@property
	def Mthdlgy(self):
		return self._Mthdlgy

	@Mthdlgy.setter
	def Mthdlgy(self, value):
		self._Mthdlgy = value if value is not None else base_types.UninitialisedField(self, 'Mthdlgy', TransparencyMethodology2Code, False)

	@Mthdlgy.deleter
	def Mthdlgy(self):
		del self._Mthdlgy
		self._Mthdlgy = base_types.UninitialisedField(self, 'Mthdlgy', TransparencyMethodology2Code, False)

	@property
	def RlvntMkt(self):
		return self._RlvntMkt

	@RlvntMkt.setter
	def RlvntMkt(self, value):
		self._RlvntMkt = value if value is not None else base_types.UninitialisedField(self, 'RlvntMkt', MarketDetail2, False)

	@RlvntMkt.deleter
	def RlvntMkt(self):
		del self._RlvntMkt
		self._RlvntMkt = base_types.UninitialisedField(self, 'RlvntMkt', MarketDetail2, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@property
	def Sttstcs(self):
		return self._Sttstcs

	@Sttstcs.setter
	def Sttstcs(self, value):
		self._Sttstcs = value if value is not None else base_types.UninitialisedField(self, 'Sttstcs', StatisticsTransparency3, False)

	@Sttstcs.deleter
	def Sttstcs(self):
		del self._Sttstcs
		self._Sttstcs = base_types.UninitialisedField(self, 'Sttstcs', StatisticsTransparency3, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApplPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=EquityInstrumentReportingClassification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lqdty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mthdlgy', type=TransparencyMethodology2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlvntMkt', type=MarketDetail2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttstcs', type=StatisticsTransparency3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))