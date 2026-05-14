from . import base_types
from ._InvestorTypeIdentification1 import InvestorTypeIdentification1
from ._Vote17Choice import Vote17Choice
from ._VoteInstructionForMeetingResolution3Choice import VoteInstructionForMeetingResolution3Choice

class VoteDetails7(base_types._BaseFieldType):

	__slots__ = ["_InvstrTpId", "_VoteInstrForAgndRsltn", "_VoteInstrForMtgRsltn"]
	@property
	def InvstrTpId(self):
		return self._InvstrTpId

	@InvstrTpId.setter
	def InvstrTpId(self, value):
		self._InvstrTpId = value if type(value) != base_types.auto else self.make_default("InvstrTpId")

	@InvstrTpId.deleter
	def InvstrTpId(self):
		del self._InvstrTpId
		self._InvstrTpId = None

	@property
	def VoteInstrForAgndRsltn(self):
		return self._VoteInstrForAgndRsltn

	@VoteInstrForAgndRsltn.setter
	def VoteInstrForAgndRsltn(self, value):
		self._VoteInstrForAgndRsltn = value if type(value) != base_types.auto else self.make_default("VoteInstrForAgndRsltn")

	@VoteInstrForAgndRsltn.deleter
	def VoteInstrForAgndRsltn(self):
		del self._VoteInstrForAgndRsltn
		self._VoteInstrForAgndRsltn = None

	@property
	def VoteInstrForMtgRsltn(self):
		return self._VoteInstrForMtgRsltn

	@VoteInstrForMtgRsltn.setter
	def VoteInstrForMtgRsltn(self, value):
		self._VoteInstrForMtgRsltn = value if type(value) != base_types.auto else self.make_default("VoteInstrForMtgRsltn")

	@VoteInstrForMtgRsltn.deleter
	def VoteInstrForMtgRsltn(self):
		del self._VoteInstrForMtgRsltn
		self._VoteInstrForMtgRsltn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrTpId', type=InvestorTypeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrForAgndRsltn', type=Vote17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrForMtgRsltn', type=VoteInstructionForMeetingResolution3Choice, min=0, max=1, mutex_group=None, array=False),
	))

