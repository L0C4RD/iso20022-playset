from . import base_types
from .VoteInstructionType1Choice import VoteInstructionType1Choice
from .Vote16Choice import Vote16Choice

class Vote15Choice(base_types._BaseFieldType):

	__slots__ = ["_VoteForAllAgndRsltns", "_VotePerAgndRsltn"]
	@property
	def VoteForAllAgndRsltns(self):
		return self._VoteForAllAgndRsltns

	@VoteForAllAgndRsltns.setter
	def VoteForAllAgndRsltns(self, value):
		self._VoteForAllAgndRsltns = value if type(value) != auto else self.make_default("VoteForAllAgndRsltns")

	@VoteForAllAgndRsltns.deleter
	def VoteForAllAgndRsltns(self):
		del self._VoteForAllAgndRsltns
		self._VoteForAllAgndRsltns = None

	@property
	def VotePerAgndRsltn(self):
		return self._VotePerAgndRsltn

	@VotePerAgndRsltn.setter
	def VotePerAgndRsltn(self, value):
		self._VotePerAgndRsltn = value if type(value) != auto else self.make_default("VotePerAgndRsltn")

	@VotePerAgndRsltn.deleter
	def VotePerAgndRsltn(self):
		del self._VotePerAgndRsltn
		self._VotePerAgndRsltn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteForAllAgndRsltns', type=VoteInstructionType1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VotePerAgndRsltn', type=Vote16Choice, min=0, max=1, mutex_group=1, array=False),
	))

