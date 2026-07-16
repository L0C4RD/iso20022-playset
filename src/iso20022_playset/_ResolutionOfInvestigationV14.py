# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import CaseAssignment6
from . import InvestigationStatus6Choice
from . import ResolutionData5
from . import SupplementaryData1
from . import UnderlyingTransaction35

class ResolutionOfInvestigationV14(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_CxlDtls", "_RsltnRltdInf", "_RslvdCase", "_SplmtryData", "_Sts"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if value is not None else base_types.UninitialisedField(self, 'Assgnmt', CaseAssignment6, False)

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = base_types.UninitialisedField(self, 'Assgnmt', CaseAssignment6, False)

	@property
	def CxlDtls(self):
		return self._CxlDtls

	@CxlDtls.setter
	def CxlDtls(self, value):
		self._CxlDtls = value if value is not None else base_types.UninitialisedField(self, 'CxlDtls', UnderlyingTransaction35, True)

	@CxlDtls.deleter
	def CxlDtls(self):
		del self._CxlDtls
		self._CxlDtls = base_types.UninitialisedField(self, 'CxlDtls', UnderlyingTransaction35, True)

	@property
	def RsltnRltdInf(self):
		return self._RsltnRltdInf

	@RsltnRltdInf.setter
	def RsltnRltdInf(self, value):
		self._RsltnRltdInf = value if value is not None else base_types.UninitialisedField(self, 'RsltnRltdInf', ResolutionData5, False)

	@RsltnRltdInf.deleter
	def RsltnRltdInf(self):
		del self._RsltnRltdInf
		self._RsltnRltdInf = base_types.UninitialisedField(self, 'RsltnRltdInf', ResolutionData5, False)

	@property
	def RslvdCase(self):
		return self._RslvdCase

	@RslvdCase.setter
	def RslvdCase(self, value):
		self._RslvdCase = value if value is not None else base_types.UninitialisedField(self, 'RslvdCase', Case6, False)

	@RslvdCase.deleter
	def RslvdCase(self):
		del self._RslvdCase
		self._RslvdCase = base_types.UninitialisedField(self, 'RslvdCase', Case6, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', InvestigationStatus6Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', InvestigationStatus6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlDtls', type=UnderlyingTransaction35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsltnRltdInf', type=ResolutionData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RslvdCase', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=InvestigationStatus6Choice, min=1, max=1, mutex_group=None, array=False),
	))