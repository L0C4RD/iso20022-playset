import base_types
import TonsOrCurrency2Choice
import Max350Text
import StatisticsTransparency2
import MICIdentifier
import Max35Text
import TrueFalseIndicator
import InstrumentOrSubClassIdentification2Choice
import Period4Choice

class TransparencyDataReport20(base_types._BaseFieldType):

	__slots__ = ["_TradgVn", "_TechRcrdId", "_PstTradInstrmSzSpcfcThrshld", "_FullNm", "_Lqdty", "_Sttstcs", "_PreTradLrgInScaleThrshld", "_PstTradLrgInScaleThrshld", "_PreTradInstrmSzSpcfcThrshld", "_Id", "_RptgPrd"]
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
	def PstTradInstrmSzSpcfcThrshld(self):
		return self._PstTradInstrmSzSpcfcThrshld

	@PstTradInstrmSzSpcfcThrshld.setter
	def PstTradInstrmSzSpcfcThrshld(self, value):
		self._PstTradInstrmSzSpcfcThrshld = value if type(value) != auto else self.make_default("PstTradInstrmSzSpcfcThrshld")

	@PstTradInstrmSzSpcfcThrshld.deleter
	def PstTradInstrmSzSpcfcThrshld(self):
		del self._PstTradInstrmSzSpcfcThrshld
		self._PstTradInstrmSzSpcfcThrshld = None

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
	def Sttstcs(self):
		return self._Sttstcs

	@Sttstcs.setter
	def Sttstcs(self, value):
		self._Sttstcs = value if type(value) != auto else self.make_default("Sttstcs")

	@Sttstcs.deleter
	def Sttstcs(self):
		del self._Sttstcs
		self._Sttstcs = None

	@property
	def PreTradLrgInScaleThrshld(self):
		return self._PreTradLrgInScaleThrshld

	@PreTradLrgInScaleThrshld.setter
	def PreTradLrgInScaleThrshld(self, value):
		self._PreTradLrgInScaleThrshld = value if type(value) != auto else self.make_default("PreTradLrgInScaleThrshld")

	@PreTradLrgInScaleThrshld.deleter
	def PreTradLrgInScaleThrshld(self):
		del self._PreTradLrgInScaleThrshld
		self._PreTradLrgInScaleThrshld = None

	@property
	def PstTradLrgInScaleThrshld(self):
		return self._PstTradLrgInScaleThrshld

	@PstTradLrgInScaleThrshld.setter
	def PstTradLrgInScaleThrshld(self, value):
		self._PstTradLrgInScaleThrshld = value if type(value) != auto else self.make_default("PstTradLrgInScaleThrshld")

	@PstTradLrgInScaleThrshld.deleter
	def PstTradLrgInScaleThrshld(self):
		del self._PstTradLrgInScaleThrshld
		self._PstTradLrgInScaleThrshld = None

	@property
	def PreTradInstrmSzSpcfcThrshld(self):
		return self._PreTradInstrmSzSpcfcThrshld

	@PreTradInstrmSzSpcfcThrshld.setter
	def PreTradInstrmSzSpcfcThrshld(self, value):
		self._PreTradInstrmSzSpcfcThrshld = value if type(value) != auto else self.make_default("PreTradInstrmSzSpcfcThrshld")

	@PreTradInstrmSzSpcfcThrshld.deleter
	def PreTradInstrmSzSpcfcThrshld(self):
		del self._PreTradInstrmSzSpcfcThrshld
		self._PreTradInstrmSzSpcfcThrshld = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradInstrmSzSpcfcThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lqdty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttstcs', type=StatisticsTransparency2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreTradLrgInScaleThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradLrgInScaleThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreTradInstrmSzSpcfcThrshld', type=TonsOrCurrency2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=InstrumentOrSubClassIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
	))

