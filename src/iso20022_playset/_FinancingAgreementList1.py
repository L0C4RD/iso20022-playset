# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import FinancingAgreementItem1
from . import FinancingNotificationParties1
from . import ISODate
from . import Max15NumericText
from . import Max2000Text
from . import Max35Text
from . import ValidationStatusInformation1
from . import xs:IDREF

class FinancingAgreementList1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgrmtRqstr", "_AgrmtRspndr", "_CtrlSum", "_Dt", "_GrntApplcnt", "_GrntIssr", "_GrntNbfcry", "_Idr", "_Itm", "_ItmCnt", "_NtfctnInf", "_RltdDoc", "_VldtnStsInf"]
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
	def AgrmtRqstr(self):
		return self._AgrmtRqstr

	@AgrmtRqstr.setter
	def AgrmtRqstr(self, value):
		self._AgrmtRqstr = value if value is not None else base_types.UninitialisedField(self, 'AgrmtRqstr', xs:IDREF, False)

	@AgrmtRqstr.deleter
	def AgrmtRqstr(self):
		del self._AgrmtRqstr
		self._AgrmtRqstr = base_types.UninitialisedField(self, 'AgrmtRqstr', xs:IDREF, False)

	@property
	def AgrmtRspndr(self):
		return self._AgrmtRspndr

	@AgrmtRspndr.setter
	def AgrmtRspndr(self, value):
		self._AgrmtRspndr = value if value is not None else base_types.UninitialisedField(self, 'AgrmtRspndr', xs:IDREF, False)

	@AgrmtRspndr.deleter
	def AgrmtRspndr(self):
		del self._AgrmtRspndr
		self._AgrmtRspndr = base_types.UninitialisedField(self, 'AgrmtRspndr', xs:IDREF, False)

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
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def GrntApplcnt(self):
		return self._GrntApplcnt

	@GrntApplcnt.setter
	def GrntApplcnt(self, value):
		self._GrntApplcnt = value if value is not None else base_types.UninitialisedField(self, 'GrntApplcnt', xs:IDREF, False)

	@GrntApplcnt.deleter
	def GrntApplcnt(self):
		del self._GrntApplcnt
		self._GrntApplcnt = base_types.UninitialisedField(self, 'GrntApplcnt', xs:IDREF, False)

	@property
	def GrntIssr(self):
		return self._GrntIssr

	@GrntIssr.setter
	def GrntIssr(self, value):
		self._GrntIssr = value if value is not None else base_types.UninitialisedField(self, 'GrntIssr', xs:IDREF, False)

	@GrntIssr.deleter
	def GrntIssr(self):
		del self._GrntIssr
		self._GrntIssr = base_types.UninitialisedField(self, 'GrntIssr', xs:IDREF, False)

	@property
	def GrntNbfcry(self):
		return self._GrntNbfcry

	@GrntNbfcry.setter
	def GrntNbfcry(self, value):
		self._GrntNbfcry = value if value is not None else base_types.UninitialisedField(self, 'GrntNbfcry', xs:IDREF, False)

	@GrntNbfcry.deleter
	def GrntNbfcry(self):
		del self._GrntNbfcry
		self._GrntNbfcry = base_types.UninitialisedField(self, 'GrntNbfcry', xs:IDREF, False)

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
	def Itm(self):
		return self._Itm

	@Itm.setter
	def Itm(self, value):
		self._Itm = value if value is not None else base_types.UninitialisedField(self, 'Itm', FinancingAgreementItem1, True)

	@Itm.deleter
	def Itm(self):
		del self._Itm
		self._Itm = base_types.UninitialisedField(self, 'Itm', FinancingAgreementItem1, True)

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
		base_types.FieldEntry(name='AgrmtRqstr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtRspndr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntApplcnt', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntIssr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntNbfcry', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Itm', type=FinancingAgreementItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnInf', type=FinancingNotificationParties1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
	))