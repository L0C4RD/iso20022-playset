# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Vote15
from . import Vote21

class Vote18Choice(base_types._BaseFieldType):

	__slots__ = ["_GblVoteInstr", "_VoteInstr"]
	@property
	def GblVoteInstr(self):
		return self._GblVoteInstr

	@GblVoteInstr.setter
	def GblVoteInstr(self, value):
		self._GblVoteInstr = value if value is not None else base_types.UninitialisedField(self, 'GblVoteInstr', Vote15, True)

	@GblVoteInstr.deleter
	def GblVoteInstr(self):
		del self._GblVoteInstr
		self._GblVoteInstr = base_types.UninitialisedField(self, 'GblVoteInstr', Vote15, True)

	@property
	def VoteInstr(self):
		return self._VoteInstr

	@VoteInstr.setter
	def VoteInstr(self, value):
		self._VoteInstr = value if value is not None else base_types.UninitialisedField(self, 'VoteInstr', Vote21, True)

	@VoteInstr.deleter
	def VoteInstr(self):
		del self._VoteInstr
		self._VoteInstr = base_types.UninitialisedField(self, 'VoteInstr', Vote21, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GblVoteInstr', type=Vote15, min=1, max=1000, mutex_group=1, array=True),
		base_types.FieldEntry(name='VoteInstr', type=Vote21, min=1, max=1000, mutex_group=1, array=True),
	))