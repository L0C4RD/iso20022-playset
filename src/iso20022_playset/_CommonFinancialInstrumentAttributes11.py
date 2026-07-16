# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ActiveOrHistoricCurrencyCode
from . import BenchmarkCurve6
from . import CallType3Choice
from . import ClassificationType2
from . import DateTimePeriod1
from . import FinancialInstrumentForm2
from . import FinancialInstrumentIdentificationValidity3
from . import FinancialInstrumentName2
from . import FinancialInstrumentQuantity1Choice
from . import ISODate
from . import ISODateTime
from . import InitialPhysicalForm3Choice
from . import InitialPhysicalForm4Choice
from . import Issuance6
from . import LegalRestrictions4Choice
from . import MaturityRedemptionType3Choice
from . import Max15NumericText
from . import Max16Text
from . import Max256Text
from . import Max35Text
from . import Max3NumericText
from . import Number
from . import Organisation38
from . import PartyIdentification136
from . import PartyIdentification177Choice
from . import PutType3Choice
from . import SecuritiesPaymentStatus5Choice
from . import SecurityCSDLink7
from . import SecurityRestriction3
from . import SecurityStatus3Choice
from . import SecurityWithHoldingTax1
from . import SettlementInformation17
from . import TEFRARules3Choice
from . import TradingParameters2
from . import UnitOrFaceAmount1Choice
from . import YesNoIndicator

