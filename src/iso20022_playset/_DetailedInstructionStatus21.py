from . import base_types
from ._Max35Text import Max35Text
from ._InstructionStatus13Choice import InstructionStatus13Choice

class DetailedInstructionStatus21(base_types._BaseFieldType):

	__slots__ = ["_SnglInstrId", "_InstrSts", "_SubAcctId", "_AcctId"]
	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if type(value) != base_types.auto else self.make_default("SnglInstrId")

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = None

	@property
	def InstrSts(self):
		return self._InstrSts

	@InstrSts.setter
	def InstrSts(self, value):
		self._InstrSts = value if type(value) != base_types.auto else self.make_default("InstrSts")

	@InstrSts.deleter
	def InstrSts(self):
		del self._InstrSts
		self._InstrSts = None

	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if type(value) != base_types.auto else self.make_default("SubAcctId")

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrSts', type=InstructionStatus13Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

