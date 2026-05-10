from . import base_types
from .PaymentTerms6 import PaymentTerms6
from .DecimalNumber import DecimalNumber
from .ValidationStatusInformation1 import ValidationStatusInformation1
from .xs:IDREF import xs:IDREF
from .Max2000Text import Max2000Text
from .ISODate import ISODate
from .PaymentIdentification1 import PaymentIdentification1
from .Max15NumericText import Max15NumericText
from .FinancialItemParameters1 import FinancialItemParameters1
from .PaymentMeans1 import PaymentMeans1
from .FinancialItem1 import FinancialItem1
from .CurrencyAndAmount import CurrencyAndAmount

class ReconciliationList1(base_types._BaseFieldType):

	__slots__ = ["_PmtTerms", "_Rcpt", "_AddtlInf", "_VldtnStsInf", "_ItmCnt", "_AssoctdDoc", "_PmtMeans", "_CtrlSum", "_Advsr", "_Itm", "_PmtDt", "_Dt", "_Params", "_PmtAmt", "_PmtRef", "_RltdDoc"]
	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if type(value) != base_types.auto else self.make_default("PmtTerms")

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

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
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if type(value) != base_types.auto else self.make_default("VldtnStsInf")

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = None

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
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if type(value) != base_types.auto else self.make_default("AssoctdDoc")

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = None

	@property
	def PmtMeans(self):
		return self._PmtMeans

	@PmtMeans.setter
	def PmtMeans(self, value):
		self._PmtMeans = value if type(value) != base_types.auto else self.make_default("PmtMeans")

	@PmtMeans.deleter
	def PmtMeans(self):
		del self._PmtMeans
		self._PmtMeans = None

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
	def Advsr(self):
		return self._Advsr

	@Advsr.setter
	def Advsr(self, value):
		self._Advsr = value if type(value) != base_types.auto else self.make_default("Advsr")

	@Advsr.deleter
	def Advsr(self):
		del self._Advsr
		self._Advsr = None

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
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

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
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if type(value) != base_types.auto else self.make_default("Params")

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = None

	@property
	def PmtAmt(self):
		return self._PmtAmt

	@PmtAmt.setter
	def PmtAmt(self, value):
		self._PmtAmt = value if type(value) != base_types.auto else self.make_default("PmtAmt")

	@PmtAmt.deleter
	def PmtAmt(self):
		del self._PmtAmt
		self._PmtAmt = None

	@property
	def PmtRef(self):
		return self._PmtRef

	@PmtRef.setter
	def PmtRef(self, value):
		self._PmtRef = value if type(value) != base_types.auto else self.make_default("PmtRef")

	@PmtRef.deleter
	def PmtRef(self):
		del self._PmtRef
		self._PmtRef = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtMeans', type=PaymentMeans1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Advsr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Itm', type=FinancialItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=FinancialItemParameters1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRef', type=PaymentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
	))

