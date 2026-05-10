import base_types
import Vote15
import Vote14

class Vote16Choice(base_types._BaseFieldType):

	__slots__ = ["_GblVoteInstr", "_VoteInstr"]
	@property
	def GblVoteInstr(self):
		return self._GblVoteInstr

	@GblVoteInstr.setter
	def GblVoteInstr(self, value):
		self._GblVoteInstr = value if type(value) != auto else self.make_default("GblVoteInstr")

	@GblVoteInstr.deleter
	def GblVoteInstr(self):
		del self._GblVoteInstr
		self._GblVoteInstr = None

	@property
	def VoteInstr(self):
		return self._VoteInstr

	@VoteInstr.setter
	def VoteInstr(self, value):
		self._VoteInstr = value if type(value) != auto else self.make_default("VoteInstr")

	@VoteInstr.deleter
	def VoteInstr(self):
		del self._VoteInstr
		self._VoteInstr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GblVoteInstr', type=Vote15, min=1, max=1000, mutex_group=1, array=True),
		base_types.FieldEntry(name='VoteInstr', type=Vote14, min=1, max=1000, mutex_group=1, array=True),
	))

