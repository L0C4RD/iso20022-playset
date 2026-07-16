# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountStatusUpdateInstruction1Choice
from . import AccountStatusUpdateInstructionReason1Choice

class AccountStatusUpdateInstruction1(base_types._BaseFieldType):

	__slots__ = ["_UpdInstr", "_UpdInstrRsn"]
	@property
	def UpdInstr(self):
		return self._UpdInstr

	@UpdInstr.setter
	def UpdInstr(self, value):
		self._UpdInstr = value if value is not None else base_types.UninitialisedField(self, 'UpdInstr', AccountStatusUpdateInstruction1Choice, False)

	@UpdInstr.deleter
	def UpdInstr(self):
		del self._UpdInstr
		self._UpdInstr = base_types.UninitialisedField(self, 'UpdInstr', AccountStatusUpdateInstruction1Choice, False)

	@property
	def UpdInstrRsn(self):
		return self._UpdInstrRsn

	@UpdInstrRsn.setter
	def UpdInstrRsn(self, value):
		self._UpdInstrRsn = value if value is not None else base_types.UninitialisedField(self, 'UpdInstrRsn', AccountStatusUpdateInstructionReason1Choice, False)

	@UpdInstrRsn.deleter
	def UpdInstrRsn(self):
		del self._UpdInstrRsn
		self._UpdInstrRsn = base_types.UninitialisedField(self, 'UpdInstrRsn', AccountStatusUpdateInstructionReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='UpdInstr', type=AccountStatusUpdateInstruction1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdInstrRsn', type=AccountStatusUpdateInstructionReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))