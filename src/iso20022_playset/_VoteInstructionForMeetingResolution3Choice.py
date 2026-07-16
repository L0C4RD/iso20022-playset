# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NameAndAddress9
from . import VoteInstructionType1Choice

class VoteInstructionForMeetingResolution3Choice(base_types._BaseFieldType):

	__slots__ = ["_Shrhldr", "_VoteIndctn"]
	@property
	def Shrhldr(self):
		return self._Shrhldr

	@Shrhldr.setter
	def Shrhldr(self, value):
		self._Shrhldr = value if value is not None else base_types.UninitialisedField(self, 'Shrhldr', NameAndAddress9, False)

	@Shrhldr.deleter
	def Shrhldr(self):
		del self._Shrhldr
		self._Shrhldr = base_types.UninitialisedField(self, 'Shrhldr', NameAndAddress9, False)

	@property
	def VoteIndctn(self):
		return self._VoteIndctn

	@VoteIndctn.setter
	def VoteIndctn(self, value):
		self._VoteIndctn = value if value is not None else base_types.UninitialisedField(self, 'VoteIndctn', VoteInstructionType1Choice, False)

	@VoteIndctn.deleter
	def VoteIndctn(self):
		del self._VoteIndctn
		self._VoteIndctn = base_types.UninitialisedField(self, 'VoteIndctn', VoteInstructionType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Shrhldr', type=NameAndAddress9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VoteIndctn', type=VoteInstructionType1Choice, min=0, max=1, mutex_group=1, array=False),
	))