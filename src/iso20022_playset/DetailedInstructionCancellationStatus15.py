import base_types
import Max35Text
import CancellationStatus32Choice

class DetailedInstructionCancellationStatus15(base_types._BaseFieldType):

	__slots__ = ["_SubAcctId", "_SnglInstrCxlId", "_AcctId", "_InstrCxlSts"]
	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if type(value) != auto else self.make_default("SubAcctId")

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = None

	@property
	def SnglInstrCxlId(self):
		return self._SnglInstrCxlId

	@SnglInstrCxlId.setter
	def SnglInstrCxlId(self, value):
		self._SnglInstrCxlId = value if type(value) != auto else self.make_default("SnglInstrCxlId")

	@SnglInstrCxlId.deleter
	def SnglInstrCxlId(self):
		del self._SnglInstrCxlId
		self._SnglInstrCxlId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def InstrCxlSts(self):
		return self._InstrCxlSts

	@InstrCxlSts.setter
	def InstrCxlSts(self, value):
		self._InstrCxlSts = value if type(value) != auto else self.make_default("InstrCxlSts")

	@InstrCxlSts.deleter
	def InstrCxlSts(self):
		del self._InstrCxlSts
		self._InstrCxlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrCxlId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlSts', type=CancellationStatus32Choice, min=1, max=1, mutex_group=None, array=False),
	))

