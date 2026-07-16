# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import CaseAssignment6
from . import CaseStatus2
from . import ReportHeader7
from . import SupplementaryData1

class CaseStatusReportV06(base_types._BaseFieldType):

	__slots__ = ["_Case", "_Hdr", "_NewAssgnmt", "_SplmtryData", "_Sts"]
	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if value is not None else base_types.UninitialisedField(self, 'Case', Case6, False)

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = base_types.UninitialisedField(self, 'Case', Case6, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', ReportHeader7, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', ReportHeader7, False)

	@property
	def NewAssgnmt(self):
		return self._NewAssgnmt

	@NewAssgnmt.setter
	def NewAssgnmt(self, value):
		self._NewAssgnmt = value if value is not None else base_types.UninitialisedField(self, 'NewAssgnmt', CaseAssignment6, False)

	@NewAssgnmt.deleter
	def NewAssgnmt(self):
		del self._NewAssgnmt
		self._NewAssgnmt = base_types.UninitialisedField(self, 'NewAssgnmt', CaseAssignment6, False)

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
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', CaseStatus2, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', CaseStatus2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Case', type=Case6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=ReportHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAssgnmt', type=CaseAssignment6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=CaseStatus2, min=1, max=1, mutex_group=None, array=False),
	))