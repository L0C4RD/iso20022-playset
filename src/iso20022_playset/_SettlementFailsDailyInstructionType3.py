# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementDailyFailureReason1Choice

class SettlementFailsDailyInstructionType3(base_types._BaseFieldType):

	__slots__ = ["_DlvryVrssPmt", "_DlvryWthPmt", "_FreeOfPmt", "_PmtFreeOfDlvry"]
	@property
	def DlvryVrssPmt(self):
		return self._DlvryVrssPmt

	@DlvryVrssPmt.setter
	def DlvryVrssPmt(self, value):
		self._DlvryVrssPmt = value if value is not None else base_types.UninitialisedField(self, 'DlvryVrssPmt', SettlementDailyFailureReason1Choice, False)

	@DlvryVrssPmt.deleter
	def DlvryVrssPmt(self):
		del self._DlvryVrssPmt
		self._DlvryVrssPmt = base_types.UninitialisedField(self, 'DlvryVrssPmt', SettlementDailyFailureReason1Choice, False)

	@property
	def DlvryWthPmt(self):
		return self._DlvryWthPmt

	@DlvryWthPmt.setter
	def DlvryWthPmt(self, value):
		self._DlvryWthPmt = value if value is not None else base_types.UninitialisedField(self, 'DlvryWthPmt', SettlementDailyFailureReason1Choice, False)

	@DlvryWthPmt.deleter
	def DlvryWthPmt(self):
		del self._DlvryWthPmt
		self._DlvryWthPmt = base_types.UninitialisedField(self, 'DlvryWthPmt', SettlementDailyFailureReason1Choice, False)

	@property
	def FreeOfPmt(self):
		return self._FreeOfPmt

	@FreeOfPmt.setter
	def FreeOfPmt(self, value):
		self._FreeOfPmt = value if value is not None else base_types.UninitialisedField(self, 'FreeOfPmt', SettlementDailyFailureReason1Choice, False)

	@FreeOfPmt.deleter
	def FreeOfPmt(self):
		del self._FreeOfPmt
		self._FreeOfPmt = base_types.UninitialisedField(self, 'FreeOfPmt', SettlementDailyFailureReason1Choice, False)

	@property
	def PmtFreeOfDlvry(self):
		return self._PmtFreeOfDlvry

	@PmtFreeOfDlvry.setter
	def PmtFreeOfDlvry(self, value):
		self._PmtFreeOfDlvry = value if value is not None else base_types.UninitialisedField(self, 'PmtFreeOfDlvry', SettlementDailyFailureReason1Choice, False)

	@PmtFreeOfDlvry.deleter
	def PmtFreeOfDlvry(self):
		del self._PmtFreeOfDlvry
		self._PmtFreeOfDlvry = base_types.UninitialisedField(self, 'PmtFreeOfDlvry', SettlementDailyFailureReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryVrssPmt', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryWthPmt', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FreeOfPmt', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFreeOfDlvry', type=SettlementDailyFailureReason1Choice, min=1, max=1, mutex_group=None, array=False),
	))