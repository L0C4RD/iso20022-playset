from . import base_types
import ISODate
import YesNoIndicator
import AdditionalInformation15
import DividendPolicy1Code
import EUSavingsDirective1Code
import AnnualChargePaymentType1Code
import DistributionPolicy1Code
import TargetMarket1Code
import EventFrequency5Code

class FinancialInstrument96(base_types._BaseFieldType):

	__slots__ = ["_SspnsnEndDt", "_DmtrlsdRegdScties", "_DmtrlsdBrScties", "_MtrtyDt", "_FrntEndLd", "_PhysBrScties", "_RDRCmplnt", "_LnchDt", "_TaxEffcntPdctElgbl", "_AddtlInf", "_InitlOfferEndDt", "_SwtchFee", "_ClsdEndFnd", "_FndEndDt", "_MayBeTermntdEarly", "_RinvstmtFrqcy", "_Authrsd", "_PhysRegdScties", "_DstrbtnPlcy", "_PrfrmncFee", "_DvddPlcy", "_EUSvgsDrctv", "_SspnsnStartDt", "_BckEndLd", "_MgmtFeeSrc", "_Equlstn", "_TermntnDt", "_DvddFrqcy"]
	@property
	def SspnsnEndDt(self):
		return self._SspnsnEndDt

	@SspnsnEndDt.setter
	def SspnsnEndDt(self, value):
		self._SspnsnEndDt = value if type(value) != auto else self.make_default("SspnsnEndDt")

	@SspnsnEndDt.deleter
	def SspnsnEndDt(self):
		del self._SspnsnEndDt
		self._SspnsnEndDt = None

	@property
	def DmtrlsdRegdScties(self):
		return self._DmtrlsdRegdScties

	@DmtrlsdRegdScties.setter
	def DmtrlsdRegdScties(self, value):
		self._DmtrlsdRegdScties = value if type(value) != auto else self.make_default("DmtrlsdRegdScties")

	@DmtrlsdRegdScties.deleter
	def DmtrlsdRegdScties(self):
		del self._DmtrlsdRegdScties
		self._DmtrlsdRegdScties = None

	@property
	def DmtrlsdBrScties(self):
		return self._DmtrlsdBrScties

	@DmtrlsdBrScties.setter
	def DmtrlsdBrScties(self, value):
		self._DmtrlsdBrScties = value if type(value) != auto else self.make_default("DmtrlsdBrScties")

	@DmtrlsdBrScties.deleter
	def DmtrlsdBrScties(self):
		del self._DmtrlsdBrScties
		self._DmtrlsdBrScties = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def FrntEndLd(self):
		return self._FrntEndLd

	@FrntEndLd.setter
	def FrntEndLd(self, value):
		self._FrntEndLd = value if type(value) != auto else self.make_default("FrntEndLd")

	@FrntEndLd.deleter
	def FrntEndLd(self):
		del self._FrntEndLd
		self._FrntEndLd = None

	@property
	def PhysBrScties(self):
		return self._PhysBrScties

	@PhysBrScties.setter
	def PhysBrScties(self, value):
		self._PhysBrScties = value if type(value) != auto else self.make_default("PhysBrScties")

	@PhysBrScties.deleter
	def PhysBrScties(self):
		del self._PhysBrScties
		self._PhysBrScties = None

	@property
	def RDRCmplnt(self):
		return self._RDRCmplnt

	@RDRCmplnt.setter
	def RDRCmplnt(self, value):
		self._RDRCmplnt = value if type(value) != auto else self.make_default("RDRCmplnt")

	@RDRCmplnt.deleter
	def RDRCmplnt(self):
		del self._RDRCmplnt
		self._RDRCmplnt = None

	@property
	def LnchDt(self):
		return self._LnchDt

	@LnchDt.setter
	def LnchDt(self, value):
		self._LnchDt = value if type(value) != auto else self.make_default("LnchDt")

	@LnchDt.deleter
	def LnchDt(self):
		del self._LnchDt
		self._LnchDt = None

	@property
	def TaxEffcntPdctElgbl(self):
		return self._TaxEffcntPdctElgbl

	@TaxEffcntPdctElgbl.setter
	def TaxEffcntPdctElgbl(self, value):
		self._TaxEffcntPdctElgbl = value if type(value) != auto else self.make_default("TaxEffcntPdctElgbl")

	@TaxEffcntPdctElgbl.deleter
	def TaxEffcntPdctElgbl(self):
		del self._TaxEffcntPdctElgbl
		self._TaxEffcntPdctElgbl = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def InitlOfferEndDt(self):
		return self._InitlOfferEndDt

	@InitlOfferEndDt.setter
	def InitlOfferEndDt(self, value):
		self._InitlOfferEndDt = value if type(value) != auto else self.make_default("InitlOfferEndDt")

	@InitlOfferEndDt.deleter
	def InitlOfferEndDt(self):
		del self._InitlOfferEndDt
		self._InitlOfferEndDt = None

	@property
	def SwtchFee(self):
		return self._SwtchFee

	@SwtchFee.setter
	def SwtchFee(self, value):
		self._SwtchFee = value if type(value) != auto else self.make_default("SwtchFee")

	@SwtchFee.deleter
	def SwtchFee(self):
		del self._SwtchFee
		self._SwtchFee = None

	@property
	def ClsdEndFnd(self):
		return self._ClsdEndFnd

	@ClsdEndFnd.setter
	def ClsdEndFnd(self, value):
		self._ClsdEndFnd = value if type(value) != auto else self.make_default("ClsdEndFnd")

	@ClsdEndFnd.deleter
	def ClsdEndFnd(self):
		del self._ClsdEndFnd
		self._ClsdEndFnd = None

	@property
	def FndEndDt(self):
		return self._FndEndDt

	@FndEndDt.setter
	def FndEndDt(self, value):
		self._FndEndDt = value if type(value) != auto else self.make_default("FndEndDt")

	@FndEndDt.deleter
	def FndEndDt(self):
		del self._FndEndDt
		self._FndEndDt = None

	@property
	def MayBeTermntdEarly(self):
		return self._MayBeTermntdEarly

	@MayBeTermntdEarly.setter
	def MayBeTermntdEarly(self, value):
		self._MayBeTermntdEarly = value if type(value) != auto else self.make_default("MayBeTermntdEarly")

	@MayBeTermntdEarly.deleter
	def MayBeTermntdEarly(self):
		del self._MayBeTermntdEarly
		self._MayBeTermntdEarly = None

	@property
	def RinvstmtFrqcy(self):
		return self._RinvstmtFrqcy

	@RinvstmtFrqcy.setter
	def RinvstmtFrqcy(self, value):
		self._RinvstmtFrqcy = value if type(value) != auto else self.make_default("RinvstmtFrqcy")

	@RinvstmtFrqcy.deleter
	def RinvstmtFrqcy(self):
		del self._RinvstmtFrqcy
		self._RinvstmtFrqcy = None

	@property
	def Authrsd(self):
		return self._Authrsd

	@Authrsd.setter
	def Authrsd(self, value):
		self._Authrsd = value if type(value) != auto else self.make_default("Authrsd")

	@Authrsd.deleter
	def Authrsd(self):
		del self._Authrsd
		self._Authrsd = None

	@property
	def PhysRegdScties(self):
		return self._PhysRegdScties

	@PhysRegdScties.setter
	def PhysRegdScties(self, value):
		self._PhysRegdScties = value if type(value) != auto else self.make_default("PhysRegdScties")

	@PhysRegdScties.deleter
	def PhysRegdScties(self):
		del self._PhysRegdScties
		self._PhysRegdScties = None

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if type(value) != auto else self.make_default("DstrbtnPlcy")

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = None

	@property
	def PrfrmncFee(self):
		return self._PrfrmncFee

	@PrfrmncFee.setter
	def PrfrmncFee(self, value):
		self._PrfrmncFee = value if type(value) != auto else self.make_default("PrfrmncFee")

	@PrfrmncFee.deleter
	def PrfrmncFee(self):
		del self._PrfrmncFee
		self._PrfrmncFee = None

	@property
	def DvddPlcy(self):
		return self._DvddPlcy

	@DvddPlcy.setter
	def DvddPlcy(self, value):
		self._DvddPlcy = value if type(value) != auto else self.make_default("DvddPlcy")

	@DvddPlcy.deleter
	def DvddPlcy(self):
		del self._DvddPlcy
		self._DvddPlcy = None

	@property
	def EUSvgsDrctv(self):
		return self._EUSvgsDrctv

	@EUSvgsDrctv.setter
	def EUSvgsDrctv(self, value):
		self._EUSvgsDrctv = value if type(value) != auto else self.make_default("EUSvgsDrctv")

	@EUSvgsDrctv.deleter
	def EUSvgsDrctv(self):
		del self._EUSvgsDrctv
		self._EUSvgsDrctv = None

	@property
	def SspnsnStartDt(self):
		return self._SspnsnStartDt

	@SspnsnStartDt.setter
	def SspnsnStartDt(self, value):
		self._SspnsnStartDt = value if type(value) != auto else self.make_default("SspnsnStartDt")

	@SspnsnStartDt.deleter
	def SspnsnStartDt(self):
		del self._SspnsnStartDt
		self._SspnsnStartDt = None

	@property
	def BckEndLd(self):
		return self._BckEndLd

	@BckEndLd.setter
	def BckEndLd(self, value):
		self._BckEndLd = value if type(value) != auto else self.make_default("BckEndLd")

	@BckEndLd.deleter
	def BckEndLd(self):
		del self._BckEndLd
		self._BckEndLd = None

	@property
	def MgmtFeeSrc(self):
		return self._MgmtFeeSrc

	@MgmtFeeSrc.setter
	def MgmtFeeSrc(self, value):
		self._MgmtFeeSrc = value if type(value) != auto else self.make_default("MgmtFeeSrc")

	@MgmtFeeSrc.deleter
	def MgmtFeeSrc(self):
		del self._MgmtFeeSrc
		self._MgmtFeeSrc = None

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if type(value) != auto else self.make_default("Equlstn")

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def DvddFrqcy(self):
		return self._DvddFrqcy

	@DvddFrqcy.setter
	def DvddFrqcy(self, value):
		self._DvddFrqcy = value if type(value) != auto else self.make_default("DvddFrqcy")

	@DvddFrqcy.deleter
	def DvddFrqcy(self):
		del self._DvddFrqcy
		self._DvddFrqcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SspnsnEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdRegdScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdBrScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrntEndLd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysBrScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RDRCmplnt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnchDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxEffcntPdctElgbl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitlOfferEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchFee', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsdEndFnd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MayBeTermntdEarly', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authrsd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysRegdScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrfrmncFee', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddPlcy', type=DividendPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUSvgsDrctv', type=EUSavingsDirective1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspnsnStartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BckEndLd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MgmtFeeSrc', type=AnnualChargePaymentType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
	))

