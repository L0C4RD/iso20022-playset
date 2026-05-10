from . import base_types
from ._AuthenticationMethod12Code import AuthenticationMethod12Code
from ._FraudReportingAction1Code import FraudReportingAction1Code
from ._FraudType1Code import FraudType1Code
from ._ISODate import ISODate
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._PartyType26Code import PartyType26Code
from ._TrueFalseIndicator import TrueFalseIndicator

class ReportedFraud4(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_Arrst", "_CaseLctrNb", "_CaseRef", "_CmprmsdCrdntl", "_ConfRptgDt", "_CrdhldrRptgDt", "_InvstgtnSts", "_MktSgmt", "_OthrActn", "_OthrRptgNtty", "_OthrTp", "_RptgNtty", "_SubmitrCaseRef", "_Tp"]
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
	def Arrst(self):
		return self._Arrst

	@Arrst.setter
	def Arrst(self, value):
		self._Arrst = value if type(value) != base_types.auto else self.make_default("Arrst")

	@Arrst.deleter
	def Arrst(self):
		del self._Arrst
		self._Arrst = None

	@property
	def CaseLctrNb(self):
		return self._CaseLctrNb

	@CaseLctrNb.setter
	def CaseLctrNb(self, value):
		self._CaseLctrNb = value if type(value) != base_types.auto else self.make_default("CaseLctrNb")

	@CaseLctrNb.deleter
	def CaseLctrNb(self):
		del self._CaseLctrNb
		self._CaseLctrNb = None

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
	def CmprmsdCrdntl(self):
		return self._CmprmsdCrdntl

	@CmprmsdCrdntl.setter
	def CmprmsdCrdntl(self, value):
		self._CmprmsdCrdntl = value if type(value) != base_types.auto else self.make_default("CmprmsdCrdntl")

	@CmprmsdCrdntl.deleter
	def CmprmsdCrdntl(self):
		del self._CmprmsdCrdntl
		self._CmprmsdCrdntl = None

	@property
	def ConfRptgDt(self):
		return self._ConfRptgDt

	@ConfRptgDt.setter
	def ConfRptgDt(self, value):
		self._ConfRptgDt = value if type(value) != base_types.auto else self.make_default("ConfRptgDt")

	@ConfRptgDt.deleter
	def ConfRptgDt(self):
		del self._ConfRptgDt
		self._ConfRptgDt = None

	@property
	def CrdhldrRptgDt(self):
		return self._CrdhldrRptgDt

	@CrdhldrRptgDt.setter
	def CrdhldrRptgDt(self, value):
		self._CrdhldrRptgDt = value if type(value) != base_types.auto else self.make_default("CrdhldrRptgDt")

	@CrdhldrRptgDt.deleter
	def CrdhldrRptgDt(self):
		del self._CrdhldrRptgDt
		self._CrdhldrRptgDt = None

	@property
	def InvstgtnSts(self):
		return self._InvstgtnSts

	@InvstgtnSts.setter
	def InvstgtnSts(self, value):
		self._InvstgtnSts = value if type(value) != base_types.auto else self.make_default("InvstgtnSts")

	@InvstgtnSts.deleter
	def InvstgtnSts(self):
		del self._InvstgtnSts
		self._InvstgtnSts = None

	@property
	def MktSgmt(self):
		return self._MktSgmt

	@MktSgmt.setter
	def MktSgmt(self, value):
		self._MktSgmt = value if type(value) != base_types.auto else self.make_default("MktSgmt")

	@MktSgmt.deleter
	def MktSgmt(self):
		del self._MktSgmt
		self._MktSgmt = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=FraudReportingAction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Arrst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseLctrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmprmsdCrdntl', type=AuthenticationMethod12Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnSts', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSgmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrActn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRptgNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=PartyType26Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrCaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FraudType1Code, min=1, max=1, mutex_group=None, array=False),
	))

