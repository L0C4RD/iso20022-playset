from . import base_types
import VoteInstructionType1Choice
import NameAndAddress9

class VoteInstructionForMeetingResolution3Choice(base_types._BaseFieldType):

	__slots__ = ["_Shrhldr", "_VoteIndctn"]
	@property
	def Shrhldr(self):
		return self._Shrhldr

	@Shrhldr.setter
	def Shrhldr(self, value):
		self._Shrhldr = value if type(value) != auto else self.make_default("Shrhldr")

	@Shrhldr.deleter
	def Shrhldr(self):
		del self._Shrhldr
		self._Shrhldr = None

	@property
	def VoteIndctn(self):
		return self._VoteIndctn

	@VoteIndctn.setter
	def VoteIndctn(self, value):
		self._VoteIndctn = value if type(value) != auto else self.make_default("VoteIndctn")

	@VoteIndctn.deleter
	def VoteIndctn(self):
		del self._VoteIndctn
		self._VoteIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Shrhldr', type=NameAndAddress9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VoteIndctn', type=VoteInstructionType1Choice, min=0, max=1, mutex_group=1, array=False),
	))

