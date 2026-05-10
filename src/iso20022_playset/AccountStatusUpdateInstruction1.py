import base_types
import AccountStatusUpdateInstructionReason1Choice
import AccountStatusUpdateInstruction1Choice

class AccountStatusUpdateInstruction1(base_types._BaseFieldType):

	__slots__ = ["_UpdInstr", "_UpdInstrRsn"]
	@property
	def UpdInstr(self):
		return self._UpdInstr

	@UpdInstr.setter
	def UpdInstr(self, value):
		self._UpdInstr = value if type(value) != auto else self.make_default("UpdInstr")

	@UpdInstr.deleter
	def UpdInstr(self):
		del self._UpdInstr
		self._UpdInstr = None

	@property
	def UpdInstrRsn(self):
		return self._UpdInstrRsn

	@UpdInstrRsn.setter
	def UpdInstrRsn(self, value):
		self._UpdInstrRsn = value if type(value) != auto else self.make_default("UpdInstrRsn")

	@UpdInstrRsn.deleter
	def UpdInstrRsn(self):
		del self._UpdInstrRsn
		self._UpdInstrRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UpdInstr', type=AccountStatusUpdateInstruction1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdInstrRsn', type=AccountStatusUpdateInstructionReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))

