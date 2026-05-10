from . import base_types
from ._LegalRestrictions4Choice import LegalRestrictions4Choice
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._TradingParameters2 import TradingParameters2
from ._SecurityStatus3Choice import SecurityStatus3Choice
from ._TEFRARules3Choice import TEFRARules3Choice
from ._Max256Text import Max256Text
from ._PutType3Choice import PutType3Choice
from ._CallType3Choice import CallType3Choice
from ._Max3NumericText import Max3NumericText
from ._SecurityWithHoldingTax1 import SecurityWithHoldingTax1
from ._ISODateTime import ISODateTime
from ._ClassificationType2 import ClassificationType2
from ._ISODate import ISODate
from ._AnyBICDec2014Identifier import AnyBICDec2014Identifier
from ._YesNoIndicator import YesNoIndicator
from ._SecuritiesPaymentStatus5Choice import SecuritiesPaymentStatus5Choice
from ._DateTimePeriod1 import DateTimePeriod1
from ._BenchmarkCurve6 import BenchmarkCurve6
from ._PartyIdentification136 import PartyIdentification136
from ._FinancialInstrumentForm2 import FinancialInstrumentForm2
from ._Max15NumericText import Max15NumericText
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._Max350Text import Max350Text
from ._InitialPhysicalForm4Choice import InitialPhysicalForm4Choice
from ._SecurityRestriction3 import SecurityRestriction3
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice
from ._Number import Number
from ._InitialPhysicalForm3Choice import InitialPhysicalForm3Choice
from ._SettlementInformation17 import SettlementInformation17
from ._Issuance5 import Issuance5
from ._Organisation38 import Organisation38
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._Max16Text import Max16Text
from ._Max35Text import Max35Text
from ._MaturityRedemptionType3Choice import MaturityRedemptionType3Choice

