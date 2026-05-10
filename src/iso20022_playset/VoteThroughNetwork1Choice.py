from . import base_types
import AnyBICDec2014Identifier
import VoteChannel1Code

class VoteThroughNetwork1Choice(base_types._BaseFieldType):

	__slots__ = ["_VoteChanl", "_VoteDrctlyToIssr"]
	@property
	def VoteChanl(self):
		return self._VoteChanl

	@VoteChanl.setter
	def VoteChanl(self, value):
		self._VoteChanl = value if type(value) != auto else self.make_default("VoteChanl")

	@VoteChanl.deleter
	def VoteChanl(self):
		del self._VoteChanl
		self._VoteChanl = None

	@property
	def VoteDrctlyToIssr(self):
		return self._VoteDrctlyToIssr

	@VoteDrctlyToIssr.setter
	def VoteDrctlyToIssr(self, value):
		self._VoteDrctlyToIssr = value if type(value) != auto else self.make_default("VoteDrctlyToIssr")

	@VoteDrctlyToIssr.deleter
	def VoteDrctlyToIssr(self):
		del self._VoteDrctlyToIssr
		self._VoteDrctlyToIssr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteChanl', type=VoteChannel1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VoteDrctlyToIssr', type=AnyBICDec2014Identifier, min=1, max=5, mutex_group=1, array=True),
	))