class CommonFinancialInstrumentAttributes11(base_types._BaseFieldType):

	__slots__ = ["_AftrXchgPhysForm", "_CallTp", "_CertNb", "_Clss", "_ClssfctnTp", "_CmonSfkpr", "_Cnfdtl", "_ConvsPrd", "_ConvsRatioDnmtr", "_ConvsRatioNmrtr", "_ConvtblInd", "_CpnAttchdNb", "_CtctNm", "_CtrctVrsnNb", "_CvrdInd", "_DnmtnCcy", "_Dpstry", "_FinInstrmForm", "_FinInstrmIdVldty", "_FinInstrmNm", "_FngbInd", "_InitlPhysForm", "_Issnc", "_LeadMgr", "_LglRstrctns", "_ListgDt", "_NearTermPosLmt", "_PmryPlcOfDpst", "_PmtSts", "_PngAgt", "_PoolNb", "_PosLmt", "_PrncplPngAgt", "_PrvtPlcmnt", "_Purp", "_PutTp", "_RcrdDt", "_RedPmtCcy", "_RedTp", "_Rstrctn", "_SctyCSDLk", "_SctySts", "_SprdAndBchmkCrv", "_SrNb", "_SttlmInf", "_TEFRARule", "_TaxLotNb", "_TradgMkt", "_TradgMtd", "_UndrlygRsk", "_WhldgTaxRgm", "_XpryDt"]
	@property
	def AftrXchgPhysForm(self):
		return self._AftrXchgPhysForm

	@AftrXchgPhysForm.setter
	def AftrXchgPhysForm(self, value):
		self._AftrXchgPhysForm = value if value is not None else base_types.UninitialisedField(self, 'AftrXchgPhysForm', InitialPhysicalForm3Choice, False)

	@AftrXchgPhysForm.deleter
	def AftrXchgPhysForm(self):
		del self._AftrXchgPhysForm
		self._AftrXchgPhysForm = base_types.UninitialisedField(self, 'AftrXchgPhysForm', InitialPhysicalForm3Choice, False)

	@property
	def CallTp(self):
		return self._CallTp

	@CallTp.setter
	def CallTp(self, value):
		self._CallTp = value if value is not None else base_types.UninitialisedField(self, 'CallTp', CallType3Choice, False)

	@CallTp.deleter
	def CallTp(self):
		del self._CallTp
		self._CallTp = base_types.UninitialisedField(self, 'CallTp', CallType3Choice, False)

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', Max35Text, False)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', Max35Text, False)

	@property
	def Clss(self):
		return self._Clss

	@Clss.setter
	def Clss(self, value):
		self._Clss = value if value is not None else base_types.UninitialisedField(self, 'Clss', Max16Text, False)

	@Clss.deleter
	def Clss(self):
		del self._Clss
		self._Clss = base_types.UninitialisedField(self, 'Clss', Max16Text, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType2, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType2, False)

	@property
	def CmonSfkpr(self):
		return self._CmonSfkpr

	@CmonSfkpr.setter
	def CmonSfkpr(self, value):
		self._CmonSfkpr = value if value is not None else base_types.UninitialisedField(self, 'CmonSfkpr', PartyIdentification177Choice, False)

	@CmonSfkpr.deleter
	def CmonSfkpr(self):
		del self._CmonSfkpr
		self._CmonSfkpr = base_types.UninitialisedField(self, 'CmonSfkpr', PartyIdentification177Choice, False)

	@property
	def Cnfdtl(self):
		return self._Cnfdtl

	@Cnfdtl.setter
	def Cnfdtl(self, value):
		self._Cnfdtl = value if value is not None else base_types.UninitialisedField(self, 'Cnfdtl', YesNoIndicator, False)

	@Cnfdtl.deleter
	def Cnfdtl(self):
		del self._Cnfdtl
		self._Cnfdtl = base_types.UninitialisedField(self, 'Cnfdtl', YesNoIndicator, False)

	@property
	def ConvsPrd(self):
		return self._ConvsPrd

	@ConvsPrd.setter
	def ConvsPrd(self, value):
		self._ConvsPrd = value if value is not None else base_types.UninitialisedField(self, 'ConvsPrd', DateTimePeriod1, False)

	@ConvsPrd.deleter
	def ConvsPrd(self):
		del self._ConvsPrd
		self._ConvsPrd = base_types.UninitialisedField(self, 'ConvsPrd', DateTimePeriod1, False)

	@property
	def ConvsRatioDnmtr(self):
		return self._ConvsRatioDnmtr

	@ConvsRatioDnmtr.setter
	def ConvsRatioDnmtr(self, value):
		self._ConvsRatioDnmtr = value if value is not None else base_types.UninitialisedField(self, 'ConvsRatioDnmtr', FinancialInstrumentQuantity1Choice, False)

	@ConvsRatioDnmtr.deleter
	def ConvsRatioDnmtr(self):
		del self._ConvsRatioDnmtr
		self._ConvsRatioDnmtr = base_types.UninitialisedField(self, 'ConvsRatioDnmtr', FinancialInstrumentQuantity1Choice, False)

	@property
	def ConvsRatioNmrtr(self):
		return self._ConvsRatioNmrtr

	@ConvsRatioNmrtr.setter
	def ConvsRatioNmrtr(self, value):
		self._ConvsRatioNmrtr = value if value is not None else base_types.UninitialisedField(self, 'ConvsRatioNmrtr', FinancialInstrumentQuantity1Choice, False)

	@ConvsRatioNmrtr.deleter
	def ConvsRatioNmrtr(self):
		del self._ConvsRatioNmrtr
		self._ConvsRatioNmrtr = base_types.UninitialisedField(self, 'ConvsRatioNmrtr', FinancialInstrumentQuantity1Choice, False)

	@property
	def ConvtblInd(self):
		return self._ConvtblInd

	@ConvtblInd.setter
	def ConvtblInd(self, value):
		self._ConvtblInd = value if value is not None else base_types.UninitialisedField(self, 'ConvtblInd', YesNoIndicator, False)

	@ConvtblInd.deleter
	def ConvtblInd(self):
		del self._ConvtblInd
		self._ConvtblInd = base_types.UninitialisedField(self, 'ConvtblInd', YesNoIndicator, False)

	@property
	def CpnAttchdNb(self):
		return self._CpnAttchdNb

	@CpnAttchdNb.setter
	def CpnAttchdNb(self, value):
		self._CpnAttchdNb = value if value is not None else base_types.UninitialisedField(self, 'CpnAttchdNb', Max3NumericText, False)

	@CpnAttchdNb.deleter
	def CpnAttchdNb(self):
		del self._CpnAttchdNb
		self._CpnAttchdNb = base_types.UninitialisedField(self, 'CpnAttchdNb', Max3NumericText, False)

	@property
	def CtctNm(self):
		return self._CtctNm

	@CtctNm.setter
	def CtctNm(self, value):
		self._CtctNm = value if value is not None else base_types.UninitialisedField(self, 'CtctNm', Organisation38, False)

	@CtctNm.deleter
	def CtctNm(self):
		del self._CtctNm
		self._CtctNm = base_types.UninitialisedField(self, 'CtctNm', Organisation38, False)

	@property
	def CtrctVrsnNb(self):
		return self._CtrctVrsnNb

	@CtrctVrsnNb.setter
	def CtrctVrsnNb(self, value):
		self._CtrctVrsnNb = value if value is not None else base_types.UninitialisedField(self, 'CtrctVrsnNb', Number, False)

	@CtrctVrsnNb.deleter
	def CtrctVrsnNb(self):
		del self._CtrctVrsnNb
		self._CtrctVrsnNb = base_types.UninitialisedField(self, 'CtrctVrsnNb', Number, False)

	@property
	def CvrdInd(self):
		return self._CvrdInd

	@CvrdInd.setter
	def CvrdInd(self, value):
		self._CvrdInd = value if value is not None else base_types.UninitialisedField(self, 'CvrdInd', YesNoIndicator, False)

	@CvrdInd.deleter
	def CvrdInd(self):
		del self._CvrdInd
		self._CvrdInd = base_types.UninitialisedField(self, 'CvrdInd', YesNoIndicator, False)

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if value is not None else base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', Organisation38, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', Organisation38, False)

	@property
	def FinInstrmForm(self):
		return self._FinInstrmForm

	@FinInstrmForm.setter
	def FinInstrmForm(self, value):
		self._FinInstrmForm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmForm', FinancialInstrumentForm2, False)

	@FinInstrmForm.deleter
	def FinInstrmForm(self):
		del self._FinInstrmForm
		self._FinInstrmForm = base_types.UninitialisedField(self, 'FinInstrmForm', FinancialInstrumentForm2, False)

	@property
	def FinInstrmIdVldty(self):
		return self._FinInstrmIdVldty

	@FinInstrmIdVldty.setter
	def FinInstrmIdVldty(self, value):
		self._FinInstrmIdVldty = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmIdVldty', FinancialInstrumentIdentificationValidity3, True)

	@FinInstrmIdVldty.deleter
	def FinInstrmIdVldty(self):
		del self._FinInstrmIdVldty
		self._FinInstrmIdVldty = base_types.UninitialisedField(self, 'FinInstrmIdVldty', FinancialInstrumentIdentificationValidity3, True)

	@property
	def FinInstrmNm(self):
		return self._FinInstrmNm

	@FinInstrmNm.setter
	def FinInstrmNm(self, value):
		self._FinInstrmNm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmNm', FinancialInstrumentName2, True)

	@FinInstrmNm.deleter
	def FinInstrmNm(self):
		del self._FinInstrmNm
		self._FinInstrmNm = base_types.UninitialisedField(self, 'FinInstrmNm', FinancialInstrumentName2, True)

	@property
	def FngbInd(self):
		return self._FngbInd

	@FngbInd.setter
	def FngbInd(self, value):
		self._FngbInd = value if value is not None else base_types.UninitialisedField(self, 'FngbInd', YesNoIndicator, False)

	@FngbInd.deleter
	def FngbInd(self):
		del self._FngbInd
		self._FngbInd = base_types.UninitialisedField(self, 'FngbInd', YesNoIndicator, False)

	@property
	def InitlPhysForm(self):
		return self._InitlPhysForm

	@InitlPhysForm.setter
	def InitlPhysForm(self, value):
		self._InitlPhysForm = value if value is not None else base_types.UninitialisedField(self, 'InitlPhysForm', InitialPhysicalForm4Choice, False)

	@InitlPhysForm.deleter
	def InitlPhysForm(self):
		del self._InitlPhysForm
		self._InitlPhysForm = base_types.UninitialisedField(self, 'InitlPhysForm', InitialPhysicalForm4Choice, False)

	@property
	def Issnc(self):
		return self._Issnc

	@Issnc.setter
	def Issnc(self, value):
		self._Issnc = value if value is not None else base_types.UninitialisedField(self, 'Issnc', Issuance6, False)

	@Issnc.deleter
	def Issnc(self):
		del self._Issnc
		self._Issnc = base_types.UninitialisedField(self, 'Issnc', Issuance6, False)

	@property
	def LeadMgr(self):
		return self._LeadMgr

	@LeadMgr.setter
	def LeadMgr(self, value):
		self._LeadMgr = value if value is not None else base_types.UninitialisedField(self, 'LeadMgr', Organisation38, False)

	@LeadMgr.deleter
	def LeadMgr(self):
		del self._LeadMgr
		self._LeadMgr = base_types.UninitialisedField(self, 'LeadMgr', Organisation38, False)

	@property
	def LglRstrctns(self):
		return self._LglRstrctns

	@LglRstrctns.setter
	def LglRstrctns(self, value):
		self._LglRstrctns = value if value is not None else base_types.UninitialisedField(self, 'LglRstrctns', LegalRestrictions4Choice, False)

	@LglRstrctns.deleter
	def LglRstrctns(self):
		del self._LglRstrctns
		self._LglRstrctns = base_types.UninitialisedField(self, 'LglRstrctns', LegalRestrictions4Choice, False)

	@property
	def ListgDt(self):
		return self._ListgDt

	@ListgDt.setter
	def ListgDt(self, value):
		self._ListgDt = value if value is not None else base_types.UninitialisedField(self, 'ListgDt', ISODate, False)

	@ListgDt.deleter
	def ListgDt(self):
		del self._ListgDt
		self._ListgDt = base_types.UninitialisedField(self, 'ListgDt', ISODate, False)

	@property
	def NearTermPosLmt(self):
		return self._NearTermPosLmt

	@NearTermPosLmt.setter
	def NearTermPosLmt(self, value):
		self._NearTermPosLmt = value if value is not None else base_types.UninitialisedField(self, 'NearTermPosLmt', FinancialInstrumentQuantity1Choice, False)

	@NearTermPosLmt.deleter
	def NearTermPosLmt(self):
		del self._NearTermPosLmt
		self._NearTermPosLmt = base_types.UninitialisedField(self, 'NearTermPosLmt', FinancialInstrumentQuantity1Choice, False)

	@property
	def PmryPlcOfDpst(self):
		return self._PmryPlcOfDpst

	@PmryPlcOfDpst.setter
	def PmryPlcOfDpst(self, value):
		self._PmryPlcOfDpst = value if value is not None else base_types.UninitialisedField(self, 'PmryPlcOfDpst', PartyIdentification136, False)

	@PmryPlcOfDpst.deleter
	def PmryPlcOfDpst(self):
		del self._PmryPlcOfDpst
		self._PmryPlcOfDpst = base_types.UninitialisedField(self, 'PmryPlcOfDpst', PartyIdentification136, False)

	@property
	def PmtSts(self):
		return self._PmtSts

	@PmtSts.setter
	def PmtSts(self, value):
		self._PmtSts = value if value is not None else base_types.UninitialisedField(self, 'PmtSts', SecuritiesPaymentStatus5Choice, False)

	@PmtSts.deleter
	def PmtSts(self):
		del self._PmtSts
		self._PmtSts = base_types.UninitialisedField(self, 'PmtSts', SecuritiesPaymentStatus5Choice, False)

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if value is not None else base_types.UninitialisedField(self, 'PngAgt', Organisation38, False)

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = base_types.UninitialisedField(self, 'PngAgt', Organisation38, False)

	@property
	def PoolNb(self):
		return self._PoolNb

	@PoolNb.setter
	def PoolNb(self, value):
		self._PoolNb = value if value is not None else base_types.UninitialisedField(self, 'PoolNb', Max15NumericText, False)

	@PoolNb.deleter
	def PoolNb(self):
		del self._PoolNb
		self._PoolNb = base_types.UninitialisedField(self, 'PoolNb', Max15NumericText, False)

	@property
	def PosLmt(self):
		return self._PosLmt

	@PosLmt.setter
	def PosLmt(self, value):
		self._PosLmt = value if value is not None else base_types.UninitialisedField(self, 'PosLmt', FinancialInstrumentQuantity1Choice, False)

	@PosLmt.deleter
	def PosLmt(self):
		del self._PosLmt
		self._PosLmt = base_types.UninitialisedField(self, 'PosLmt', FinancialInstrumentQuantity1Choice, False)

	@property
	def PrncplPngAgt(self):
		return self._PrncplPngAgt

	@PrncplPngAgt.setter
	def PrncplPngAgt(self, value):
		self._PrncplPngAgt = value if value is not None else base_types.UninitialisedField(self, 'PrncplPngAgt', Organisation38, False)

	@PrncplPngAgt.deleter
	def PrncplPngAgt(self):
		del self._PrncplPngAgt
		self._PrncplPngAgt = base_types.UninitialisedField(self, 'PrncplPngAgt', Organisation38, False)

	@property
	def PrvtPlcmnt(self):
		return self._PrvtPlcmnt

	@PrvtPlcmnt.setter
	def PrvtPlcmnt(self, value):
		self._PrvtPlcmnt = value if value is not None else base_types.UninitialisedField(self, 'PrvtPlcmnt', YesNoIndicator, False)

	@PrvtPlcmnt.deleter
	def PrvtPlcmnt(self):
		del self._PrvtPlcmnt
		self._PrvtPlcmnt = base_types.UninitialisedField(self, 'PrvtPlcmnt', YesNoIndicator, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max256Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max256Text, False)

	@property
	def PutTp(self):
		return self._PutTp

	@PutTp.setter
	def PutTp(self, value):
		self._PutTp = value if value is not None else base_types.UninitialisedField(self, 'PutTp', PutType3Choice, False)

	@PutTp.deleter
	def PutTp(self):
		del self._PutTp
		self._PutTp = base_types.UninitialisedField(self, 'PutTp', PutType3Choice, False)

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if value is not None else base_types.UninitialisedField(self, 'RcrdDt', ISODateTime, False)

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = base_types.UninitialisedField(self, 'RcrdDt', ISODateTime, False)

	@property
	def RedPmtCcy(self):
		return self._RedPmtCcy

	@RedPmtCcy.setter
	def RedPmtCcy(self, value):
		self._RedPmtCcy = value if value is not None else base_types.UninitialisedField(self, 'RedPmtCcy', ActiveCurrencyCode, False)

	@RedPmtCcy.deleter
	def RedPmtCcy(self):
		del self._RedPmtCcy
		self._RedPmtCcy = base_types.UninitialisedField(self, 'RedPmtCcy', ActiveCurrencyCode, False)

	@property
	def RedTp(self):
		return self._RedTp

	@RedTp.setter
	def RedTp(self, value):
		self._RedTp = value if value is not None else base_types.UninitialisedField(self, 'RedTp', MaturityRedemptionType3Choice, False)

	@RedTp.deleter
	def RedTp(self):
		del self._RedTp
		self._RedTp = base_types.UninitialisedField(self, 'RedTp', MaturityRedemptionType3Choice, False)

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if value is not None else base_types.UninitialisedField(self, 'Rstrctn', SecurityRestriction3, True)

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = base_types.UninitialisedField(self, 'Rstrctn', SecurityRestriction3, True)

	@property
	def SctyCSDLk(self):
		return self._SctyCSDLk

	@SctyCSDLk.setter
	def SctyCSDLk(self, value):
		self._SctyCSDLk = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLk', SecurityCSDLink7, True)

	@SctyCSDLk.deleter
	def SctyCSDLk(self):
		del self._SctyCSDLk
		self._SctyCSDLk = base_types.UninitialisedField(self, 'SctyCSDLk', SecurityCSDLink7, True)

	@property
	def SctySts(self):
		return self._SctySts

	@SctySts.setter
	def SctySts(self, value):
		self._SctySts = value if value is not None else base_types.UninitialisedField(self, 'SctySts', SecurityStatus3Choice, False)

	@SctySts.deleter
	def SctySts(self):
		del self._SctySts
		self._SctySts = base_types.UninitialisedField(self, 'SctySts', SecurityStatus3Choice, False)

	@property
	def SprdAndBchmkCrv(self):
		return self._SprdAndBchmkCrv

	@SprdAndBchmkCrv.setter
	def SprdAndBchmkCrv(self, value):
		self._SprdAndBchmkCrv = value if value is not None else base_types.UninitialisedField(self, 'SprdAndBchmkCrv', BenchmarkCurve6, True)

	@SprdAndBchmkCrv.deleter
	def SprdAndBchmkCrv(self):
		del self._SprdAndBchmkCrv
		self._SprdAndBchmkCrv = base_types.UninitialisedField(self, 'SprdAndBchmkCrv', BenchmarkCurve6, True)

	@property
	def SrNb(self):
		return self._SrNb

	@SrNb.setter
	def SrNb(self, value):
		self._SrNb = value if value is not None else base_types.UninitialisedField(self, 'SrNb', Max16Text, False)

	@SrNb.deleter
	def SrNb(self):
		del self._SrNb
		self._SrNb = base_types.UninitialisedField(self, 'SrNb', Max16Text, False)

	@property
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if value is not None else base_types.UninitialisedField(self, 'SttlmInf', SettlementInformation17, True)

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = base_types.UninitialisedField(self, 'SttlmInf', SettlementInformation17, True)

	@property
	def TEFRARule(self):
		return self._TEFRARule

	@TEFRARule.setter
	def TEFRARule(self, value):
		self._TEFRARule = value if value is not None else base_types.UninitialisedField(self, 'TEFRARule', TEFRARules3Choice, False)

	@TEFRARule.deleter
	def TEFRARule(self):
		del self._TEFRARule
		self._TEFRARule = base_types.UninitialisedField(self, 'TEFRARule', TEFRARules3Choice, False)

	@property
	def TaxLotNb(self):
		return self._TaxLotNb

	@TaxLotNb.setter
	def TaxLotNb(self, value):
		self._TaxLotNb = value if value is not None else base_types.UninitialisedField(self, 'TaxLotNb', Max15NumericText, False)

	@TaxLotNb.deleter
	def TaxLotNb(self):
		del self._TaxLotNb
		self._TaxLotNb = base_types.UninitialisedField(self, 'TaxLotNb', Max15NumericText, False)

	@property
	def TradgMkt(self):
		return self._TradgMkt

	@TradgMkt.setter
	def TradgMkt(self, value):
		self._TradgMkt = value if value is not None else base_types.UninitialisedField(self, 'TradgMkt', TradingParameters2, True)

	@TradgMkt.deleter
	def TradgMkt(self):
		del self._TradgMkt
		self._TradgMkt = base_types.UninitialisedField(self, 'TradgMkt', TradingParameters2, True)

	@property
	def TradgMtd(self):
		return self._TradgMtd

	@TradgMtd.setter
	def TradgMtd(self, value):
		self._TradgMtd = value if value is not None else base_types.UninitialisedField(self, 'TradgMtd', UnitOrFaceAmount1Choice, False)

	@TradgMtd.deleter
	def TradgMtd(self):
		del self._TradgMtd
		self._TradgMtd = base_types.UninitialisedField(self, 'TradgMtd', UnitOrFaceAmount1Choice, False)

	@property
	def UndrlygRsk(self):
		return self._UndrlygRsk

	@UndrlygRsk.setter
	def UndrlygRsk(self, value):
		self._UndrlygRsk = value if value is not None else base_types.UninitialisedField(self, 'UndrlygRsk', Organisation38, False)

	@UndrlygRsk.deleter
	def UndrlygRsk(self):
		del self._UndrlygRsk
		self._UndrlygRsk = base_types.UninitialisedField(self, 'UndrlygRsk', Organisation38, False)

	@property
	def WhldgTaxRgm(self):
		return self._WhldgTaxRgm

	@WhldgTaxRgm.setter
	def WhldgTaxRgm(self, value):
		self._WhldgTaxRgm = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRgm', SecurityWithHoldingTax1, True)

	@WhldgTaxRgm.deleter
	def WhldgTaxRgm(self):
		del self._WhldgTaxRgm
		self._WhldgTaxRgm = base_types.UninitialisedField(self, 'WhldgTaxRgm', SecurityWithHoldingTax1, True)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AftrXchgPhysForm', type=InitialPhysicalForm3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallTp', type=CallType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clss', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonSfkpr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnfdtl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPrd', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsRatioDnmtr', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsRatioNmrtr', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnAttchdNb', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctNm', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctVrsnNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmForm', type=FinancialInstrumentForm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmIdVldty', type=FinancialInstrumentIdentificationValidity3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmNm', type=FinancialInstrumentName2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FngbInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlPhysForm', type=InitialPhysicalForm4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issnc', type=Issuance6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LeadMgr', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRstrctns', type=LegalRestrictions4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NearTermPosLmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
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
		base_types.FieldEntry(name='SctyCSDLk', type=SecurityCSDLink7, min=0, max=None, mutex_group=None, array=True),
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