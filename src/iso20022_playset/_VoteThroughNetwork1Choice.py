# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import VoteChannel1Code

class VoteThroughNetwork1Choice(base_types._BaseFieldType):

	__slots__ = ["_VoteChanl", "_VoteDrctlyToIssr"]
	@property
	def VoteChanl(self):
		return self._VoteChanl

	@VoteChanl.setter
	def VoteChanl(self, value):
		self._VoteChanl = value if value is not None else base_types.UninitialisedField(self, 'VoteChanl', VoteChannel1Code, False)

	@VoteChanl.deleter
	def VoteChanl(self):
		del self._VoteChanl
		self._VoteChanl = base_types.UninitialisedField(self, 'VoteChanl', VoteChannel1Code, False)

	@property
	def VoteDrctlyToIssr(self):
		return self._VoteDrctlyToIssr

	@VoteDrctlyToIssr.setter
	def VoteDrctlyToIssr(self, value):
		self._VoteDrctlyToIssr = value if value is not None else base_types.UninitialisedField(self, 'VoteDrctlyToIssr', AnyBICDec2014Identifier, True)

	@VoteDrctlyToIssr.deleter
	def VoteDrctlyToIssr(self):
		del self._VoteDrctlyToIssr
		self._VoteDrctlyToIssr = base_types.UninitialisedField(self, 'VoteDrctlyToIssr', AnyBICDec2014Identifier, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteChanl', type=VoteChannel1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VoteDrctlyToIssr', type=AnyBICDec2014Identifier, min=1, max=5, mutex_group=1, array=True),
	))