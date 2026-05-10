from . import base_types
from ._CommunicationAddress12 import CommunicationAddress12
from ._MailAddress1 import MailAddress1
from ._Max35Text import Max35Text
from ._VoteThroughNetwork1Choice import VoteThroughNetwork1Choice

class VoteMethods5(base_types._BaseFieldType):

	__slots__ = ["_ElctrncVote", "_VoteByMail", "_VoteByTel", "_VoteThrghNtwk"]
	@property
	def ElctrncVote(self):
		return self._ElctrncVote

	@ElctrncVote.setter
	def ElctrncVote(self, value):
		self._ElctrncVote = value if type(value) != base_types.auto else self.make_default("ElctrncVote")

	@ElctrncVote.deleter
	def ElctrncVote(self):
		del self._ElctrncVote
		self._ElctrncVote = None

	@property
	def VoteByMail(self):
		return self._VoteByMail

	@VoteByMail.setter
	def VoteByMail(self, value):
		self._VoteByMail = value if type(value) != base_types.auto else self.make_default("VoteByMail")

	@VoteByMail.deleter
	def VoteByMail(self):
		del self._VoteByMail
		self._VoteByMail = None

	@property
	def VoteByTel(self):
		return self._VoteByTel

	@VoteByTel.setter
	def VoteByTel(self, value):
		self._VoteByTel = value if type(value) != base_types.auto else self.make_default("VoteByTel")

	@VoteByTel.deleter
	def VoteByTel(self):
		del self._VoteByTel
		self._VoteByTel = None

	@property
	def VoteThrghNtwk(self):
		return self._VoteThrghNtwk

	@VoteThrghNtwk.setter
	def VoteThrghNtwk(self, value):
		self._VoteThrghNtwk = value if type(value) != base_types.auto else self.make_default("VoteThrghNtwk")

	@VoteThrghNtwk.deleter
	def VoteThrghNtwk(self):
		del self._VoteThrghNtwk
		self._VoteThrghNtwk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncVote', type=CommunicationAddress12, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteByMail', type=MailAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteByTel', type=Max35Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteThrghNtwk', type=VoteThroughNetwork1Choice, min=0, max=1, mutex_group=None, array=False),
	))

