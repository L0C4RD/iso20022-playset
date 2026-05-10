from . import base_types
from ._ReportHeader7 import ReportHeader7
from ._Case6 import Case6
from ._CaseAssignment6 import CaseAssignment6
from ._SupplementaryData1 import SupplementaryData1
from ._CaseStatus2 import CaseStatus2

class CaseStatusReportV06(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_Case", "_Sts", "_NewAssgnmt", "_SplmtryData"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != base_types.auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

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

	@property
	def NewAssgnmt(self):
		return self._NewAssgnmt

	@NewAssgnmt.setter
	def NewAssgnmt(self, value):
		self._NewAssgnmt = value if type(value) != base_types.auto else self.make_default("NewAssgnmt")

	@NewAssgnmt.deleter
	def NewAssgnmt(self):
		del self._NewAssgnmt
		self._NewAssgnmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=ReportHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=CaseStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAssgnmt', type=CaseAssignment6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

