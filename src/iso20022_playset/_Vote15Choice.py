# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Vote16Choice
from . import VoteInstructionType1Choice

class Vote15Choice(base_types._BaseFieldType):

	__slots__ = ["_VoteForAllAgndRsltns", "_VotePerAgndRsltn"]
	@property
	def VoteForAllAgndRsltns(self):
		return self._VoteForAllAgndRsltns

	@VoteForAllAgndRsltns.setter
	def VoteForAllAgndRsltns(self, value):
		self._VoteForAllAgndRsltns = value if value is not None else base_types.UninitialisedField(self, 'VoteForAllAgndRsltns', VoteInstructionType1Choice, False)

	@VoteForAllAgndRsltns.deleter
	def VoteForAllAgndRsltns(self):
		del self._VoteForAllAgndRsltns
		self._VoteForAllAgndRsltns = base_types.UninitialisedField(self, 'VoteForAllAgndRsltns', VoteInstructionType1Choice, False)

	@property
	def VotePerAgndRsltn(self):
		return self._VotePerAgndRsltn

	@VotePerAgndRsltn.setter
	def VotePerAgndRsltn(self, value):
		self._VotePerAgndRsltn = value if value is not None else base_types.UninitialisedField(self, 'VotePerAgndRsltn', Vote16Choice, False)

	@VotePerAgndRsltn.deleter
	def VotePerAgndRsltn(self):
		del self._VotePerAgndRsltn
		self._VotePerAgndRsltn = base_types.UninitialisedField(self, 'VotePerAgndRsltn', Vote16Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteForAllAgndRsltns', type=VoteInstructionType1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VotePerAgndRsltn', type=Vote16Choice, min=0, max=1, mutex_group=1, array=False),
	))