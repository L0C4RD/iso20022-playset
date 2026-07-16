# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatus31Choice
from . import DetailedInstructionStatus21

class InstructionTypeStatus7Choice(base_types._BaseFieldType):

	__slots__ = ["_CxlSts", "_InstrSts"]
	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if value is not None else base_types.UninitialisedField(self, 'CxlSts', CancellationStatus31Choice, False)

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = base_types.UninitialisedField(self, 'CxlSts', CancellationStatus31Choice, False)

	@property
	def InstrSts(self):
		return self._InstrSts

	@InstrSts.setter
	def InstrSts(self, value):
		self._InstrSts = value if value is not None else base_types.UninitialisedField(self, 'InstrSts', DetailedInstructionStatus21, True)

	@InstrSts.deleter
	def InstrSts(self):
		del self._InstrSts
		self._InstrSts = base_types.UninitialisedField(self, 'InstrSts', DetailedInstructionStatus21, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlSts', type=CancellationStatus31Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrSts', type=DetailedInstructionStatus21, min=1, max=None, mutex_group=1, array=True),
	))