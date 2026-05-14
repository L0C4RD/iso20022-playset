# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AgreedRate1 import AgreedRate1
from ._DecimalNumber import DecimalNumber
from ._FinancialItem1 import FinancialItem1
from ._FinancingInformationAndStatus1 import FinancingInformationAndStatus1
from ._FinancingNotificationParties1 import FinancingNotificationParties1
from ._FinancingRateOrAmountChoice import FinancingRateOrAmountChoice
from ._ISODate import ISODate
from ._Instalment2 import Instalment2
from ._Max15NumericText import Max15NumericText
from ._Max2000Text import Max2000Text
from ._Max35Text import Max35Text
from ._ValidationStatusInformation1 import ValidationStatusInformation1
from ._xs:IDREF import xs:IDREF

class FinancingItemList1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgrdRate", "_AmtCutOffDt", "_Assgne", "_Assgnr", "_CtrlSum", "_FinItm", "_FincgInstlmt", "_FincgSts", "_Idr", "_IsseDt", "_ItmCnt", "_NtfctnInf", "_RltdDoc", "_TtlReqAmt", "_TtlReqFincg", "_VldtnStsInf"]
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
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if type(value) != base_types.auto else self.make_default("AgrdRate")

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = None

	@property
	def AmtCutOffDt(self):
		return self._AmtCutOffDt

	@AmtCutOffDt.setter
	def AmtCutOffDt(self, value):
		self._AmtCutOffDt = value if type(value) != base_types.auto else self.make_default("AmtCutOffDt")

	@AmtCutOffDt.deleter
	def AmtCutOffDt(self):
		del self._AmtCutOffDt
		self._AmtCutOffDt = None

	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if type(value) != base_types.auto else self.make_default("Assgne")

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def FinItm(self):
		return self._FinItm

	@FinItm.setter
	def FinItm(self, value):
		self._FinItm = value if type(value) != base_types.auto else self.make_default("FinItm")

	@FinItm.deleter
	def FinItm(self):
		del self._FinItm
		self._FinItm = None

	@property
	def FincgInstlmt(self):
		return self._FincgInstlmt

	@FincgInstlmt.setter
	def FincgInstlmt(self, value):
		self._FincgInstlmt = value if type(value) != base_types.auto else self.make_default("FincgInstlmt")

	@FincgInstlmt.deleter
	def FincgInstlmt(self):
		del self._FincgInstlmt
		self._FincgInstlmt = None

	@property
	def FincgSts(self):
		return self._FincgSts

	@FincgSts.setter
	def FincgSts(self, value):
		self._FincgSts = value if type(value) != base_types.auto else self.make_default("FincgSts")

	@FincgSts.deleter
	def FincgSts(self):
		del self._FincgSts
		self._FincgSts = None

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
	def ItmCnt(self):
		return self._ItmCnt

	@ItmCnt.setter
	def ItmCnt(self, value):
		self._ItmCnt = value if type(value) != base_types.auto else self.make_default("ItmCnt")

	@ItmCnt.deleter
	def ItmCnt(self):
		del self._ItmCnt
		self._ItmCnt = None

	@property
	def NtfctnInf(self):
		return self._NtfctnInf

	@NtfctnInf.setter
	def NtfctnInf(self, value):
		self._NtfctnInf = value if type(value) != base_types.auto else self.make_default("NtfctnInf")

	@NtfctnInf.deleter
	def NtfctnInf(self):
		del self._NtfctnInf
		self._NtfctnInf = None

	@property
	def RltdDoc(self):
		return self._RltdDoc

	@RltdDoc.setter
	def RltdDoc(self, value):
		self._RltdDoc = value if type(value) != base_types.auto else self.make_default("RltdDoc")

	@RltdDoc.deleter
	def RltdDoc(self):
		del self._RltdDoc
		self._RltdDoc = None

	@property
	def TtlReqAmt(self):
		return self._TtlReqAmt

	@TtlReqAmt.setter
	def TtlReqAmt(self, value):
		self._TtlReqAmt = value if type(value) != base_types.auto else self.make_default("TtlReqAmt")

	@TtlReqAmt.deleter
	def TtlReqAmt(self):
		del self._TtlReqAmt
		self._TtlReqAmt = None

	@property
	def TtlReqFincg(self):
		return self._TtlReqFincg

	@TtlReqFincg.setter
	def TtlReqFincg(self, value):
		self._TtlReqFincg = value if type(value) != base_types.auto else self.make_default("TtlReqFincg")

	@TtlReqFincg.deleter
	def TtlReqFincg(self):
		del self._TtlReqFincg
		self._TtlReqFincg = None

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if type(value) != base_types.auto else self.make_default("VldtnStsInf")

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = None

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