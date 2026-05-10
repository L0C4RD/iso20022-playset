from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .CaseAssignment6 import CaseAssignment6
from .Case6 import Case6
from .ReportHeader7 import ReportHeader7
from .CaseForwardingNotification3 import CaseForwardingNotification3

class NotificationOfCaseAssignmentV06(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SplmtryData", "_Ntfctn", "_Assgnmt", "_Case"]
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
	def Ntfctn(self):
		return self._Ntfctn

	@Ntfctn.setter
	def Ntfctn(self, value):
		self._Ntfctn = value if type(value) != base_types.auto else self.make_default("Ntfctn")

	@Ntfctn.deleter
	def Ntfctn(self):
		del self._Ntfctn
		self._Ntfctn = None

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
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != base_types.auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=ReportHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ntfctn', type=CaseForwardingNotification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=1, max=1, mutex_group=None, array=False),
	))

