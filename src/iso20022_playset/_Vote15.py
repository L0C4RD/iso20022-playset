# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._VoteInstructionType2Choice import VoteInstructionType2Choice

class Vote15(base_types._BaseFieldType):

	__slots__ = ["_IssrLabl", "_VoteOptn"]
	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if type(value) != base_types.auto else self.make_default("IssrLabl")

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = None

	@property
	def VoteOptn(self):
		return self._VoteOptn

	@VoteOptn.setter
	def VoteOptn(self, value):
		self._VoteOptn = value if type(value) != base_types.auto else self.make_default("VoteOptn")

	@VoteOptn.deleter
	def VoteOptn(self):
		del self._VoteOptn
		self._VoteOptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrLabl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteOptn', type=VoteInstructionType2Choice, min=1, max=1, mutex_group=None, array=False),
	))