import base_types
import DecimalNumberFraction5
import EquityInstrumentReportingClassification1Code
import Max35Text
import Max350Text
import MICIdentifier
import ActiveCurrencyAndAmount
import ISODate
import ISINOct2015Identifier
import ActiveCurrencyAnd13DecimalAmount

class TransparencyDataReport11(base_types._BaseFieldType):

	__slots__ = ["_TradgVn", "_Id", "_RptgDt", "_FullNm", "_IssncSz", "_InstrmPric", "_HldgsExcdgTtlVtngRghtThrshld", "_NbOutsdngInstrms", "_TechRcrdId", "_FinInstrmClssfctn"]
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
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if type(value) != auto else self.make_default("RptgDt")

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = None

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
	def IssncSz(self):
		return self._IssncSz

	@IssncSz.setter
	def IssncSz(self, value):
		self._IssncSz = value if type(value) != auto else self.make_default("IssncSz")

	@IssncSz.deleter
	def IssncSz(self):
		del self._IssncSz
		self._IssncSz = None

	@property
	def InstrmPric(self):
		return self._InstrmPric

	@InstrmPric.setter
	def InstrmPric(self, value):
		self._InstrmPric = value if type(value) != auto else self.make_default("InstrmPric")

	@InstrmPric.deleter
	def InstrmPric(self):
		del self._InstrmPric
		self._InstrmPric = None

	@property
	def HldgsExcdgTtlVtngRghtThrshld(self):
		return self._HldgsExcdgTtlVtngRghtThrshld

	@HldgsExcdgTtlVtngRghtThrshld.setter
	def HldgsExcdgTtlVtngRghtThrshld(self, value):
		self._HldgsExcdgTtlVtngRghtThrshld = value if type(value) != auto else self.make_default("HldgsExcdgTtlVtngRghtThrshld")

	@HldgsExcdgTtlVtngRghtThrshld.deleter
	def HldgsExcdgTtlVtngRghtThrshld(self):
		del self._HldgsExcdgTtlVtngRghtThrshld
		self._HldgsExcdgTtlVtngRghtThrshld = None

	@property
	def NbOutsdngInstrms(self):
		return self._NbOutsdngInstrms

	@NbOutsdngInstrms.setter
	def NbOutsdngInstrms(self, value):
		self._NbOutsdngInstrms = value if type(value) != auto else self.make_default("NbOutsdngInstrms")

	@NbOutsdngInstrms.deleter
	def NbOutsdngInstrms(self):
		del self._NbOutsdngInstrms
		self._NbOutsdngInstrms = None

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
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if type(value) != auto else self.make_default("FinInstrmClssfctn")

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncSz', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmPric', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsExcdgTtlVtngRghtThrshld', type=DecimalNumberFraction5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOutsdngInstrms', type=DecimalNumberFraction5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=EquityInstrumentReportingClassification1Code, min=1, max=1, mutex_group=None, array=False),
	))

