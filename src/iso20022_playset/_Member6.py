# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress8
from . import ContactIdentificationAndAddress1
from . import MemberIdentification3Choice

class Member6(base_types._BaseFieldType):

	__slots__ = ["_ComAdr", "_CtctRef", "_MmbRtrAdr"]
	@property
	def ComAdr(self):
		return self._ComAdr

	@ComAdr.setter
	def ComAdr(self, value):
		self._ComAdr = value if value is not None else base_types.UninitialisedField(self, 'ComAdr', CommunicationAddress8, False)

	@ComAdr.deleter
	def ComAdr(self):
		del self._ComAdr
		self._ComAdr = base_types.UninitialisedField(self, 'ComAdr', CommunicationAddress8, False)

	@property
	def CtctRef(self):
		return self._CtctRef

	@CtctRef.setter
	def CtctRef(self, value):
		self._CtctRef = value if value is not None else base_types.UninitialisedField(self, 'CtctRef', ContactIdentificationAndAddress1, True)

	@CtctRef.deleter
	def CtctRef(self):
		del self._CtctRef
		self._CtctRef = base_types.UninitialisedField(self, 'CtctRef', ContactIdentificationAndAddress1, True)

	@property
	def MmbRtrAdr(self):
		return self._MmbRtrAdr

	@MmbRtrAdr.setter
	def MmbRtrAdr(self, value):
		self._MmbRtrAdr = value if value is not None else base_types.UninitialisedField(self, 'MmbRtrAdr', MemberIdentification3Choice, True)

	@MmbRtrAdr.deleter
	def MmbRtrAdr(self):
		del self._MmbRtrAdr
		self._MmbRtrAdr = base_types.UninitialisedField(self, 'MmbRtrAdr', MemberIdentification3Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComAdr', type=CommunicationAddress8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctRef', type=ContactIdentificationAndAddress1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MmbRtrAdr', type=MemberIdentification3Choice, min=0, max=None, mutex_group=None, array=True),
	))