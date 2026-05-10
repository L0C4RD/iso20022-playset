from . import base_types
from ._DecimalNumber import DecimalNumber
from ._FinancingAgreementItem1 import FinancingAgreementItem1
from ._FinancingNotificationParties1 import FinancingNotificationParties1
from ._ISODate import ISODate
from ._Max15NumericText import Max15NumericText
from ._Max2000Text import Max2000Text
from ._Max35Text import Max35Text
from ._ValidationStatusInformation1 import ValidationStatusInformation1
from ._xs:IDREF import xs:IDREF

class FinancingAgreementList1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgrmtRqstr", "_AgrmtRspndr", "_CtrlSum", "_Dt", "_GrntApplcnt", "_GrntIssr", "_GrntNbfcry", "_Idr", "_Itm", "_ItmCnt", "_NtfctnInf", "_RltdDoc", "_VldtnStsInf"]
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
	def AgrmtRqstr(self):
		return self._AgrmtRqstr

	@AgrmtRqstr.setter
	def AgrmtRqstr(self, value):
		self._AgrmtRqstr = value if type(value) != base_types.auto else self.make_default("AgrmtRqstr")

	@AgrmtRqstr.deleter
	def AgrmtRqstr(self):
		del self._AgrmtRqstr
		self._AgrmtRqstr = None

	@property
	def AgrmtRspndr(self):
		return self._AgrmtRspndr

	@AgrmtRspndr.setter
	def AgrmtRspndr(self, value):
		self._AgrmtRspndr = value if type(value) != base_types.auto else self.make_default("AgrmtRspndr")

	@AgrmtRspndr.deleter
	def AgrmtRspndr(self):
		del self._AgrmtRspndr
		self._AgrmtRspndr = None

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
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def GrntApplcnt(self):
		return self._GrntApplcnt

	@GrntApplcnt.setter
	def GrntApplcnt(self, value):
		self._GrntApplcnt = value if type(value) != base_types.auto else self.make_default("GrntApplcnt")

	@GrntApplcnt.deleter
	def GrntApplcnt(self):
		del self._GrntApplcnt
		self._GrntApplcnt = None

	@property
	def GrntIssr(self):
		return self._GrntIssr

	@GrntIssr.setter
	def GrntIssr(self, value):
		self._GrntIssr = value if type(value) != base_types.auto else self.make_default("GrntIssr")

	@GrntIssr.deleter
	def GrntIssr(self):
		del self._GrntIssr
		self._GrntIssr = None

	@property
	def GrntNbfcry(self):
		return self._GrntNbfcry

	@GrntNbfcry.setter
	def GrntNbfcry(self, value):
		self._GrntNbfcry = value if type(value) != base_types.auto else self.make_default("GrntNbfcry")

	@GrntNbfcry.deleter
	def GrntNbfcry(self):
		del self._GrntNbfcry
		self._GrntNbfcry = None

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
	def Itm(self):
		return self._Itm

	@Itm.setter
	def Itm(self, value):
		self._Itm = value if type(value) != base_types.auto else self.make_default("Itm")

	@Itm.deleter
	def Itm(self):
		del self._Itm
		self._Itm = None

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

