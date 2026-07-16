# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Vote15Choice
from . import VoteInstructionForMeetingResolution3Choice

class VoteDetails6(base_types._BaseFieldType):

	__slots__ = ["_VoteInstrForAgndRsltn", "_VoteInstrForMtgRsltn"]
	@property
	def VoteInstrForAgndRsltn(self):
		return self._VoteInstrForAgndRsltn

	@VoteInstrForAgndRsltn.setter
	def VoteInstrForAgndRsltn(self, value):
		self._VoteInstrForAgndRsltn = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrForAgndRsltn', Vote15Choice, False)

	@VoteInstrForAgndRsltn.deleter
	def VoteInstrForAgndRsltn(self):
		del self._VoteInstrForAgndRsltn
		self._VoteInstrForAgndRsltn = base_types.UninitialisedField(self, 'VoteInstrForAgndRsltn', Vote15Choice, False)

	@property
	def VoteInstrForMtgRsltn(self):
		return self._VoteInstrForMtgRsltn

	@VoteInstrForMtgRsltn.setter
	def VoteInstrForMtgRsltn(self, value):
		self._VoteInstrForMtgRsltn = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrForMtgRsltn', VoteInstructionForMeetingResolution3Choice, False)

	@VoteInstrForMtgRsltn.deleter
	def VoteInstrForMtgRsltn(self):
		del self._VoteInstrForMtgRsltn
		self._VoteInstrForMtgRsltn = base_types.UninitialisedField(self, 'VoteInstrForMtgRsltn', VoteInstructionForMeetingResolution3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteInstrForAgndRsltn', type=Vote15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrForMtgRsltn', type=VoteInstructionForMeetingResolution3Choice, min=0, max=1, mutex_group=None, array=False),
	))