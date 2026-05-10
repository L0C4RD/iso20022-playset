from . import base_types
from ._SettlementDailyFailureReason1Choice import SettlementDailyFailureReason1Choice

class SettlementFailsDailyInstructionType3(base_types._BaseFieldType):

	__slots__ = ["_FreeOfPmt", "_DlvryWthPmt", "_PmtFreeOfDlvry", "_DlvryVrssPmt"]
	@property
	def FreeOfPmt(self):
		return self._FreeOfPmt

	@FreeOfPmt.setter
	def FreeOfPmt(self, value):
		self._FreeOfPmt = value if type(value) != base_types.auto else self.make_default("FreeOfPmt")

	@FreeOfPmt.deleter
	def FreeOfPmt(self):
		del self._FreeOfPmt
		self._FreeOfPmt = None

	@property
	def DlvryWthPmt(self):
		return self._DlvryWthPmt

	@DlvryWthPmt.setter
	def DlvryWthPmt(self, value):
		self._DlvryWthPmt = value if type(value) != base_types.auto else self.make_default("DlvryWthPmt")

	@DlvryWthPmt.deleter
	def DlvryWthPmt(self):
		del self._DlvryWthPmt
		self._DlvryWthPmt = None

	@property
	def PmtFreeOfDlvry(self):
		return self._PmtFreeOfDlvry

	@PmtFreeOfDlvry.setter
	def PmtFreeOfDlvry(self, value):
		self._PmtFreeOfDlvry = value if type(value) != base_types.auto else self.make_default("PmtFreeOfDlvry")

	@PmtFreeOfDlvry.deleter
	def PmtFreeOfDlvry(self):
		del self._PmtFreeOfDlvry
		self._PmtFreeOfDlvry = None

	@property
	def DlvryVrssPmt(self):
		return self._DlvryVrssPmt

	@DlvryVrssPmt.setter
	def DlvryVrssPmt(self, value):
		self._DlvryVrssPmt = value if type(value) != base_types.auto else self.make_default("DlvryVrssPmt")

	@DlvryVrssPmt.deleter
	def DlvryVrssPmt(self):
		del self._DlvryVrssPmt
		self._DlvryVrssPmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FreeOfPmt', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryWthPmt', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFreeOfDlvry', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryVrssPmt', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
	))

