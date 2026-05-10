from . import base_types
from .Max35Text import Max35Text

class MeetingInstructionCancellation1(base_types._BaseFieldType):

	__slots__ = ["_SnglInstrId", "_MtgInstrCxlReqId"]
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
	def MtgInstrCxlReqId(self):
		return self._MtgInstrCxlReqId

	@MtgInstrCxlReqId.setter
	def MtgInstrCxlReqId(self, value):
		self._MtgInstrCxlReqId = value if type(value) != base_types.auto else self.make_default("MtgInstrCxlReqId")

	@MtgInstrCxlReqId.deleter
	def MtgInstrCxlReqId(self):
		del self._MtgInstrCxlReqId
		self._MtgInstrCxlReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgInstrCxlReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

