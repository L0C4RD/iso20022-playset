# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstructionStatus13Choice
from . import Max35Text

class DetailedInstructionStatus21(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_InstrSts", "_SnglInstrId", "_SubAcctId"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def InstrSts(self):
		return self._InstrSts

	@InstrSts.setter
	def InstrSts(self, value):
		self._InstrSts = value if value is not None else base_types.UninitialisedField(self, 'InstrSts', InstructionStatus13Choice, False)

	@InstrSts.deleter
	def InstrSts(self):
		del self._InstrSts
		self._InstrSts = base_types.UninitialisedField(self, 'InstrSts', InstructionStatus13Choice, False)

	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if value is not None else base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if value is not None else base_types.UninitialisedField(self, 'SubAcctId', Max35Text, False)

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = base_types.UninitialisedField(self, 'SubAcctId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrSts', type=InstructionStatus13Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))