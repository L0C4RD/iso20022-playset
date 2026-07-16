# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class MeetingInstructionIdentification1(base_types._BaseFieldType):

	__slots__ = ["_MtgInstrId", "_SnglInstrId"]
	@property
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if value is not None else base_types.UninitialisedField(self, 'MtgInstrId', Max35Text, False)

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = base_types.UninitialisedField(self, 'MtgInstrId', Max35Text, False)

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
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))