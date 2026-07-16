# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountingStatus1Choice
from . import AdditiononalInformation13
from . import CRSForm1Choice
from . import CRSStatus4
from . import CommunicationAddress6
from . import CompanyLink1Choice
from . import CountryAndResidentialStatusType2
from . import DateAndAmount1
from . import FATCAForm1Choice
from . import FATCAStatus2
from . import GenericIdentification82
from . import ISODate
from . import LanguageCode
from . import MailType1Choice
from . import Max350Text
from . import Max35Text
from . import MiFIDClassification1
from . import ModificationScope27
from . import MoneyLaunderingCheck1Choice
from . import Notification2
from . import OwnershipBeneficiaryRate1
from . import Party48Choice
from . import RegulatoryInformation1
from . import TaxExemptionReason2Choice
from . import TaxReporting3
from . import YesNoIndicator

class InvestmentAccountOwnershipInformation17(base_types._BaseFieldType):

	__slots__ = ["_AcctgSts", "_AddtlInf", "_AddtlRgltryInf", "_CRSFormTp", "_CRSRptgDt", "_CRSSts", "_ClntId", "_CpnyLk", "_CtrlgPty", "_CtryAndResdtlSts", "_ElctrncMlngSvcRef", "_EqtyVal", "_FATCAFormTp", "_FATCARptgDt", "_FATCASts", "_FsclXmptn", "_Lang", "_MailTp", "_MiFIDClssfctn", "_MntryWlth", "_MnyLndrgChck", "_ModfdInvstrPrflVldtn", "_Ntfctn", "_OthrId", "_OwnrshBnfcryRate", "_PmryComAdr", "_Pty", "_ScndryComAdr", "_SgntryRghtInd", "_TaxRptg", "_TaxXmptn", "_WorkgCptl"]
	@property
	def AcctgSts(self):
		return self._AcctgSts

	@AcctgSts.setter
	def AcctgSts(self, value):
		self._AcctgSts = value if value is not None else base_types.UninitialisedField(self, 'AcctgSts', AccountingStatus1Choice, False)

	@AcctgSts.deleter
	def AcctgSts(self):
		del self._AcctgSts
		self._AcctgSts = base_types.UninitialisedField(self, 'AcctgSts', AccountingStatus1Choice, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditiononalInformation13, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditiononalInformation13, True)

	@property
	def AddtlRgltryInf(self):
		return self._AddtlRgltryInf

	@AddtlRgltryInf.setter
	def AddtlRgltryInf(self, value):
		self._AddtlRgltryInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRgltryInf', RegulatoryInformation1, False)

	@AddtlRgltryInf.deleter
	def AddtlRgltryInf(self):
		del self._AddtlRgltryInf
		self._AddtlRgltryInf = base_types.UninitialisedField(self, 'AddtlRgltryInf', RegulatoryInformation1, False)

	@property
	def CRSFormTp(self):
		return self._CRSFormTp

	@CRSFormTp.setter
	def CRSFormTp(self, value):
		self._CRSFormTp = value if value is not None else base_types.UninitialisedField(self, 'CRSFormTp', CRSForm1Choice, True)

	@CRSFormTp.deleter
	def CRSFormTp(self):
		del self._CRSFormTp
		self._CRSFormTp = base_types.UninitialisedField(self, 'CRSFormTp', CRSForm1Choice, True)

	@property
	def CRSRptgDt(self):
		return self._CRSRptgDt

	@CRSRptgDt.setter
	def CRSRptgDt(self, value):
		self._CRSRptgDt = value if value is not None else base_types.UninitialisedField(self, 'CRSRptgDt', ISODate, False)

	@CRSRptgDt.deleter
	def CRSRptgDt(self):
		del self._CRSRptgDt
		self._CRSRptgDt = base_types.UninitialisedField(self, 'CRSRptgDt', ISODate, False)

	@property
	def CRSSts(self):
		return self._CRSSts

	@CRSSts.setter
	def CRSSts(self, value):
		self._CRSSts = value if value is not None else base_types.UninitialisedField(self, 'CRSSts', CRSStatus4, True)

	@CRSSts.deleter
	def CRSSts(self):
		del self._CRSSts
		self._CRSSts = base_types.UninitialisedField(self, 'CRSSts', CRSStatus4, True)

	@property
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if value is not None else base_types.UninitialisedField(self, 'ClntId', Max35Text, False)

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = base_types.UninitialisedField(self, 'ClntId', Max35Text, False)

	@property
	def CpnyLk(self):
		return self._CpnyLk

	@CpnyLk.setter
	def CpnyLk(self, value):
		self._CpnyLk = value if value is not None else base_types.UninitialisedField(self, 'CpnyLk', CompanyLink1Choice, False)

	@CpnyLk.deleter
	def CpnyLk(self):
		del self._CpnyLk
		self._CpnyLk = base_types.UninitialisedField(self, 'CpnyLk', CompanyLink1Choice, False)

	@property
	def CtrlgPty(self):
		return self._CtrlgPty

	@CtrlgPty.setter
	def CtrlgPty(self, value):
		self._CtrlgPty = value if value is not None else base_types.UninitialisedField(self, 'CtrlgPty', YesNoIndicator, False)

	@CtrlgPty.deleter
	def CtrlgPty(self):
		del self._CtrlgPty
		self._CtrlgPty = base_types.UninitialisedField(self, 'CtrlgPty', YesNoIndicator, False)

	@property
	def CtryAndResdtlSts(self):
		return self._CtryAndResdtlSts

	@CtryAndResdtlSts.setter
	def CtryAndResdtlSts(self, value):
		self._CtryAndResdtlSts = value if value is not None else base_types.UninitialisedField(self, 'CtryAndResdtlSts', CountryAndResidentialStatusType2, False)

	@CtryAndResdtlSts.deleter
	def CtryAndResdtlSts(self):
		del self._CtryAndResdtlSts
		self._CtryAndResdtlSts = base_types.UninitialisedField(self, 'CtryAndResdtlSts', CountryAndResidentialStatusType2, False)

	@property
	def ElctrncMlngSvcRef(self):
		return self._ElctrncMlngSvcRef

	@ElctrncMlngSvcRef.setter
	def ElctrncMlngSvcRef(self, value):
		self._ElctrncMlngSvcRef = value if value is not None else base_types.UninitialisedField(self, 'ElctrncMlngSvcRef', Max350Text, False)

	@ElctrncMlngSvcRef.deleter
	def ElctrncMlngSvcRef(self):
		del self._ElctrncMlngSvcRef
		self._ElctrncMlngSvcRef = base_types.UninitialisedField(self, 'ElctrncMlngSvcRef', Max350Text, False)

	@property
	def EqtyVal(self):
		return self._EqtyVal

	@EqtyVal.setter
	def EqtyVal(self, value):
		self._EqtyVal = value if value is not None else base_types.UninitialisedField(self, 'EqtyVal', DateAndAmount1, False)

	@EqtyVal.deleter
	def EqtyVal(self):
		del self._EqtyVal
		self._EqtyVal = base_types.UninitialisedField(self, 'EqtyVal', DateAndAmount1, False)

	@property
	def FATCAFormTp(self):
		return self._FATCAFormTp

	@FATCAFormTp.setter
	def FATCAFormTp(self, value):
		self._FATCAFormTp = value if value is not None else base_types.UninitialisedField(self, 'FATCAFormTp', FATCAForm1Choice, True)

	@FATCAFormTp.deleter
	def FATCAFormTp(self):
		del self._FATCAFormTp
		self._FATCAFormTp = base_types.UninitialisedField(self, 'FATCAFormTp', FATCAForm1Choice, True)

	@property
	def FATCARptgDt(self):
		return self._FATCARptgDt

	@FATCARptgDt.setter
	def FATCARptgDt(self, value):
		self._FATCARptgDt = value if value is not None else base_types.UninitialisedField(self, 'FATCARptgDt', ISODate, False)

	@FATCARptgDt.deleter
	def FATCARptgDt(self):
		del self._FATCARptgDt
		self._FATCARptgDt = base_types.UninitialisedField(self, 'FATCARptgDt', ISODate, False)

	@property
	def FATCASts(self):
		return self._FATCASts

	@FATCASts.setter
	def FATCASts(self, value):
		self._FATCASts = value if value is not None else base_types.UninitialisedField(self, 'FATCASts', FATCAStatus2, True)

	@FATCASts.deleter
	def FATCASts(self):
		del self._FATCASts
		self._FATCASts = base_types.UninitialisedField(self, 'FATCASts', FATCAStatus2, True)

	@property
	def FsclXmptn(self):
		return self._FsclXmptn

	@FsclXmptn.setter
	def FsclXmptn(self, value):
		self._FsclXmptn = value if value is not None else base_types.UninitialisedField(self, 'FsclXmptn', YesNoIndicator, False)

	@FsclXmptn.deleter
	def FsclXmptn(self):
		del self._FsclXmptn
		self._FsclXmptn = base_types.UninitialisedField(self, 'FsclXmptn', YesNoIndicator, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@property
	def MailTp(self):
		return self._MailTp

	@MailTp.setter
	def MailTp(self, value):
		self._MailTp = value if value is not None else base_types.UninitialisedField(self, 'MailTp', MailType1Choice, False)

	@MailTp.deleter
	def MailTp(self):
		del self._MailTp
		self._MailTp = base_types.UninitialisedField(self, 'MailTp', MailType1Choice, False)

	@property
	def MiFIDClssfctn(self):
		return self._MiFIDClssfctn

	@MiFIDClssfctn.setter
	def MiFIDClssfctn(self, value):
		self._MiFIDClssfctn = value if value is not None else base_types.UninitialisedField(self, 'MiFIDClssfctn', MiFIDClassification1, False)

	@MiFIDClssfctn.deleter
	def MiFIDClssfctn(self):
		del self._MiFIDClssfctn
		self._MiFIDClssfctn = base_types.UninitialisedField(self, 'MiFIDClssfctn', MiFIDClassification1, False)

	@property
	def MntryWlth(self):
		return self._MntryWlth

	@MntryWlth.setter
	def MntryWlth(self, value):
		self._MntryWlth = value if value is not None else base_types.UninitialisedField(self, 'MntryWlth', DateAndAmount1, False)

	@MntryWlth.deleter
	def MntryWlth(self):
		del self._MntryWlth
		self._MntryWlth = base_types.UninitialisedField(self, 'MntryWlth', DateAndAmount1, False)

	@property
	def MnyLndrgChck(self):
		return self._MnyLndrgChck

	@MnyLndrgChck.setter
	def MnyLndrgChck(self, value):
		self._MnyLndrgChck = value if value is not None else base_types.UninitialisedField(self, 'MnyLndrgChck', MoneyLaunderingCheck1Choice, False)

	@MnyLndrgChck.deleter
	def MnyLndrgChck(self):
		del self._MnyLndrgChck
		self._MnyLndrgChck = base_types.UninitialisedField(self, 'MnyLndrgChck', MoneyLaunderingCheck1Choice, False)

	@property
	def ModfdInvstrPrflVldtn(self):
		return self._ModfdInvstrPrflVldtn

	@ModfdInvstrPrflVldtn.setter
	def ModfdInvstrPrflVldtn(self, value):
		self._ModfdInvstrPrflVldtn = value if value is not None else base_types.UninitialisedField(self, 'ModfdInvstrPrflVldtn', ModificationScope27, True)

	@ModfdInvstrPrflVldtn.deleter
	def ModfdInvstrPrflVldtn(self):
		del self._ModfdInvstrPrflVldtn
		self._ModfdInvstrPrflVldtn = base_types.UninitialisedField(self, 'ModfdInvstrPrflVldtn', ModificationScope27, True)

	@property
	def Ntfctn(self):
		return self._Ntfctn

	@Ntfctn.setter
	def Ntfctn(self, value):
		self._Ntfctn = value if value is not None else base_types.UninitialisedField(self, 'Ntfctn', Notification2, True)

	@Ntfctn.deleter
	def Ntfctn(self):
		del self._Ntfctn
		self._Ntfctn = base_types.UninitialisedField(self, 'Ntfctn', Notification2, True)

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if value is not None else base_types.UninitialisedField(self, 'OthrId', GenericIdentification82, True)

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = base_types.UninitialisedField(self, 'OthrId', GenericIdentification82, True)

	@property
	def OwnrshBnfcryRate(self):
		return self._OwnrshBnfcryRate

	@OwnrshBnfcryRate.setter
	def OwnrshBnfcryRate(self, value):
		self._OwnrshBnfcryRate = value if value is not None else base_types.UninitialisedField(self, 'OwnrshBnfcryRate', OwnershipBeneficiaryRate1, False)

	@OwnrshBnfcryRate.deleter
	def OwnrshBnfcryRate(self):
		del self._OwnrshBnfcryRate
		self._OwnrshBnfcryRate = base_types.UninitialisedField(self, 'OwnrshBnfcryRate', OwnershipBeneficiaryRate1, False)

	@property
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if value is not None else base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress6, True)

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress6, True)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', Party48Choice, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', Party48Choice, False)

	@property
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if value is not None else base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress6, True)

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress6, True)

	@property
	def SgntryRghtInd(self):
		return self._SgntryRghtInd

	@SgntryRghtInd.setter
	def SgntryRghtInd(self, value):
		self._SgntryRghtInd = value if value is not None else base_types.UninitialisedField(self, 'SgntryRghtInd', YesNoIndicator, False)

	@SgntryRghtInd.deleter
	def SgntryRghtInd(self):
		del self._SgntryRghtInd
		self._SgntryRghtInd = base_types.UninitialisedField(self, 'SgntryRghtInd', YesNoIndicator, False)

	@property
	def TaxRptg(self):
		return self._TaxRptg

	@TaxRptg.setter
	def TaxRptg(self, value):
		self._TaxRptg = value if value is not None else base_types.UninitialisedField(self, 'TaxRptg', TaxReporting3, True)

	@TaxRptg.deleter
	def TaxRptg(self):
		del self._TaxRptg
		self._TaxRptg = base_types.UninitialisedField(self, 'TaxRptg', TaxReporting3, True)

	@property
	def TaxXmptn(self):
		return self._TaxXmptn

	@TaxXmptn.setter
	def TaxXmptn(self, value):
		self._TaxXmptn = value if value is not None else base_types.UninitialisedField(self, 'TaxXmptn', TaxExemptionReason2Choice, False)

	@TaxXmptn.deleter
	def TaxXmptn(self):
		del self._TaxXmptn
		self._TaxXmptn = base_types.UninitialisedField(self, 'TaxXmptn', TaxExemptionReason2Choice, False)

	@property
	def WorkgCptl(self):
		return self._WorkgCptl

	@WorkgCptl.setter
	def WorkgCptl(self, value):
		self._WorkgCptl = value if value is not None else base_types.UninitialisedField(self, 'WorkgCptl', DateAndAmount1, False)

	@WorkgCptl.deleter
	def WorkgCptl(self):
		del self._WorkgCptl
		self._WorkgCptl = base_types.UninitialisedField(self, 'WorkgCptl', DateAndAmount1, False)

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
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MailTp', type=MailType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MiFIDClssfctn', type=MiFIDClassification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntryWlth', type=DateAndAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyLndrgChck', type=MoneyLaunderingCheck1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdInvstrPrflVldtn', type=ModificationScope27, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ntfctn', type=Notification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification82, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OwnrshBnfcryRate', type=OwnershipBeneficiaryRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pty', type=Party48Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SgntryRghtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRptg', type=TaxReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxXmptn', type=TaxExemptionReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WorkgCptl', type=DateAndAmount1, min=0, max=1, mutex_group=None, array=False),
	))