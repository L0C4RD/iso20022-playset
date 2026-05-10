import base_types
import Max35Text

class InstructionType2Choice(base_types._BaseFieldType):

	__slots__ = ["_InstrCxlId", "_InstrId"]
	@property
	def InstrCxlId(self):
		return self._InstrCxlId

	@InstrCxlId.setter
	def InstrCxlId(self, value):
		self._InstrCxlId = value if type(value) != auto else self.make_default("InstrCxlId")

	@InstrCxlId.deleter
	def InstrCxlId(self):
		del self._InstrCxlId
		self._InstrCxlId = None

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if type(value) != auto else self.make_default("InstrId")

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrCxlId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

