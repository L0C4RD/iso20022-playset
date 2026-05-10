import base_types
import AllOtherCash1
import PaymentInstrument20
import CashAll1
import AdditionalInformation15
import Max35Text
import FinancialInstrument105
import FundPortfolio7Choice
import ISODate
import ResidualCash2

class PortfolioTransfer13(base_types._BaseFieldType):

	__slots__ = ["_PmtDtls", "_AddtlInf", "_AllOthrCsh", "_RsdlCsh", "_TaxDt", "_TrfCmpltnId", "_Prtfl", "_ActlTrfDt", "_CshAll", "_TrfInstrRef", "_MstrRef", "_FinInstrmAsstForTrf"]
	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if type(value) != auto else self.make_default("PmtDtls")

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = None

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
	def AllOthrCsh(self):
		return self._AllOthrCsh

	@AllOthrCsh.setter
	def AllOthrCsh(self, value):
		self._AllOthrCsh = value if type(value) != auto else self.make_default("AllOthrCsh")

	@AllOthrCsh.deleter
	def AllOthrCsh(self):
		del self._AllOthrCsh
		self._AllOthrCsh = None

	@property
	def RsdlCsh(self):
		return self._RsdlCsh

	@RsdlCsh.setter
	def RsdlCsh(self, value):
		self._RsdlCsh = value if type(value) != auto else self.make_default("RsdlCsh")

	@RsdlCsh.deleter
	def RsdlCsh(self):
		del self._RsdlCsh
		self._RsdlCsh = None

	@property
	def TaxDt(self):
		return self._TaxDt

	@TaxDt.setter
	def TaxDt(self, value):
		self._TaxDt = value if type(value) != auto else self.make_default("TaxDt")

	@TaxDt.deleter
	def TaxDt(self):
		del self._TaxDt
		self._TaxDt = None

	@property
	def TrfCmpltnId(self):
		return self._TrfCmpltnId

	@TrfCmpltnId.setter
	def TrfCmpltnId(self, value):
		self._TrfCmpltnId = value if type(value) != auto else self.make_default("TrfCmpltnId")

	@TrfCmpltnId.deleter
	def TrfCmpltnId(self):
		del self._TrfCmpltnId
		self._TrfCmpltnId = None

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if type(value) != auto else self.make_default("Prtfl")

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = None

	@property
	def ActlTrfDt(self):
		return self._ActlTrfDt

	@ActlTrfDt.setter
	def ActlTrfDt(self, value):
		self._ActlTrfDt = value if type(value) != auto else self.make_default("ActlTrfDt")

	@ActlTrfDt.deleter
	def ActlTrfDt(self):
		del self._ActlTrfDt
		self._ActlTrfDt = None

	@property
	def CshAll(self):
		return self._CshAll

	@CshAll.setter
	def CshAll(self, value):
		self._CshAll = value if type(value) != auto else self.make_default("CshAll")

	@CshAll.deleter
	def CshAll(self):
		del self._CshAll
		self._CshAll = None

	@property
	def TrfInstrRef(self):
		return self._TrfInstrRef

	@TrfInstrRef.setter
	def TrfInstrRef(self, value):
		self._TrfInstrRef = value if type(value) != auto else self.make_default("TrfInstrRef")

	@TrfInstrRef.deleter
	def TrfInstrRef(self):
		del self._TrfInstrRef
		self._TrfInstrRef = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def FinInstrmAsstForTrf(self):
		return self._FinInstrmAsstForTrf

	@FinInstrmAsstForTrf.setter
	def FinInstrmAsstForTrf(self, value):
		self._FinInstrmAsstForTrf = value if type(value) != auto else self.make_default("FinInstrmAsstForTrf")

	@FinInstrmAsstForTrf.deleter
	def FinInstrmAsstForTrf(self):
		del self._FinInstrmAsstForTrf
		self._FinInstrmAsstForTrf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllOthrCsh', type=AllOtherCash1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsdlCsh', type=ResidualCash2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCmpltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtfl', type=FundPortfolio7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlTrfDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAll', type=CashAll1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfInstrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAsstForTrf', type=FinancialInstrument105, min=0, max=None, mutex_group=None, array=True),
	))

