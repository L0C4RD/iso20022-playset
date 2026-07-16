# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatus35Choice
from . import Max35Text

class DetailedInstructionCancellationStatus16(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_InstrCxlSts", "_SnglInstrCxlId", "_SubAcctId"]
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
	def InstrCxlSts(self):
		return self._InstrCxlSts

	@InstrCxlSts.setter
	def InstrCxlSts(self, value):
		self._InstrCxlSts = value if value is not None else base_types.UninitialisedField(self, 'InstrCxlSts', CancellationStatus35Choice, False)

	@InstrCxlSts.deleter
	def InstrCxlSts(self):
		del self._InstrCxlSts
		self._InstrCxlSts = base_types.UninitialisedField(self, 'InstrCxlSts', CancellationStatus35Choice, False)

	@property
	def SnglInstrCxlId(self):
		return self._SnglInstrCxlId

	@SnglInstrCxlId.setter
	def SnglInstrCxlId(self, value):
		self._SnglInstrCxlId = value if value is not None else base_types.UninitialisedField(self, 'SnglInstrCxlId', Max35Text, False)

	@SnglInstrCxlId.deleter
	def SnglInstrCxlId(self):
		del self._SnglInstrCxlId
		self._SnglInstrCxlId = base_types.UninitialisedField(self, 'SnglInstrCxlId', Max35Text, False)

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
		base_types.FieldEntry(name='InstrCxlSts', type=CancellationStatus35Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrCxlId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))