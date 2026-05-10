from . import base_types
from ._AccountingStatus1Choice import AccountingStatus1Choice
from ._AdditiononalInformation13 import AdditiononalInformation13
from ._CRSForm1Choice import CRSForm1Choice
from ._CRSStatus4 import CRSStatus4
from ._CommunicationAddress6 import CommunicationAddress6
from ._CompanyLink1Choice import CompanyLink1Choice
from ._CountryAndResidentialStatusType2 import CountryAndResidentialStatusType2
from ._DateAndAmount1 import DateAndAmount1
from ._FATCAForm1Choice import FATCAForm1Choice
from ._FATCAStatus2 import FATCAStatus2
from ._GenericIdentification82 import GenericIdentification82
from ._ISODate import ISODate
from ._LanguageCode import LanguageCode
from ._MailType1Choice import MailType1Choice
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._MiFIDClassification1 import MiFIDClassification1
from ._MoneyLaunderingCheck1Choice import MoneyLaunderingCheck1Choice
from ._Notification2 import Notification2
from ._OwnershipBeneficiaryRate1 import OwnershipBeneficiaryRate1
from ._Party47Choice import Party47Choice
from ._PartyProfileInformation5 import PartyProfileInformation5
from ._RegulatoryInformation1 import RegulatoryInformation1
from ._TaxExemptionReason2Choice import TaxExemptionReason2Choice
from ._TaxReporting3 import TaxReporting3
from ._YesNoIndicator import YesNoIndicator

