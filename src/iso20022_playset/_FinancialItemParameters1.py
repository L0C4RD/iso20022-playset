from . import base_types
from .TradeMarket1Choice import TradeMarket1Choice
from .ExternalDocumentPurpose1Code import ExternalDocumentPurpose1Code
from .ISODate import ISODate
from .AccountIdentification4Choice import AccountIdentification4Choice
from .xs:IDREF import xs:IDREF
from .CurrencyCode import CurrencyCode
from .Max35Text import Max35Text
from .LanguageCode import LanguageCode

class FinancialItemParameters1(base_types._BaseFieldType):

	__slots__ = ["_LangCd", "_Ccy", "_LglCntxt", "_SellrFinAgt", "_Buyr", "_DbtAcct", "_BuyrFinAgt", "_IsseDt", "_CdtAcct", "_RltdItm", "_Issr", "_GovngCtrct", "_Rcpt", "_Idr", "_TradMkt", "_DocPurp", "_Sellr"]
	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if type(value) != base_types.auto else self.make_default("LangCd")

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def LglCntxt(self):
		return self._LglCntxt

	@LglCntxt.setter
	def LglCntxt(self, value):
		self._LglCntxt = value if type(value) != base_types.auto else self.make_default("LglCntxt")

	@LglCntxt.deleter
	def LglCntxt(self):
		del self._LglCntxt
		self._LglCntxt = None

	@property
	def SellrFinAgt(self):
		return self._SellrFinAgt

	@SellrFinAgt.setter
	def SellrFinAgt(self, value):
		self._SellrFinAgt = value if type(value) != base_types.auto else self.make_default("SellrFinAgt")

	@SellrFinAgt.deleter
	def SellrFinAgt(self):
		del self._SellrFinAgt
		self._SellrFinAgt = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != base_types.auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def DbtAcct(self):
		return self._DbtAcct

	@DbtAcct.setter
	def DbtAcct(self, value):
		self._DbtAcct = value if type(value) != base_types.auto else self.make_default("DbtAcct")

	@DbtAcct.deleter
	def DbtAcct(self):
		del self._DbtAcct
		self._DbtAcct = None

	@property
	def BuyrFinAgt(self):
		return self._BuyrFinAgt

	@BuyrFinAgt.setter
	def BuyrFinAgt(self, value):
		self._BuyrFinAgt = value if type(value) != base_types.auto else self.make_default("BuyrFinAgt")

	@BuyrFinAgt.deleter
	def BuyrFinAgt(self):
		del self._BuyrFinAgt
		self._BuyrFinAgt = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def CdtAcct(self):
		return self._CdtAcct

	@CdtAcct.setter
	def CdtAcct(self, value):
		self._CdtAcct = value if type(value) != base_types.auto else self.make_default("CdtAcct")

	@CdtAcct.deleter
	def CdtAcct(self):
		del self._CdtAcct
		self._CdtAcct = None

	@property
	def RltdItm(self):
		return self._RltdItm

	@RltdItm.setter
	def RltdItm(self, value):
		self._RltdItm = value if type(value) != base_types.auto else self.make_default("RltdItm")

	@RltdItm.deleter
	def RltdItm(self):
		del self._RltdItm
		self._RltdItm = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def GovngCtrct(self):
		return self._GovngCtrct

	@GovngCtrct.setter
	def GovngCtrct(self, value):
		self._GovngCtrct = value if type(value) != base_types.auto else self.make_default("GovngCtrct")

	@GovngCtrct.deleter
	def GovngCtrct(self):
		del self._GovngCtrct
		self._GovngCtrct = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != base_types.auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	@property
	def TradMkt(self):
		return self._TradMkt

	@TradMkt.setter
	def TradMkt(self, value):
		self._TradMkt = value if type(value) != base_types.auto else self.make_default("TradMkt")

	@TradMkt.deleter
	def TradMkt(self):
		del self._TradMkt
		self._TradMkt = None

	@property
	def DocPurp(self):
		return self._DocPurp

	@DocPurp.setter
	def DocPurp(self, value):
		self._DocPurp = value if type(value) != base_types.auto else self.make_default("DocPurp")

	@DocPurp.deleter
	def DocPurp(self):
		del self._DocPurp
		self._DocPurp = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != base_types.auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=CurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCntxt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrFinAgt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrFinAgt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdItm', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngCtrct', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcpt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradMkt', type=TradeMarket1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocPurp', type=ExternalDocumentPurpose1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
	))

