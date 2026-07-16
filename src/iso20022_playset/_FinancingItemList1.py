# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AgreedRate1
from . import DecimalNumber
from . import FinancialItem1
from . import FinancingInformationAndStatus1
from . import FinancingNotificationParties1
from . import FinancingRateOrAmountChoice
from . import ISODate
from . import Instalment2
from . import Max15NumericText
from . import Max2000Text
from . import Max35Text
from . import ValidationStatusInformation1
from . import xs:IDREF

class FinancingItemList1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgrdRate", "_AmtCutOffDt", "_Assgne", "_Assgnr", "_CtrlSum", "_FinItm", "_FincgInstlmt", "_FincgSts", "_Idr", "_IsseDt", "_ItmCnt", "_NtfctnInf", "_RltdDoc", "_TtlReqAmt", "_TtlReqFincg", "_VldtnStsInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@property
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if value is not None else base_types.UninitialisedField(self, 'AgrdRate', AgreedRate1, False)

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = base_types.UninitialisedField(self, 'AgrdRate', AgreedRate1, False)

	@property
	def AmtCutOffDt(self):
		return self._AmtCutOffDt

	@AmtCutOffDt.setter
	def AmtCutOffDt(self, value):
		self._AmtCutOffDt = value if value is not None else base_types.UninitialisedField(self, 'AmtCutOffDt', ISODate, False)

	@AmtCutOffDt.deleter
	def AmtCutOffDt(self):
		del self._AmtCutOffDt
		self._AmtCutOffDt = base_types.UninitialisedField(self, 'AmtCutOffDt', ISODate, False)

	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if value is not None else base_types.UninitialisedField(self, 'Assgne', xs:IDREF, False)

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = base_types.UninitialisedField(self, 'Assgne', xs:IDREF, False)

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', xs:IDREF, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', xs:IDREF, False)

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if value is not None else base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@property
	def FinItm(self):
		return self._FinItm

	@FinItm.setter
	def FinItm(self, value):
		self._FinItm = value if value is not None else base_types.UninitialisedField(self, 'FinItm', FinancialItem1, True)

	@FinItm.deleter
	def FinItm(self):
		del self._FinItm
		self._FinItm = base_types.UninitialisedField(self, 'FinItm', FinancialItem1, True)

	@property
	def FincgInstlmt(self):
		return self._FincgInstlmt

	@FincgInstlmt.setter
	def FincgInstlmt(self, value):
		self._FincgInstlmt = value if value is not None else base_types.UninitialisedField(self, 'FincgInstlmt', Instalment2, True)

	@FincgInstlmt.deleter
	def FincgInstlmt(self):
		del self._FincgInstlmt
		self._FincgInstlmt = base_types.UninitialisedField(self, 'FincgInstlmt', Instalment2, True)

	@property
	def FincgSts(self):
		return self._FincgSts

	@FincgSts.setter
	def FincgSts(self, value):
		self._FincgSts = value if value is not None else base_types.UninitialisedField(self, 'FincgSts', FinancingInformationAndStatus1, False)

	@FincgSts.deleter
	def FincgSts(self):
		del self._FincgSts
		self._FincgSts = base_types.UninitialisedField(self, 'FincgSts', FinancingInformationAndStatus1, False)

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
	def ItmCnt(self):
		return self._ItmCnt

	@ItmCnt.setter
	def ItmCnt(self, value):
		self._ItmCnt = value if value is not None else base_types.UninitialisedField(self, 'ItmCnt', Max15NumericText, False)

	@ItmCnt.deleter
	def ItmCnt(self):
		del self._ItmCnt
		self._ItmCnt = base_types.UninitialisedField(self, 'ItmCnt', Max15NumericText, False)

	@property
	def NtfctnInf(self):
		return self._NtfctnInf

	@NtfctnInf.setter
	def NtfctnInf(self, value):
		self._NtfctnInf = value if value is not None else base_types.UninitialisedField(self, 'NtfctnInf', FinancingNotificationParties1, True)

	@NtfctnInf.deleter
	def NtfctnInf(self):
		del self._NtfctnInf
		self._NtfctnInf = base_types.UninitialisedField(self, 'NtfctnInf', FinancingNotificationParties1, True)

	@property
	def RltdDoc(self):
		return self._RltdDoc

	@RltdDoc.setter
	def RltdDoc(self, value):
		self._RltdDoc = value if value is not None else base_types.UninitialisedField(self, 'RltdDoc', xs:IDREF, True)

	@RltdDoc.deleter
	def RltdDoc(self):
		del self._RltdDoc
		self._RltdDoc = base_types.UninitialisedField(self, 'RltdDoc', xs:IDREF, True)

	@property
	def TtlReqAmt(self):
		return self._TtlReqAmt

	@TtlReqAmt.setter
	def TtlReqAmt(self, value):
		self._TtlReqAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlReqAmt', ActiveCurrencyAndAmount, False)

	@TtlReqAmt.deleter
	def TtlReqAmt(self):
		del self._TtlReqAmt
		self._TtlReqAmt = base_types.UninitialisedField(self, 'TtlReqAmt', ActiveCurrencyAndAmount, False)

	@property
	def TtlReqFincg(self):
		return self._TtlReqFincg

	@TtlReqFincg.setter
	def TtlReqFincg(self, value):
		self._TtlReqFincg = value if value is not None else base_types.UninitialisedField(self, 'TtlReqFincg', FinancingRateOrAmountChoice, False)

	@TtlReqFincg.deleter
	def TtlReqFincg(self):
		del self._TtlReqFincg
		self._TtlReqFincg = base_types.UninitialisedField(self, 'TtlReqFincg', FinancingRateOrAmountChoice, False)

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if value is not None else base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdRate', type=AgreedRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtCutOffDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgne', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinItm', type=FinancialItem1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FincgInstlmt', type=Instalment2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FincgSts', type=FinancingInformationAndStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnInf', type=FinancingNotificationParties1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlReqAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqFincg', type=FinancingRateOrAmountChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
	))