from . import base_types
from .PartyIdentification232Choice import PartyIdentification232Choice
from .AttendanceCard3 import AttendanceCard3
from .VotingParticipationMethod2Code import VotingParticipationMethod2Code
from .PartyIdentification129Choice import PartyIdentification129Choice

class IndividualPerson41(base_types._BaseFieldType):

	__slots__ = ["_AttndncCardDtls", "_EmplngPty", "_PrtcptnMtd", "_Id"]
	@property
	def AttndncCardDtls(self):
		return self._AttndncCardDtls

	@AttndncCardDtls.setter
	def AttndncCardDtls(self, value):
		self._AttndncCardDtls = value if type(value) != auto else self.make_default("AttndncCardDtls")

	@AttndncCardDtls.deleter
	def AttndncCardDtls(self):
		del self._AttndncCardDtls
		self._AttndncCardDtls = None

	@property
	def EmplngPty(self):
		return self._EmplngPty

	@EmplngPty.setter
	def EmplngPty(self, value):
		self._EmplngPty = value if type(value) != auto else self.make_default("EmplngPty")

	@EmplngPty.deleter
	def EmplngPty(self):
		del self._EmplngPty
		self._EmplngPty = None

	@property
	def PrtcptnMtd(self):
		return self._PrtcptnMtd

	@PrtcptnMtd.setter
	def PrtcptnMtd(self, value):
		self._PrtcptnMtd = value if type(value) != auto else self.make_default("PrtcptnMtd")

	@PrtcptnMtd.deleter
	def PrtcptnMtd(self):
		del self._PrtcptnMtd
		self._PrtcptnMtd = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCardDtls', type=AttendanceCard3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcptnMtd', type=VotingParticipationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
	))

