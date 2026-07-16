# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class InstructionType2Choice(base_types._BaseFieldType):

	__slots__ = ["_InstrCxlId", "_InstrId"]
	@property
	def InstrCxlId(self):
		return self._InstrCxlId

	@InstrCxlId.setter
	def InstrCxlId(self, value):
		self._InstrCxlId = value if value is not None else base_types.UninitialisedField(self, 'InstrCxlId', Max35Text, False)

	@InstrCxlId.deleter
	def InstrCxlId(self):
		del self._InstrCxlId
		self._InstrCxlId = base_types.UninitialisedField(self, 'InstrCxlId', Max35Text, False)

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrCxlId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))