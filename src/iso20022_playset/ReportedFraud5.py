from . import base_types
from .FraudType1Code import FraudType1Code
from .FraudReportingAction1Code import FraudReportingAction1Code
from .PartyType26Code import PartyType26Code
from .Max35Text import Max35Text

class ReportedFraud5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_CaseRef", "_OthrTp", "_RptgNtty", "_Actn", "_SubmitrCaseRef", "_OthrRptgNtty", "_OthrActn"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def CaseRef(self):
		return self._CaseRef

	@CaseRef.setter
	def CaseRef(self, value):
		self._CaseRef = value if type(value) != base_types.auto else self.make_default("CaseRef")

	@CaseRef.deleter
	def CaseRef(self):
		del self._CaseRef
		self._CaseRef = None

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if type(value) != base_types.auto else self.make_default("RptgNtty")

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != base_types.auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def SubmitrCaseRef(self):
		return self._SubmitrCaseRef

	@SubmitrCaseRef.setter
	def SubmitrCaseRef(self, value):
		self._SubmitrCaseRef = value if type(value) != base_types.auto else self.make_default("SubmitrCaseRef")

	@SubmitrCaseRef.deleter
	def SubmitrCaseRef(self):
		del self._SubmitrCaseRef
		self._SubmitrCaseRef = None

	@property
	def OthrRptgNtty(self):
		return self._OthrRptgNtty

	@OthrRptgNtty.setter
	def OthrRptgNtty(self, value):
		self._OthrRptgNtty = value if type(value) != base_types.auto else self.make_default("OthrRptgNtty")

	@OthrRptgNtty.deleter
	def OthrRptgNtty(self):
		del self._OthrRptgNtty
		self._OthrRptgNtty = None

	@property
	def OthrActn(self):
		return self._OthrActn

	@OthrActn.setter
	def OthrActn(self, value):
		self._OthrActn = value if type(value) != base_types.auto else self.make_default("OthrActn")

	@OthrActn.deleter
	def OthrActn(self):
		del self._OthrActn
		self._OthrActn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=FraudType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=PartyType26Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=FraudReportingAction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrCaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRptgNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrActn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

