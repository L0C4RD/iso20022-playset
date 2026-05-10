import base_types
import VoteInstructionType2Choice
import Max35Text

class Vote15(base_types._BaseFieldType):

	__slots__ = ["_VoteOptn", "_IssrLabl"]
	@property
	def VoteOptn(self):
		return self._VoteOptn

	@VoteOptn.setter
	def VoteOptn(self, value):
		self._VoteOptn = value if type(value) != auto else self.make_default("VoteOptn")

	@VoteOptn.deleter
	def VoteOptn(self):
		del self._VoteOptn
		self._VoteOptn = None

	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if type(value) != auto else self.make_default("IssrLabl")

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteOptn', type=VoteInstructionType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrLabl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

