# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestorTypeIdentification1
from . import Vote17Choice
from . import VoteInstructionForMeetingResolution3Choice

class VoteDetails7(base_types._BaseFieldType):

	__slots__ = ["_InvstrTpId", "_VoteInstrForAgndRsltn", "_VoteInstrForMtgRsltn"]
	@property
	def InvstrTpId(self):
		return self._InvstrTpId

	@InvstrTpId.setter
	def InvstrTpId(self, value):
		self._InvstrTpId = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpId', InvestorTypeIdentification1, False)

	@InvstrTpId.deleter
	def InvstrTpId(self):
		del self._InvstrTpId
		self._InvstrTpId = base_types.UninitialisedField(self, 'InvstrTpId', InvestorTypeIdentification1, False)

	@property
	def VoteInstrForAgndRsltn(self):
		return self._VoteInstrForAgndRsltn

	@VoteInstrForAgndRsltn.setter
	def VoteInstrForAgndRsltn(self, value):
		self._VoteInstrForAgndRsltn = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrForAgndRsltn', Vote17Choice, False)

	@VoteInstrForAgndRsltn.deleter
	def VoteInstrForAgndRsltn(self):
		del self._VoteInstrForAgndRsltn
		self._VoteInstrForAgndRsltn = base_types.UninitialisedField(self, 'VoteInstrForAgndRsltn', Vote17Choice, False)

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
		base_types.FieldEntry(name='InvstrTpId', type=InvestorTypeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrForAgndRsltn', type=Vote17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrForMtgRsltn', type=VoteInstructionForMeetingResolution3Choice, min=0, max=1, mutex_group=None, array=False),
	))