class CommonFinancialInstrumentAttributes10(base_types._BaseFieldType):

	__slots__ = ["_LeadMgr", "_Purp", "_ListgDt", "_RcrdDt", "_FinInstrmForm", "_TaxLotNb", "_PngAgt", "_ISOSctyShrtNm", "_ConvtblInd", "_CtctNm", "_Dpstry", "_UndrlygRsk", "_FngbInd", "_ConvsRatioDnmtr", "_CmonSfkpr", "_TEFRARule", "_Clss", "_AftrXchgPhysForm", "_XpryDt", "_CpnAttchdNb", "_CvrdInd", "_ConvsRatioNmrtr", "_NearTermPosLmt", "_WhldgTaxRgm", "_NmVldFr", "_ISOSctyLngNm", "_RedTp", "_CertNb", "_SrNb", "_SttlmInf", "_Issnc", "_DnmtnCcy", "_PrvtPlcmnt", "_TradgMkt", "_PmtSts", "_RedPmtCcy", "_ConvsPrd", "_CallTp", "_Cnfdtl", "_PmryPlcOfDpst", "_InitlPhysForm", "_ClssfctnTp", "_SctySts", "_PutTp", "_CtrctVrsnNb", "_PoolNb", "_Rstrctn", "_TradgMtd", "_LglRstrctns", "_SprdAndBchmkCrv", "_PrncplPngAgt", "_PosLmt"]
	@property
	def AftrXchgPhysForm(self):
		return self._AftrXchgPhysForm

	@AftrXchgPhysForm.setter
	def AftrXchgPhysForm(self, value):
		self._AftrXchgPhysForm = value if type(value) != base_types.auto else self.make_default("AftrXchgPhysForm")

	@AftrXchgPhysForm.deleter
	def AftrXchgPhysForm(self):
		del self._AftrXchgPhysForm
		self._AftrXchgPhysForm = None

	@property
	def CallTp(self):
		return self._CallTp

	@CallTp.setter
	def CallTp(self, value):
		self._CallTp = value if type(value) != base_types.auto else self.make_default("CallTp")

	@CallTp.deleter
	def CallTp(self):
		del self._CallTp
		self._CallTp = None

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if type(value) != base_types.auto else self.make_default("CertNb")

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = None

	@property
	def Clss(self):
		return self._Clss

	@Clss.setter
	def Clss(self, value):
		self._Clss = value if type(value) != base_types.auto else self.make_default("Clss")

	@Clss.deleter
	def Clss(self):
		del self._Clss
		self._Clss = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def CmonSfkpr(self):
		return self._CmonSfkpr

	@CmonSfkpr.setter
	def CmonSfkpr(self, value):
		self._CmonSfkpr = value if type(value) != base_types.auto else self.make_default("CmonSfkpr")

	@CmonSfkpr.deleter
	def CmonSfkpr(self):
		del self._CmonSfkpr
		self._CmonSfkpr = None

	@property
	def Cnfdtl(self):
		return self._Cnfdtl

	@Cnfdtl.setter
	def Cnfdtl(self, value):
		self._Cnfdtl = value if type(value) != base_types.auto else self.make_default("Cnfdtl")

	@Cnfdtl.deleter
	def Cnfdtl(self):
		del self._Cnfdtl
		self._Cnfdtl = None

	@property
	def ConvsPrd(self):
		return self._ConvsPrd

	@ConvsPrd.setter
	def ConvsPrd(self, value):
		self._ConvsPrd = value if type(value) != base_types.auto else self.make_default("ConvsPrd")

	@ConvsPrd.deleter
	def ConvsPrd(self):
		del self._ConvsPrd
		self._ConvsPrd = None

	@property
	def ConvsRatioDnmtr(self):
		return self._ConvsRatioDnmtr

	@ConvsRatioDnmtr.setter
	def ConvsRatioDnmtr(self, value):
		self._ConvsRatioDnmtr = value if type(value) != base_types.auto else self.make_default("ConvsRatioDnmtr")

	@ConvsRatioDnmtr.deleter
	def ConvsRatioDnmtr(self):
		del self._ConvsRatioDnmtr
		self._ConvsRatioDnmtr = None

	@property
	def ConvsRatioNmrtr(self):
		return self._ConvsRatioNmrtr

	@ConvsRatioNmrtr.setter
	def ConvsRatioNmrtr(self, value):
		self._ConvsRatioNmrtr = value if type(value) != base_types.auto else self.make_default("ConvsRatioNmrtr")

	@ConvsRatioNmrtr.deleter
	def ConvsRatioNmrtr(self):
		del self._ConvsRatioNmrtr
		self._ConvsRatioNmrtr = None

	@property
	def ConvtblInd(self):
		return self._ConvtblInd

	@ConvtblInd.setter
	def ConvtblInd(self, value):
		self._ConvtblInd = value if type(value) != base_types.auto else self.make_default("ConvtblInd")

	@ConvtblInd.deleter
	def ConvtblInd(self):
		del self._ConvtblInd
		self._ConvtblInd = None

	@property
	def CpnAttchdNb(self):
		return self._CpnAttchdNb

	@CpnAttchdNb.setter
	def CpnAttchdNb(self, value):
		self._CpnAttchdNb = value if type(value) != base_types.auto else self.make_default("CpnAttchdNb")

	@CpnAttchdNb.deleter
	def CpnAttchdNb(self):
		del self._CpnAttchdNb
		self._CpnAttchdNb = None

	@property
	def CtctNm(self):
		return self._CtctNm

	@CtctNm.setter
	def CtctNm(self, value):
		self._CtctNm = value if type(value) != base_types.auto else self.make_default("CtctNm")

	@CtctNm.deleter
	def CtctNm(self):
		del self._CtctNm
		self._CtctNm = None

	@property
	def CtrctVrsnNb(self):
		return self._CtrctVrsnNb

	@CtrctVrsnNb.setter
	def CtrctVrsnNb(self, value):
		self._CtrctVrsnNb = value if type(value) != base_types.auto else self.make_default("CtrctVrsnNb")

	@CtrctVrsnNb.deleter
	def CtrctVrsnNb(self):
		del self._CtrctVrsnNb
		self._CtrctVrsnNb = None

	@property
	def CvrdInd(self):
		return self._CvrdInd

	@CvrdInd.setter
	def CvrdInd(self, value):
		self._CvrdInd = value if type(value) != base_types.auto else self.make_default("CvrdInd")

	@CvrdInd.deleter
	def CvrdInd(self):
		del self._CvrdInd
		self._CvrdInd = None

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != base_types.auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	@property
	def FinInstrmForm(self):
		return self._FinInstrmForm

	@FinInstrmForm.setter
	def FinInstrmForm(self, value):
		self._FinInstrmForm = value if type(value) != base_types.auto else self.make_default("FinInstrmForm")

	@FinInstrmForm.deleter
	def FinInstrmForm(self):
		del self._FinInstrmForm
		self._FinInstrmForm = None

	@property
	def FngbInd(self):
		return self._FngbInd

	@FngbInd.setter
	def FngbInd(self, value):
		self._FngbInd = value if type(value) != base_types.auto else self.make_default("FngbInd")

	@FngbInd.deleter
	def FngbInd(self):
		del self._FngbInd
		self._FngbInd = None

	@property
	def ISOSctyLngNm(self):
		return self._ISOSctyLngNm

	@ISOSctyLngNm.setter
	def ISOSctyLngNm(self, value):
		self._ISOSctyLngNm = value if type(value) != base_types.auto else self.make_default("ISOSctyLngNm")

	@ISOSctyLngNm.deleter
	def ISOSctyLngNm(self):
		del self._ISOSctyLngNm
		self._ISOSctyLngNm = None

	@property
	def ISOSctyShrtNm(self):
		return self._ISOSctyShrtNm

	@ISOSctyShrtNm.setter
	def ISOSctyShrtNm(self, value):
		self._ISOSctyShrtNm = value if type(value) != base_types.auto else self.make_default("ISOSctyShrtNm")

	@ISOSctyShrtNm.deleter
	def ISOSctyShrtNm(self):
		del self._ISOSctyShrtNm
		self._ISOSctyShrtNm = None

	@property
	def InitlPhysForm(self):
		return self._InitlPhysForm

	@InitlPhysForm.setter
	def InitlPhysForm(self, value):
		self._InitlPhysForm = value if type(value) != base_types.auto else self.make_default("InitlPhysForm")

	@InitlPhysForm.deleter
	def InitlPhysForm(self):
		del self._InitlPhysForm
		self._InitlPhysForm = None

	@property
	def Issnc(self):
		return self._Issnc

	@Issnc.setter
	def Issnc(self, value):
		self._Issnc = value if type(value) != base_types.auto else self.make_default("Issnc")

	@Issnc.deleter
	def Issnc(self):
		del self._Issnc
		self._Issnc = None

	@property
	def LeadMgr(self):
		return self._LeadMgr

	@LeadMgr.setter
	def LeadMgr(self, value):
		self._LeadMgr = value if type(value) != base_types.auto else self.make_default("LeadMgr")

	@LeadMgr.deleter
	def LeadMgr(self):
		del self._LeadMgr
		self._LeadMgr = None

	@property
	def LglRstrctns(self):
		return self._LglRstrctns

	@LglRstrctns.setter
	def LglRstrctns(self, value):
		self._LglRstrctns = value if type(value) != base_types.auto else self.make_default("LglRstrctns")

	@LglRstrctns.deleter
	def LglRstrctns(self):
		del self._LglRstrctns
		self._LglRstrctns = None

	@property
	def ListgDt(self):
		return self._ListgDt

	@ListgDt.setter
	def ListgDt(self, value):
		self._ListgDt = value if type(value) != base_types.auto else self.make_default("ListgDt")

	@ListgDt.deleter
	def ListgDt(self):
		del self._ListgDt
		self._ListgDt = None

	@property
	def NearTermPosLmt(self):
		return self._NearTermPosLmt

	@NearTermPosLmt.setter
	def NearTermPosLmt(self, value):
		self._NearTermPosLmt = value if type(value) != base_types.auto else self.make_default("NearTermPosLmt")

	@NearTermPosLmt.deleter
	def NearTermPosLmt(self):
		del self._NearTermPosLmt
		self._NearTermPosLmt = None

	@property
	def NmVldFr(self):
		return self._NmVldFr

	@NmVldFr.setter
	def NmVldFr(self, value):
		self._NmVldFr = value if type(value) != base_types.auto else self.make_default("NmVldFr")

	@NmVldFr.deleter
	def NmVldFr(self):
		del self._NmVldFr
		self._NmVldFr = None

	@property
	def PmryPlcOfDpst(self):
		return self._PmryPlcOfDpst

	@PmryPlcOfDpst.setter
	def PmryPlcOfDpst(self, value):
		self._PmryPlcOfDpst = value if type(value) != base_types.auto else self.make_default("PmryPlcOfDpst")

	@PmryPlcOfDpst.deleter
	def PmryPlcOfDpst(self):
		del self._PmryPlcOfDpst
		self._PmryPlcOfDpst = None

	@property
	def PmtSts(self):
		return self._PmtSts

	@PmtSts.setter
	def PmtSts(self, value):
		self._PmtSts = value if type(value) != base_types.auto else self.make_default("PmtSts")

	@PmtSts.deleter
	def PmtSts(self):
		del self._PmtSts
		self._PmtSts = None

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if type(value) != base_types.auto else self.make_default("PngAgt")

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = None

	@property
	def PoolNb(self):
		return self._PoolNb

	@PoolNb.setter
	def PoolNb(self, value):
		self._PoolNb = value if type(value) != base_types.auto else self.make_default("PoolNb")

	@PoolNb.deleter
	def PoolNb(self):
		del self._PoolNb
		self._PoolNb = None

	@property
	def PosLmt(self):
		return self._PosLmt

	@PosLmt.setter
	def PosLmt(self, value):
		self._PosLmt = value if type(value) != base_types.auto else self.make_default("PosLmt")

	@PosLmt.deleter
	def PosLmt(self):
		del self._PosLmt
		self._PosLmt = None

	@property
	def PrncplPngAgt(self):
		return self._PrncplPngAgt

	@PrncplPngAgt.setter
	def PrncplPngAgt(self, value):
		self._PrncplPngAgt = value if type(value) != base_types.auto else self.make_default("PrncplPngAgt")

	@PrncplPngAgt.deleter
	def PrncplPngAgt(self):
		del self._PrncplPngAgt
		self._PrncplPngAgt = None

	@property
	def PrvtPlcmnt(self):
		return self._PrvtPlcmnt

	@PrvtPlcmnt.setter
	def PrvtPlcmnt(self, value):
		self._PrvtPlcmnt = value if type(value) != base_types.auto else self.make_default("PrvtPlcmnt")

	@PrvtPlcmnt.deleter
	def PrvtPlcmnt(self):
		del self._PrvtPlcmnt
		self._PrvtPlcmnt = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def PutTp(self):
		return self._PutTp

	@PutTp.setter
	def PutTp(self, value):
		self._PutTp = value if type(value) != base_types.auto else self.make_default("PutTp")

	@PutTp.deleter
	def PutTp(self):
		del self._PutTp
		self._PutTp = None

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if type(value) != base_types.auto else self.make_default("RcrdDt")

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = None

	@property
	def RedPmtCcy(self):
		return self._RedPmtCcy

	@RedPmtCcy.setter
	def RedPmtCcy(self, value):
		self._RedPmtCcy = value if type(value) != base_types.auto else self.make_default("RedPmtCcy")

	@RedPmtCcy.deleter
	def RedPmtCcy(self):
		del self._RedPmtCcy
		self._RedPmtCcy = None

	@property
	def RedTp(self):
		return self._RedTp

	@RedTp.setter
	def RedTp(self, value):
		self._RedTp = value if type(value) != base_types.auto else self.make_default("RedTp")

	@RedTp.deleter
	def RedTp(self):
		del self._RedTp
		self._RedTp = None

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if type(value) != base_types.auto else self.make_default("Rstrctn")

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = None

	@property
	def SctySts(self):
		return self._SctySts

	@SctySts.setter
	def SctySts(self, value):
		self._SctySts = value if type(value) != base_types.auto else self.make_default("SctySts")

	@SctySts.deleter
	def SctySts(self):
		del self._SctySts
		self._SctySts = None

	@property
	def SprdAndBchmkCrv(self):
		return self._SprdAndBchmkCrv

	@SprdAndBchmkCrv.setter
	def SprdAndBchmkCrv(self, value):
		self._SprdAndBchmkCrv = value if type(value) != base_types.auto else self.make_default("SprdAndBchmkCrv")

	@SprdAndBchmkCrv.deleter
	def SprdAndBchmkCrv(self):
		del self._SprdAndBchmkCrv
		self._SprdAndBchmkCrv = None

	@property
	def SrNb(self):
		return self._SrNb

	@SrNb.setter
	def SrNb(self, value):
		self._SrNb = value if type(value) != base_types.auto else self.make_default("SrNb")

	@SrNb.deleter
	def SrNb(self):
		del self._SrNb
		self._SrNb = None

	@property
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if type(value) != base_types.auto else self.make_default("SttlmInf")

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = None

	@property
	def TEFRARule(self):
		return self._TEFRARule

	@TEFRARule.setter
	def TEFRARule(self, value):
		self._TEFRARule = value if type(value) != base_types.auto else self.make_default("TEFRARule")

	@TEFRARule.deleter
	def TEFRARule(self):
		del self._TEFRARule
		self._TEFRARule = None

	@property
	def TaxLotNb(self):
		return self._TaxLotNb

	@TaxLotNb.setter
	def TaxLotNb(self, value):
		self._TaxLotNb = value if type(value) != base_types.auto else self.make_default("TaxLotNb")

	@TaxLotNb.deleter
	def TaxLotNb(self):
		del self._TaxLotNb
		self._TaxLotNb = None

	@property
	def TradgMkt(self):
		return self._TradgMkt

	@TradgMkt.setter
	def TradgMkt(self, value):
		self._TradgMkt = value if type(value) != base_types.auto else self.make_default("TradgMkt")

	@TradgMkt.deleter
	def TradgMkt(self):
		del self._TradgMkt
		self._TradgMkt = None

	@property
	def TradgMtd(self):
		return self._TradgMtd

	@TradgMtd.setter
	def TradgMtd(self, value):
		self._TradgMtd = value if type(value) != base_types.auto else self.make_default("TradgMtd")

	@TradgMtd.deleter
	def TradgMtd(self):
		del self._TradgMtd
		self._TradgMtd = None

	@property
	def UndrlygRsk(self):
		return self._UndrlygRsk

	@UndrlygRsk.setter
	def UndrlygRsk(self, value):
		self._UndrlygRsk = value if type(value) != base_types.auto else self.make_default("UndrlygRsk")

	@UndrlygRsk.deleter
	def UndrlygRsk(self):
		del self._UndrlygRsk
		self._UndrlygRsk = None

	@property
	def WhldgTaxRgm(self):
		return self._WhldgTaxRgm

	@WhldgTaxRgm.setter
	def WhldgTaxRgm(self, value):
		self._WhldgTaxRgm = value if type(value) != base_types.auto else self.make_default("WhldgTaxRgm")

	@WhldgTaxRgm.deleter
	def WhldgTaxRgm(self):
		del self._WhldgTaxRgm
		self._WhldgTaxRgm = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AftrXchgPhysForm', type=InitialPhysicalForm3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallTp', type=CallType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clss', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonSfkpr', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnfdtl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPrd', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsRatioDnmtr', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsRatioNmrtr', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnAttchdNb', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctNm', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctVrsnNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmForm', type=FinancialInstrumentForm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FngbInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISOSctyLngNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISOSctyShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlPhysForm', type=InitialPhysicalForm4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issnc', type=Issuance5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LeadMgr', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRstrctns', type=LegalRestrictions4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NearTermPosLmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmVldFr', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryPlcOfDpst', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSts', type=SecuritiesPaymentStatus5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolNb', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosLmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplPngAgt', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtPlcmnt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutTp', type=PutType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedTp', type=MaturityRedemptionType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctn', type=SecurityRestriction3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctySts', type=SecurityStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SprdAndBchmkCrv', type=BenchmarkCurve6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SrNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInf', type=SettlementInformation17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TEFRARule', type=TEFRARules3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxLotNb', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMkt', type=TradingParameters2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradgMtd', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygRsk', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRgm', type=SecurityWithHoldingTax1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

