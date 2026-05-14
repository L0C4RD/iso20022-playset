# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Case6 import Case6
from ._CaseAssignment6 import CaseAssignment6
from ._InvestigationStatus6Choice import InvestigationStatus6Choice
from ._ResolutionData5 import ResolutionData5
from ._SupplementaryData1 import SupplementaryData1
from ._UnderlyingTransaction35 import UnderlyingTransaction35

class ResolutionOfInvestigationV14(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_CxlDtls", "_RsltnRltdInf", "_RslvdCase", "_SplmtryData", "_Sts"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != base_types.auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

	@property
	def CxlDtls(self):
		return self._CxlDtls

	@CxlDtls.setter
	def CxlDtls(self, value):
		self._CxlDtls = value if type(value) != base_types.auto else self.make_default("CxlDtls")

	@CxlDtls.deleter
	def CxlDtls(self):
		del self._CxlDtls
		self._CxlDtls = None

	@property
	def RsltnRltdInf(self):
		return self._RsltnRltdInf

	@RsltnRltdInf.setter
	def RsltnRltdInf(self, value):
		self._RsltnRltdInf = value if type(value) != base_types.auto else self.make_default("RsltnRltdInf")

	@RsltnRltdInf.deleter
	def RsltnRltdInf(self):
		del self._RsltnRltdInf
		self._RsltnRltdInf = None

	@property
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if type(value) != base_types.auto else self.make_default("RslvdCase")

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlDtls', type=UnderlyingTransaction35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsltnRltdInf', type=ResolutionData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=InvestigationStatus6Choice, min=1, max=1, mutex_group=None, array=False),
	))