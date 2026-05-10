import base_types
import Max35Text

class MeetingInstructionIdentification1(base_types._BaseFieldType):

	__slots__ = ["_SnglInstrId", "_MtgInstrId"]
	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if type(value) != auto else self.make_default("SnglInstrId")

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = None

	@property
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if type(value) != auto else self.make_default("MtgInstrId")

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

