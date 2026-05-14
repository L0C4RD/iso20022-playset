# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Vote18Choice import Vote18Choice
from ._VoteInstructionType3Choice import VoteInstructionType3Choice

class Vote17Choice(base_types._BaseFieldType):

	__slots__ = ["_VoteForAllAgndRsltns", "_VotePerAgndRsltn"]
	@property
	def VoteForAllAgndRsltns(self):
		return self._VoteForAllAgndRsltns

	@VoteForAllAgndRsltns.setter
	def VoteForAllAgndRsltns(self, value):
		self._VoteForAllAgndRsltns = value if type(value) != base_types.auto else self.make_default("VoteForAllAgndRsltns")

	@VoteForAllAgndRsltns.deleter
	def VoteForAllAgndRsltns(self):
		del self._VoteForAllAgndRsltns
		self._VoteForAllAgndRsltns = None

	@property
	def VotePerAgndRsltn(self):
		return self._VotePerAgndRsltn

	@VotePerAgndRsltn.setter
	def VotePerAgndRsltn(self, value):
		self._VotePerAgndRsltn = value if type(value) != base_types.auto else self.make_default("VotePerAgndRsltn")

	@VotePerAgndRsltn.deleter
	def VotePerAgndRsltn(self):
		del self._VotePerAgndRsltn
		self._VotePerAgndRsltn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteForAllAgndRsltns', type=VoteInstructionType3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VotePerAgndRsltn', type=Vote18Choice, min=0, max=1, mutex_group=1, array=False),
	))