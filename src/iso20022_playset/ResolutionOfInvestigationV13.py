from . import base_types
import StatementResolutionEntry5
import UnderlyingTransaction32
import SupplementaryData1
import CorrectiveTransaction5Choice
import CaseAssignment6
import ResolutionData5
import ClaimNonReceipt3Choice
import PaymentTransaction157
import Case6
import InvestigationStatus6Choice

class ResolutionOfInvestigationV13(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_SplmtryData", "_RsltnRltdInf", "_CxlDtls", "_ClmNonRctDtls", "_ModDtls", "_Sts", "_RslvdCase", "_StmtDtls", "_CrrctnTx"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def RsltnRltdInf(self):
		return self._RsltnRltdInf

	@RsltnRltdInf.setter
	def RsltnRltdInf(self, value):
		self._RsltnRltdInf = value if type(value) != auto else self.make_default("RsltnRltdInf")

	@RsltnRltdInf.deleter
	def RsltnRltdInf(self):
		del self._RsltnRltdInf
		self._RsltnRltdInf = None

	@property
	def CxlDtls(self):
		return self._CxlDtls

	@CxlDtls.setter
	def CxlDtls(self, value):
		self._CxlDtls = value if type(value) != auto else self.make_default("CxlDtls")

	@CxlDtls.deleter
	def CxlDtls(self):
		del self._CxlDtls
		self._CxlDtls = None

	@property
	def ClmNonRctDtls(self):
		return self._ClmNonRctDtls

	@ClmNonRctDtls.setter
	def ClmNonRctDtls(self, value):
		self._ClmNonRctDtls = value if type(value) != auto else self.make_default("ClmNonRctDtls")

	@ClmNonRctDtls.deleter
	def ClmNonRctDtls(self):
		del self._ClmNonRctDtls
		self._ClmNonRctDtls = None

	@property
	def ModDtls(self):
		return self._ModDtls

	@ModDtls.setter
	def ModDtls(self, value):
		self._ModDtls = value if type(value) != auto else self.make_default("ModDtls")

	@ModDtls.deleter
	def ModDtls(self):
		del self._ModDtls
		self._ModDtls = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if type(value) != auto else self.make_default("RslvdCase")

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = None

	@property
	def StmtDtls(self):
		return self._StmtDtls

	@StmtDtls.setter
	def StmtDtls(self, value):
		self._StmtDtls = value if type(value) != auto else self.make_default("StmtDtls")

	@StmtDtls.deleter
	def StmtDtls(self):
		del self._StmtDtls
		self._StmtDtls = None

	@property
	def CrrctnTx(self):
		return self._CrrctnTx

	@CrrctnTx.setter
	def CrrctnTx(self, value):
		self._CrrctnTx = value if type(value) != auto else self.make_default("CrrctnTx")

	@CrrctnTx.deleter
	def CrrctnTx(self):
		del self._CrrctnTx
		self._CrrctnTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsltnRltdInf', type=ResolutionData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlDtls', type=UnderlyingTransaction32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClmNonRctDtls', type=ClaimNonReceipt3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModDtls', type=PaymentTransaction157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=InvestigationStatus6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtls', type=StatementResolutionEntry5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrctnTx', type=CorrectiveTransaction5Choice, min=0, max=1, mutex_group=None, array=False),
	))

