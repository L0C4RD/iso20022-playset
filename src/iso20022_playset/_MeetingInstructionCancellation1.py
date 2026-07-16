# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class MeetingInstructionCancellation1(base_types._BaseFieldType):

	__slots__ = ["_MtgInstrCxlReqId", "_SnglInstrId"]
	@property
	def MtgInstrCxlReqId(self):
		return self._MtgInstrCxlReqId

	@MtgInstrCxlReqId.setter
	def MtgInstrCxlReqId(self, value):
		self._MtgInstrCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'MtgInstrCxlReqId', Max35Text, False)

	@MtgInstrCxlReqId.deleter
	def MtgInstrCxlReqId(self):
		del self._MtgInstrCxlReqId
		self._MtgInstrCxlReqId = base_types.UninitialisedField(self, 'MtgInstrCxlReqId', Max35Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtgInstrCxlReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))