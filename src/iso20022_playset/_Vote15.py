# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import VoteInstructionType2Choice

class Vote15(base_types._BaseFieldType):

	__slots__ = ["_IssrLabl", "_VoteOptn"]
	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if value is not None else base_types.UninitialisedField(self, 'IssrLabl', Max35Text, False)

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = base_types.UninitialisedField(self, 'IssrLabl', Max35Text, False)

	@property
	def VoteOptn(self):
		return self._VoteOptn

	@VoteOptn.setter
	def VoteOptn(self, value):
		self._VoteOptn = value if value is not None else base_types.UninitialisedField(self, 'VoteOptn', VoteInstructionType2Choice, False)

	@VoteOptn.deleter
	def VoteOptn(self):
		del self._VoteOptn
		self._VoteOptn = base_types.UninitialisedField(self, 'VoteOptn', VoteInstructionType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrLabl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteOptn', type=VoteInstructionType2Choice, min=1, max=1, mutex_group=None, array=False),
	))