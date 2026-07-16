# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import DecimalNumber
from . import FinancialItem1
from . import FinancialItemParameters1
from . import ISODate
from . import Max15NumericText
from . import Max2000Text
from . import PaymentIdentification1
from . import PaymentMeans1
from . import PaymentTerms6
from . import ValidationStatusInformation1
from . import xs:IDREF

class ReconciliationList1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Advsr", "_AssoctdDoc", "_CtrlSum", "_Dt", "_Itm", "_ItmCnt", "_Params", "_PmtAmt", "_PmtDt", "_PmtMeans", "_PmtRef", "_PmtTerms", "_Rcpt", "_RltdDoc", "_VldtnStsInf"]
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
	def Advsr(self):
		return self._Advsr

	@Advsr.setter
	def Advsr(self, value):
		self._Advsr = value if value is not None else base_types.UninitialisedField(self, 'Advsr', xs:IDREF, False)

	@Advsr.deleter
	def Advsr(self):
		del self._Advsr
		self._Advsr = base_types.UninitialisedField(self, 'Advsr', xs:IDREF, False)

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

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
	def Itm(self):
		return self._Itm

	@Itm.setter
	def Itm(self, value):
		self._Itm = value if value is not None else base_types.UninitialisedField(self, 'Itm', FinancialItem1, True)

	@Itm.deleter
	def Itm(self):
		del self._Itm
		self._Itm = base_types.UninitialisedField(self, 'Itm', FinancialItem1, True)

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
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if value is not None else base_types.UninitialisedField(self, 'Params', FinancialItemParameters1, False)

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = base_types.UninitialisedField(self, 'Params', FinancialItemParameters1, False)

	@property
	def PmtAmt(self):
		return self._PmtAmt

	@PmtAmt.setter
	def PmtAmt(self, value):
		self._PmtAmt = value if value is not None else base_types.UninitialisedField(self, 'PmtAmt', CurrencyAndAmount, False)

	@PmtAmt.deleter
	def PmtAmt(self):
		del self._PmtAmt
		self._PmtAmt = base_types.UninitialisedField(self, 'PmtAmt', CurrencyAndAmount, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', ISODate, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', ISODate, False)

	@property
	def PmtMeans(self):
		return self._PmtMeans

	@PmtMeans.setter
	def PmtMeans(self, value):
		self._PmtMeans = value if value is not None else base_types.UninitialisedField(self, 'PmtMeans', PaymentMeans1, False)

	@PmtMeans.deleter
	def PmtMeans(self):
		del self._PmtMeans
		self._PmtMeans = base_types.UninitialisedField(self, 'PmtMeans', PaymentMeans1, False)

	@property
	def PmtRef(self):
		return self._PmtRef

	@PmtRef.setter
	def PmtRef(self, value):
		self._PmtRef = value if value is not None else base_types.UninitialisedField(self, 'PmtRef', PaymentIdentification1, False)

	@PmtRef.deleter
	def PmtRef(self):
		del self._PmtRef
		self._PmtRef = base_types.UninitialisedField(self, 'PmtRef', PaymentIdentification1, False)

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if value is not None else base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms6, False)

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms6, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', xs:IDREF, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', xs:IDREF, False)

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
		base_types.FieldEntry(name='Advsr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Itm', type=FinancialItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ItmCnt', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=FinancialItemParameters1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMeans', type=PaymentMeans1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRef', type=PaymentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
	))