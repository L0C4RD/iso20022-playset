# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import AnnualChargePaymentType1Code
from . import DistributionPolicy1Code
from . import DividendPolicy1Code
from . import EUSavingsDirective1Code
from . import EventFrequency5Code
from . import ISODate
from . import TargetMarket1Code
from . import YesNoIndicator

class FinancialInstrument96(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Authrsd", "_BckEndLd", "_ClsdEndFnd", "_DmtrlsdBrScties", "_DmtrlsdRegdScties", "_DstrbtnPlcy", "_DvddFrqcy", "_DvddPlcy", "_EUSvgsDrctv", "_Equlstn", "_FndEndDt", "_FrntEndLd", "_InitlOfferEndDt", "_LnchDt", "_MayBeTermntdEarly", "_MgmtFeeSrc", "_MtrtyDt", "_PhysBrScties", "_PhysRegdScties", "_PrfrmncFee", "_RDRCmplnt", "_RinvstmtFrqcy", "_SspnsnEndDt", "_SspnsnStartDt", "_SwtchFee", "_TaxEffcntPdctElgbl", "_TermntnDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def Authrsd(self):
		return self._Authrsd

	@Authrsd.setter
	def Authrsd(self, value):
		self._Authrsd = value if value is not None else base_types.UninitialisedField(self, 'Authrsd', YesNoIndicator, False)

	@Authrsd.deleter
	def Authrsd(self):
		del self._Authrsd
		self._Authrsd = base_types.UninitialisedField(self, 'Authrsd', YesNoIndicator, False)

	@property
	def BckEndLd(self):
		return self._BckEndLd

	@BckEndLd.setter
	def BckEndLd(self, value):
		self._BckEndLd = value if value is not None else base_types.UninitialisedField(self, 'BckEndLd', YesNoIndicator, False)

	@BckEndLd.deleter
	def BckEndLd(self):
		del self._BckEndLd
		self._BckEndLd = base_types.UninitialisedField(self, 'BckEndLd', YesNoIndicator, False)

	@property
	def ClsdEndFnd(self):
		return self._ClsdEndFnd

	@ClsdEndFnd.setter
	def ClsdEndFnd(self, value):
		self._ClsdEndFnd = value if value is not None else base_types.UninitialisedField(self, 'ClsdEndFnd', YesNoIndicator, False)

	@ClsdEndFnd.deleter
	def ClsdEndFnd(self):
		del self._ClsdEndFnd
		self._ClsdEndFnd = base_types.UninitialisedField(self, 'ClsdEndFnd', YesNoIndicator, False)

	@property
	def DmtrlsdBrScties(self):
		return self._DmtrlsdBrScties

	@DmtrlsdBrScties.setter
	def DmtrlsdBrScties(self, value):
		self._DmtrlsdBrScties = value if value is not None else base_types.UninitialisedField(self, 'DmtrlsdBrScties', YesNoIndicator, False)

	@DmtrlsdBrScties.deleter
	def DmtrlsdBrScties(self):
		del self._DmtrlsdBrScties
		self._DmtrlsdBrScties = base_types.UninitialisedField(self, 'DmtrlsdBrScties', YesNoIndicator, False)

	@property
	def DmtrlsdRegdScties(self):
		return self._DmtrlsdRegdScties

	@DmtrlsdRegdScties.setter
	def DmtrlsdRegdScties(self, value):
		self._DmtrlsdRegdScties = value if value is not None else base_types.UninitialisedField(self, 'DmtrlsdRegdScties', YesNoIndicator, False)

	@DmtrlsdRegdScties.deleter
	def DmtrlsdRegdScties(self):
		del self._DmtrlsdRegdScties
		self._DmtrlsdRegdScties = base_types.UninitialisedField(self, 'DmtrlsdRegdScties', YesNoIndicator, False)

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if value is not None else base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@property
	def DvddFrqcy(self):
		return self._DvddFrqcy

	@DvddFrqcy.setter
	def DvddFrqcy(self, value):
		self._DvddFrqcy = value if value is not None else base_types.UninitialisedField(self, 'DvddFrqcy', EventFrequency5Code, False)

	@DvddFrqcy.deleter
	def DvddFrqcy(self):
		del self._DvddFrqcy
		self._DvddFrqcy = base_types.UninitialisedField(self, 'DvddFrqcy', EventFrequency5Code, False)

	@property
	def DvddPlcy(self):
		return self._DvddPlcy

	@DvddPlcy.setter
	def DvddPlcy(self, value):
		self._DvddPlcy = value if value is not None else base_types.UninitialisedField(self, 'DvddPlcy', DividendPolicy1Code, False)

	@DvddPlcy.deleter
	def DvddPlcy(self):
		del self._DvddPlcy
		self._DvddPlcy = base_types.UninitialisedField(self, 'DvddPlcy', DividendPolicy1Code, False)

	@property
	def EUSvgsDrctv(self):
		return self._EUSvgsDrctv

	@EUSvgsDrctv.setter
	def EUSvgsDrctv(self, value):
		self._EUSvgsDrctv = value if value is not None else base_types.UninitialisedField(self, 'EUSvgsDrctv', EUSavingsDirective1Code, False)

	@EUSvgsDrctv.deleter
	def EUSvgsDrctv(self):
		del self._EUSvgsDrctv
		self._EUSvgsDrctv = base_types.UninitialisedField(self, 'EUSvgsDrctv', EUSavingsDirective1Code, False)

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if value is not None else base_types.UninitialisedField(self, 'Equlstn', YesNoIndicator, False)

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = base_types.UninitialisedField(self, 'Equlstn', YesNoIndicator, False)

	@property
	def FndEndDt(self):
		return self._FndEndDt

	@FndEndDt.setter
	def FndEndDt(self, value):
		self._FndEndDt = value if value is not None else base_types.UninitialisedField(self, 'FndEndDt', ISODate, False)

	@FndEndDt.deleter
	def FndEndDt(self):
		del self._FndEndDt
		self._FndEndDt = base_types.UninitialisedField(self, 'FndEndDt', ISODate, False)

	@property
	def FrntEndLd(self):
		return self._FrntEndLd

	@FrntEndLd.setter
	def FrntEndLd(self, value):
		self._FrntEndLd = value if value is not None else base_types.UninitialisedField(self, 'FrntEndLd', YesNoIndicator, False)

	@FrntEndLd.deleter
	def FrntEndLd(self):
		del self._FrntEndLd
		self._FrntEndLd = base_types.UninitialisedField(self, 'FrntEndLd', YesNoIndicator, False)

	@property
	def InitlOfferEndDt(self):
		return self._InitlOfferEndDt

	@InitlOfferEndDt.setter
	def InitlOfferEndDt(self, value):
		self._InitlOfferEndDt = value if value is not None else base_types.UninitialisedField(self, 'InitlOfferEndDt', ISODate, False)

	@InitlOfferEndDt.deleter
	def InitlOfferEndDt(self):
		del self._InitlOfferEndDt
		self._InitlOfferEndDt = base_types.UninitialisedField(self, 'InitlOfferEndDt', ISODate, False)

	@property
	def LnchDt(self):
		return self._LnchDt

	@LnchDt.setter
	def LnchDt(self, value):
		self._LnchDt = value if value is not None else base_types.UninitialisedField(self, 'LnchDt', ISODate, False)

	@LnchDt.deleter
	def LnchDt(self):
		del self._LnchDt
		self._LnchDt = base_types.UninitialisedField(self, 'LnchDt', ISODate, False)

	@property
	def MayBeTermntdEarly(self):
		return self._MayBeTermntdEarly

	@MayBeTermntdEarly.setter
	def MayBeTermntdEarly(self, value):
		self._MayBeTermntdEarly = value if value is not None else base_types.UninitialisedField(self, 'MayBeTermntdEarly', TargetMarket1Code, False)

	@MayBeTermntdEarly.deleter
	def MayBeTermntdEarly(self):
		del self._MayBeTermntdEarly
		self._MayBeTermntdEarly = base_types.UninitialisedField(self, 'MayBeTermntdEarly', TargetMarket1Code, False)

	@property
	def MgmtFeeSrc(self):
		return self._MgmtFeeSrc

	@MgmtFeeSrc.setter
	def MgmtFeeSrc(self, value):
		self._MgmtFeeSrc = value if value is not None else base_types.UninitialisedField(self, 'MgmtFeeSrc', AnnualChargePaymentType1Code, False)

	@MgmtFeeSrc.deleter
	def MgmtFeeSrc(self):
		del self._MgmtFeeSrc
		self._MgmtFeeSrc = base_types.UninitialisedField(self, 'MgmtFeeSrc', AnnualChargePaymentType1Code, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def PhysBrScties(self):
		return self._PhysBrScties

	@PhysBrScties.setter
	def PhysBrScties(self, value):
		self._PhysBrScties = value if value is not None else base_types.UninitialisedField(self, 'PhysBrScties', YesNoIndicator, False)

	@PhysBrScties.deleter
	def PhysBrScties(self):
		del self._PhysBrScties
		self._PhysBrScties = base_types.UninitialisedField(self, 'PhysBrScties', YesNoIndicator, False)

	@property
	def PhysRegdScties(self):
		return self._PhysRegdScties

	@PhysRegdScties.setter
	def PhysRegdScties(self, value):
		self._PhysRegdScties = value if value is not None else base_types.UninitialisedField(self, 'PhysRegdScties', YesNoIndicator, False)

	@PhysRegdScties.deleter
	def PhysRegdScties(self):
		del self._PhysRegdScties
		self._PhysRegdScties = base_types.UninitialisedField(self, 'PhysRegdScties', YesNoIndicator, False)

	@property
	def PrfrmncFee(self):
		return self._PrfrmncFee

	@PrfrmncFee.setter
	def PrfrmncFee(self, value):
		self._PrfrmncFee = value if value is not None else base_types.UninitialisedField(self, 'PrfrmncFee', YesNoIndicator, False)

	@PrfrmncFee.deleter
	def PrfrmncFee(self):
		del self._PrfrmncFee
		self._PrfrmncFee = base_types.UninitialisedField(self, 'PrfrmncFee', YesNoIndicator, False)

	@property
	def RDRCmplnt(self):
		return self._RDRCmplnt

	@RDRCmplnt.setter
	def RDRCmplnt(self, value):
		self._RDRCmplnt = value if value is not None else base_types.UninitialisedField(self, 'RDRCmplnt', YesNoIndicator, False)

	@RDRCmplnt.deleter
	def RDRCmplnt(self):
		del self._RDRCmplnt
		self._RDRCmplnt = base_types.UninitialisedField(self, 'RDRCmplnt', YesNoIndicator, False)

	@property
	def RinvstmtFrqcy(self):
		return self._RinvstmtFrqcy

	@RinvstmtFrqcy.setter
	def RinvstmtFrqcy(self, value):
		self._RinvstmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtFrqcy', EventFrequency5Code, False)

	@RinvstmtFrqcy.deleter
	def RinvstmtFrqcy(self):
		del self._RinvstmtFrqcy
		self._RinvstmtFrqcy = base_types.UninitialisedField(self, 'RinvstmtFrqcy', EventFrequency5Code, False)

	@property
	def SspnsnEndDt(self):
		return self._SspnsnEndDt

	@SspnsnEndDt.setter
	def SspnsnEndDt(self, value):
		self._SspnsnEndDt = value if value is not None else base_types.UninitialisedField(self, 'SspnsnEndDt', ISODate, False)

	@SspnsnEndDt.deleter
	def SspnsnEndDt(self):
		del self._SspnsnEndDt
		self._SspnsnEndDt = base_types.UninitialisedField(self, 'SspnsnEndDt', ISODate, False)

	@property
	def SspnsnStartDt(self):
		return self._SspnsnStartDt

	@SspnsnStartDt.setter
	def SspnsnStartDt(self, value):
		self._SspnsnStartDt = value if value is not None else base_types.UninitialisedField(self, 'SspnsnStartDt', ISODate, False)

	@SspnsnStartDt.deleter
	def SspnsnStartDt(self):
		del self._SspnsnStartDt
		self._SspnsnStartDt = base_types.UninitialisedField(self, 'SspnsnStartDt', ISODate, False)

	@property
	def SwtchFee(self):
		return self._SwtchFee

	@SwtchFee.setter
	def SwtchFee(self, value):
		self._SwtchFee = value if value is not None else base_types.UninitialisedField(self, 'SwtchFee', YesNoIndicator, False)

	@SwtchFee.deleter
	def SwtchFee(self):
		del self._SwtchFee
		self._SwtchFee = base_types.UninitialisedField(self, 'SwtchFee', YesNoIndicator, False)

	@property
	def TaxEffcntPdctElgbl(self):
		return self._TaxEffcntPdctElgbl

	@TaxEffcntPdctElgbl.setter
	def TaxEffcntPdctElgbl(self, value):
		self._TaxEffcntPdctElgbl = value if value is not None else base_types.UninitialisedField(self, 'TaxEffcntPdctElgbl', YesNoIndicator, False)

	@TaxEffcntPdctElgbl.deleter
	def TaxEffcntPdctElgbl(self):
		del self._TaxEffcntPdctElgbl
		self._TaxEffcntPdctElgbl = base_types.UninitialisedField(self, 'TaxEffcntPdctElgbl', YesNoIndicator, False)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', ISODate, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Authrsd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BckEndLd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsdEndFnd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdBrScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdRegdScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddPlcy', type=DividendPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUSvgsDrctv', type=EUSavingsDirective1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrntEndLd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlOfferEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnchDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MayBeTermntdEarly', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MgmtFeeSrc', type=AnnualChargePaymentType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysBrScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysRegdScties', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrfrmncFee', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RDRCmplnt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtFrqcy', type=EventFrequency5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspnsnEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspnsnStartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchFee', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxEffcntPdctElgbl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))