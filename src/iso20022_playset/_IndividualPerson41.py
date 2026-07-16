# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceCard3
from . import PartyIdentification129Choice
from . import PartyIdentification232Choice
from . import VotingParticipationMethod2Code

class IndividualPerson41(base_types._BaseFieldType):

	__slots__ = ["_AttndncCardDtls", "_EmplngPty", "_Id", "_PrtcptnMtd"]
	@property
	def AttndncCardDtls(self):
		return self._AttndncCardDtls

	@AttndncCardDtls.setter
	def AttndncCardDtls(self, value):
		self._AttndncCardDtls = value if value is not None else base_types.UninitialisedField(self, 'AttndncCardDtls', AttendanceCard3, False)

	@AttndncCardDtls.deleter
	def AttndncCardDtls(self):
		del self._AttndncCardDtls
		self._AttndncCardDtls = base_types.UninitialisedField(self, 'AttndncCardDtls', AttendanceCard3, False)

	@property
	def EmplngPty(self):
		return self._EmplngPty

	@EmplngPty.setter
	def EmplngPty(self, value):
		self._EmplngPty = value if value is not None else base_types.UninitialisedField(self, 'EmplngPty', PartyIdentification129Choice, False)

	@EmplngPty.deleter
	def EmplngPty(self):
		del self._EmplngPty
		self._EmplngPty = base_types.UninitialisedField(self, 'EmplngPty', PartyIdentification129Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification232Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification232Choice, False)

	@property
	def PrtcptnMtd(self):
		return self._PrtcptnMtd

	@PrtcptnMtd.setter
	def PrtcptnMtd(self, value):
		self._PrtcptnMtd = value if value is not None else base_types.UninitialisedField(self, 'PrtcptnMtd', VotingParticipationMethod2Code, False)

	@PrtcptnMtd.deleter
	def PrtcptnMtd(self):
		del self._PrtcptnMtd
		self._PrtcptnMtd = base_types.UninitialisedField(self, 'PrtcptnMtd', VotingParticipationMethod2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCardDtls', type=AttendanceCard3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcptnMtd', type=VotingParticipationMethod2Code, min=0, max=1, mutex_group=None, array=False),
	))