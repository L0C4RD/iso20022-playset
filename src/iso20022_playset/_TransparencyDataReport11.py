# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveCurrencyAndAmount
from . import DecimalNumberFraction5
from . import EquityInstrumentReportingClassification1Code
from . import ISINOct2015Identifier
from . import ISODate
from . import MICIdentifier
from . import Max350Text
from . import Max35Text

class TransparencyDataReport11(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmClssfctn", "_FullNm", "_HldgsExcdgTtlVtngRghtThrshld", "_Id", "_InstrmPric", "_IssncSz", "_NbOutsdngInstrms", "_RptgDt", "_TechRcrdId", "_TradgVn"]
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
	def HldgsExcdgTtlVtngRghtThrshld(self):
		return self._HldgsExcdgTtlVtngRghtThrshld

	@HldgsExcdgTtlVtngRghtThrshld.setter
	def HldgsExcdgTtlVtngRghtThrshld(self, value):
		self._HldgsExcdgTtlVtngRghtThrshld = value if value is not None else base_types.UninitialisedField(self, 'HldgsExcdgTtlVtngRghtThrshld', DecimalNumberFraction5, False)

	@HldgsExcdgTtlVtngRghtThrshld.deleter
	def HldgsExcdgTtlVtngRghtThrshld(self):
		del self._HldgsExcdgTtlVtngRghtThrshld
		self._HldgsExcdgTtlVtngRghtThrshld = base_types.UninitialisedField(self, 'HldgsExcdgTtlVtngRghtThrshld', DecimalNumberFraction5, False)

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
	def InstrmPric(self):
		return self._InstrmPric

	@InstrmPric.setter
	def InstrmPric(self, value):
		self._InstrmPric = value if value is not None else base_types.UninitialisedField(self, 'InstrmPric', ActiveCurrencyAnd13DecimalAmount, False)

	@InstrmPric.deleter
	def InstrmPric(self):
		del self._InstrmPric
		self._InstrmPric = base_types.UninitialisedField(self, 'InstrmPric', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def IssncSz(self):
		return self._IssncSz

	@IssncSz.setter
	def IssncSz(self, value):
		self._IssncSz = value if value is not None else base_types.UninitialisedField(self, 'IssncSz', ActiveCurrencyAndAmount, False)

	@IssncSz.deleter
	def IssncSz(self):
		del self._IssncSz
		self._IssncSz = base_types.UninitialisedField(self, 'IssncSz', ActiveCurrencyAndAmount, False)

	@property
	def NbOutsdngInstrms(self):
		return self._NbOutsdngInstrms

	@NbOutsdngInstrms.setter
	def NbOutsdngInstrms(self, value):
		self._NbOutsdngInstrms = value if value is not None else base_types.UninitialisedField(self, 'NbOutsdngInstrms', DecimalNumberFraction5, False)

	@NbOutsdngInstrms.deleter
	def NbOutsdngInstrms(self):
		del self._NbOutsdngInstrms
		self._NbOutsdngInstrms = base_types.UninitialisedField(self, 'NbOutsdngInstrms', DecimalNumberFraction5, False)

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if value is not None else base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

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
		base_types.FieldEntry(name='FinInstrmClssfctn', type=EquityInstrumentReportingClassification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsExcdgTtlVtngRghtThrshld', type=DecimalNumberFraction5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmPric', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncSz', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOutsdngInstrms', type=DecimalNumberFraction5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))