class InvestmentAccountOwnershipInformation16(base_types._BaseFieldType):

	__slots__ = ["_AcctgSts", "_AddtlInf", "_AddtlRgltryInf", "_CRSFormTp", "_CRSRptgDt", "_CRSSts", "_ClntId", "_CpnyLk", "_CtrlgPty", "_CtryAndResdtlSts", "_ElctrncMlngSvcRef", "_EqtyVal", "_FATCAFormTp", "_FATCARptgDt", "_FATCASts", "_FsclXmptn", "_InvstrPrflVldtn", "_Lang", "_MailTp", "_MiFIDClssfctn", "_MntryWlth", "_MnyLndrgChck", "_Ntfctn", "_OthrId", "_OwnrshBnfcryRate", "_PmryComAdr", "_Pty", "_ScndryComAdr", "_SgntryRghtInd", "_TaxRptg", "_TaxXmptn", "_WorkgCptl"]
	@property
	def AcctgSts(self):
		return self._AcctgSts

	@AcctgSts.setter
	def AcctgSts(self, value):
		self._AcctgSts = value if type(value) != base_types.auto else self.make_default("AcctgSts")

	@AcctgSts.deleter
	def AcctgSts(self):
		del self._AcctgSts
		self._AcctgSts = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AddtlRgltryInf(self):
		return self._AddtlRgltryInf

	@AddtlRgltryInf.setter
	def AddtlRgltryInf(self, value):
		self._AddtlRgltryInf = value if type(value) != base_types.auto else self.make_default("AddtlRgltryInf")

	@AddtlRgltryInf.deleter
	def AddtlRgltryInf(self):
		del self._AddtlRgltryInf
		self._AddtlRgltryInf = None

	@property
	def CRSFormTp(self):
		return self._CRSFormTp

	@CRSFormTp.setter
	def CRSFormTp(self, value):
		self._CRSFormTp = value if type(value) != base_types.auto else self.make_default("CRSFormTp")

	@CRSFormTp.deleter
	def CRSFormTp(self):
		del self._CRSFormTp
		self._CRSFormTp = None

	@property
	def CRSRptgDt(self):
		return self._CRSRptgDt

	@CRSRptgDt.setter
	def CRSRptgDt(self, value):
		self._CRSRptgDt = value if type(value) != base_types.auto else self.make_default("CRSRptgDt")

	@CRSRptgDt.deleter
	def CRSRptgDt(self):
		del self._CRSRptgDt
		self._CRSRptgDt = None

	@property
	def CRSSts(self):
		return self._CRSSts

	@CRSSts.setter
	def CRSSts(self, value):
		self._CRSSts = value if type(value) != base_types.auto else self.make_default("CRSSts")

	@CRSSts.deleter
	def CRSSts(self):
		del self._CRSSts
		self._CRSSts = None

	@property
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if type(value) != base_types.auto else self.make_default("ClntId")

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = None

	@property
	def CpnyLk(self):
		return self._CpnyLk

	@CpnyLk.setter
	def CpnyLk(self, value):
		self._CpnyLk = value if type(value) != base_types.auto else self.make_default("CpnyLk")

	@CpnyLk.deleter
	def CpnyLk(self):
		del self._CpnyLk
		self._CpnyLk = None

	@property
	def CtrlgPty(self):
		return self._CtrlgPty

	@CtrlgPty.setter
	def CtrlgPty(self, value):
		self._CtrlgPty = value if type(value) != base_types.auto else self.make_default("CtrlgPty")

	@CtrlgPty.deleter
	def CtrlgPty(self):
		del self._CtrlgPty
		self._CtrlgPty = None

	@property
	def CtryAndResdtlSts(self):
		return self._CtryAndResdtlSts

	@CtryAndResdtlSts.setter
	def CtryAndResdtlSts(self, value):
		self._CtryAndResdtlSts = value if type(value) != base_types.auto else self.make_default("CtryAndResdtlSts")

	@CtryAndResdtlSts.deleter
	def CtryAndResdtlSts(self):
		del self._CtryAndResdtlSts
		self._CtryAndResdtlSts = None

	@property
	def ElctrncMlngSvcRef(self):
		return self._ElctrncMlngSvcRef

	@ElctrncMlngSvcRef.setter
	def ElctrncMlngSvcRef(self, value):
		self._ElctrncMlngSvcRef = value if type(value) != base_types.auto else self.make_default("ElctrncMlngSvcRef")

	@ElctrncMlngSvcRef.deleter
	def ElctrncMlngSvcRef(self):
		del self._ElctrncMlngSvcRef
		self._ElctrncMlngSvcRef = None

	@property
	def EqtyVal(self):
		return self._EqtyVal

	@EqtyVal.setter
	def EqtyVal(self, value):
		self._EqtyVal = value if type(value) != base_types.auto else self.make_default("EqtyVal")

	@EqtyVal.deleter
	def EqtyVal(self):
		del self._EqtyVal
		self._EqtyVal = None

	@property
	def FATCAFormTp(self):
		return self._FATCAFormTp

	@FATCAFormTp.setter
	def FATCAFormTp(self, value):
		self._FATCAFormTp = value if type(value) != base_types.auto else self.make_default("FATCAFormTp")

	@FATCAFormTp.deleter
	def FATCAFormTp(self):
		del self._FATCAFormTp
		self._FATCAFormTp = None

	@property
	def FATCARptgDt(self):
		return self._FATCARptgDt

	@FATCARptgDt.setter
	def FATCARptgDt(self, value):
		self._FATCARptgDt = value if type(value) != base_types.auto else self.make_default("FATCARptgDt")

	@FATCARptgDt.deleter
	def FATCARptgDt(self):
		del self._FATCARptgDt
		self._FATCARptgDt = None

	@property
	def FATCASts(self):
		return self._FATCASts

	@FATCASts.setter
	def FATCASts(self, value):
		self._FATCASts = value if type(value) != base_types.auto else self.make_default("FATCASts")

	@FATCASts.deleter
	def FATCASts(self):
		del self._FATCASts
		self._FATCASts = None

	@property
	def FsclXmptn(self):
		return self._FsclXmptn

	@FsclXmptn.setter
	def FsclXmptn(self, value):
		self._FsclXmptn = value if type(value) != base_types.auto else self.make_default("FsclXmptn")

	@FsclXmptn.deleter
	def FsclXmptn(self):
		del self._FsclXmptn
		self._FsclXmptn = None

	@property
	def InvstrPrflVldtn(self):
		return self._InvstrPrflVldtn

	@InvstrPrflVldtn.setter
	def InvstrPrflVldtn(self, value):
		self._InvstrPrflVldtn = value if type(value) != base_types.auto else self.make_default("InvstrPrflVldtn")

	@InvstrPrflVldtn.deleter
	def InvstrPrflVldtn(self):
		del self._InvstrPrflVldtn
		self._InvstrPrflVldtn = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def MailTp(self):
		return self._MailTp

	@MailTp.setter
	def MailTp(self, value):
		self._MailTp = value if type(value) != base_types.auto else self.make_default("MailTp")

	@MailTp.deleter
	def MailTp(self):
		del self._MailTp
		self._MailTp = None

	@property
	def MiFIDClssfctn(self):
		return self._MiFIDClssfctn

	@MiFIDClssfctn.setter
	def MiFIDClssfctn(self, value):
		self._MiFIDClssfctn = value if type(value) != base_types.auto else self.make_default("MiFIDClssfctn")

	@MiFIDClssfctn.deleter
	def MiFIDClssfctn(self):
		del self._MiFIDClssfctn
		self._MiFIDClssfctn = None

	@property
	def MntryWlth(self):
		return self._MntryWlth

	@MntryWlth.setter
	def MntryWlth(self, value):
		self._MntryWlth = value if type(value) != base_types.auto else self.make_default("MntryWlth")

	@MntryWlth.deleter
	def MntryWlth(self):
		del self._MntryWlth
		self._MntryWlth = None

	@property
	def MnyLndrgChck(self):
		return self._MnyLndrgChck

	@MnyLndrgChck.setter
	def MnyLndrgChck(self, value):
		self._MnyLndrgChck = value if type(value) != base_types.auto else self.make_default("MnyLndrgChck")

	@MnyLndrgChck.deleter
	def MnyLndrgChck(self):
		del self._MnyLndrgChck
		self._MnyLndrgChck = None

	@property
	def Ntfctn(self):
		return self._Ntfctn

	@Ntfctn.setter
	def Ntfctn(self, value):
		self._Ntfctn = value if type(value) != base_types.auto else self.make_default("Ntfctn")

	@Ntfctn.deleter
	def Ntfctn(self):
		del self._Ntfctn
		self._Ntfctn = None

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if type(value) != base_types.auto else self.make_default("OthrId")

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = None

	@property
	def OwnrshBnfcryRate(self):
		return self._OwnrshBnfcryRate

	@OwnrshBnfcryRate.setter
	def OwnrshBnfcryRate(self, value):
		self._OwnrshBnfcryRate = value if type(value) != base_types.auto else self.make_default("OwnrshBnfcryRate")

	@OwnrshBnfcryRate.deleter
	def OwnrshBnfcryRate(self):
		del self._OwnrshBnfcryRate
		self._OwnrshBnfcryRate = None

	@property
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if type(value) != base_types.auto else self.make_default("PmryComAdr")

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if type(value) != base_types.auto else self.make_default("ScndryComAdr")

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = None

	@property
	def SgntryRghtInd(self):
		return self._SgntryRghtInd

	@SgntryRghtInd.setter
	def SgntryRghtInd(self, value):
		self._SgntryRghtInd = value if type(value) != base_types.auto else self.make_default("SgntryRghtInd")

	@SgntryRghtInd.deleter
	def SgntryRghtInd(self):
		del self._SgntryRghtInd
		self._SgntryRghtInd = None

	@property
	def TaxRptg(self):
		return self._TaxRptg

	@TaxRptg.setter
	def TaxRptg(self, value):
		self._TaxRptg = value if type(value) != base_types.auto else self.make_default("TaxRptg")

	@TaxRptg.deleter
	def TaxRptg(self):
		del self._TaxRptg
		self._TaxRptg = None

	@property
	def TaxXmptn(self):
		return self._TaxXmptn

	@TaxXmptn.setter
	def TaxXmptn(self, value):
		self._TaxXmptn = value if type(value) != base_types.auto else self.make_default("TaxXmptn")

	@TaxXmptn.deleter
	def TaxXmptn(self):
		del self._TaxXmptn
		self._TaxXmptn = None

	@property
	def WorkgCptl(self):
		return self._WorkgCptl

	@WorkgCptl.setter
	def WorkgCptl(self, value):
		self._WorkgCptl = value if type(value) != base_types.auto else self.make_default("WorkgCptl")

	@WorkgCptl.deleter
	def WorkgCptl(self):
		del self._WorkgCptl
		self._WorkgCptl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctgSts', type=AccountingStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditiononalInformation13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlRgltryInf', type=RegulatoryInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CRSFormTp', type=CRSForm1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CRSRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CRSSts', type=CRSStatus4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyLk', type=CompanyLink1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlgPty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryAndResdtlSts', type=CountryAndResidentialStatusType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncMlngSvcRef', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqtyVal', type=DateAndAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FATCAFormTp', type=FATCAForm1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FATCARptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FATCASts', type=FATCAStatus2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FsclXmptn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrPrflVldtn', type=PartyProfileInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MailTp', type=MailType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MiFIDClssfctn', type=MiFIDClassification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntryWlth', type=DateAndAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyLndrgChck', type=MoneyLaunderingCheck1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntfctn', type=Notification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification82, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OwnrshBnfcryRate', type=OwnershipBeneficiaryRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pty', type=Party47Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SgntryRghtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRptg', type=TaxReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxXmptn', type=TaxExemptionReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WorkgCptl', type=DateAndAmount1, min=0, max=1, mutex_group=None, array=False),
	))

