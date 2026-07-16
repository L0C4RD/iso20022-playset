# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import CurrencyCode
from . import ExternalDocumentPurpose1Code
from . import ISODate
from . import LanguageCode
from . import Max35Text
from . import TradeMarket1Choice
from . import xs:IDREF

class FinancialItemParameters1(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_BuyrFinAgt", "_Ccy", "_CdtAcct", "_DbtAcct", "_DocPurp", "_GovngCtrct", "_Idr", "_IsseDt", "_Issr", "_LangCd", "_LglCntxt", "_Rcpt", "_RltdItm", "_Sellr", "_SellrFinAgt", "_TradMkt"]
	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', xs:IDREF, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', xs:IDREF, False)

	@property
	def BuyrFinAgt(self):
		return self._BuyrFinAgt

	@BuyrFinAgt.setter
	def BuyrFinAgt(self, value):
		self._BuyrFinAgt = value if value is not None else base_types.UninitialisedField(self, 'BuyrFinAgt', xs:IDREF, False)

	@BuyrFinAgt.deleter
	def BuyrFinAgt(self):
		del self._BuyrFinAgt
		self._BuyrFinAgt = base_types.UninitialisedField(self, 'BuyrFinAgt', xs:IDREF, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', CurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', CurrencyCode, False)

	@property
	def CdtAcct(self):
		return self._CdtAcct

	@CdtAcct.setter
	def CdtAcct(self, value):
		self._CdtAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtAcct', AccountIdentification4Choice, False)

	@CdtAcct.deleter
	def CdtAcct(self):
		del self._CdtAcct
		self._CdtAcct = base_types.UninitialisedField(self, 'CdtAcct', AccountIdentification4Choice, False)

	@property
	def DbtAcct(self):
		return self._DbtAcct

	@DbtAcct.setter
	def DbtAcct(self, value):
		self._DbtAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtAcct', AccountIdentification4Choice, False)

	@DbtAcct.deleter
	def DbtAcct(self):
		del self._DbtAcct
		self._DbtAcct = base_types.UninitialisedField(self, 'DbtAcct', AccountIdentification4Choice, False)

	@property
	def DocPurp(self):
		return self._DocPurp

	@DocPurp.setter
	def DocPurp(self, value):
		self._DocPurp = value if value is not None else base_types.UninitialisedField(self, 'DocPurp', ExternalDocumentPurpose1Code, False)

	@DocPurp.deleter
	def DocPurp(self):
		del self._DocPurp
		self._DocPurp = base_types.UninitialisedField(self, 'DocPurp', ExternalDocumentPurpose1Code, False)

	@property
	def GovngCtrct(self):
		return self._GovngCtrct

	@GovngCtrct.setter
	def GovngCtrct(self, value):
		self._GovngCtrct = value if value is not None else base_types.UninitialisedField(self, 'GovngCtrct', xs:IDREF, True)

	@GovngCtrct.deleter
	def GovngCtrct(self):
		del self._GovngCtrct
		self._GovngCtrct = base_types.UninitialisedField(self, 'GovngCtrct', xs:IDREF, True)

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if value is not None else base_types.UninitialisedField(self, 'Idr', Max35Text, False)

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = base_types.UninitialisedField(self, 'Idr', Max35Text, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', xs:IDREF, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', xs:IDREF, False)

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if value is not None else base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@property
	def LglCntxt(self):
		return self._LglCntxt

	@LglCntxt.setter
	def LglCntxt(self, value):
		self._LglCntxt = value if value is not None else base_types.UninitialisedField(self, 'LglCntxt', xs:IDREF, False)

	@LglCntxt.deleter
	def LglCntxt(self):
		del self._LglCntxt
		self._LglCntxt = base_types.UninitialisedField(self, 'LglCntxt', xs:IDREF, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', xs:IDREF, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', xs:IDREF, False)

	@property
	def RltdItm(self):
		return self._RltdItm

	@RltdItm.setter
	def RltdItm(self, value):
		self._RltdItm = value if value is not None else base_types.UninitialisedField(self, 'RltdItm', xs:IDREF, True)

	@RltdItm.deleter
	def RltdItm(self):
		del self._RltdItm
		self._RltdItm = base_types.UninitialisedField(self, 'RltdItm', xs:IDREF, True)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', xs:IDREF, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', xs:IDREF, False)

	@property
	def SellrFinAgt(self):
		return self._SellrFinAgt

	@SellrFinAgt.setter
	def SellrFinAgt(self, value):
		self._SellrFinAgt = value if value is not None else base_types.UninitialisedField(self, 'SellrFinAgt', xs:IDREF, False)

	@SellrFinAgt.deleter
	def SellrFinAgt(self):
		del self._SellrFinAgt
		self._SellrFinAgt = base_types.UninitialisedField(self, 'SellrFinAgt', xs:IDREF, False)

	@property
	def TradMkt(self):
		return self._TradMkt

	@TradMkt.setter
	def TradMkt(self, value):
		self._TradMkt = value if value is not None else base_types.UninitialisedField(self, 'TradMkt', TradeMarket1Choice, False)

	@TradMkt.deleter
	def TradMkt(self):
		del self._TradMkt
		self._TradMkt = base_types.UninitialisedField(self, 'TradMkt', TradeMarket1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrFinAgt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=CurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocPurp', type=ExternalDocumentPurpose1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngCtrct', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCntxt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdItm', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrFinAgt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradMkt', type=TradeMarket1Choice, min=0, max=1, mutex_group=None, array=False),
	))