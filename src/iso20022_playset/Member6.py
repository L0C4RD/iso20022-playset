import base_types
import CommunicationAddress8
import MemberIdentification3Choice
import ContactIdentificationAndAddress1

class Member6(base_types._BaseFieldType):

	__slots__ = ["_CtctRef", "_MmbRtrAdr", "_ComAdr"]
	@property
	def CtctRef(self):
		return self._CtctRef

	@CtctRef.setter
	def CtctRef(self, value):
		self._CtctRef = value if type(value) != auto else self.make_default("CtctRef")

	@CtctRef.deleter
	def CtctRef(self):
		del self._CtctRef
		self._CtctRef = None

	@property
	def MmbRtrAdr(self):
		return self._MmbRtrAdr

	@MmbRtrAdr.setter
	def MmbRtrAdr(self, value):
		self._MmbRtrAdr = value if type(value) != auto else self.make_default("MmbRtrAdr")

	@MmbRtrAdr.deleter
	def MmbRtrAdr(self):
		del self._MmbRtrAdr
		self._MmbRtrAdr = None

	@property
	def ComAdr(self):
		return self._ComAdr

	@ComAdr.setter
	def ComAdr(self, value):
		self._ComAdr = value if type(value) != auto else self.make_default("ComAdr")

	@ComAdr.deleter
	def ComAdr(self):
		del self._ComAdr
		self._ComAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctRef', type=ContactIdentificationAndAddress1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MmbRtrAdr', type=MemberIdentification3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComAdr', type=CommunicationAddress8, min=0, max=1, mutex_group=None, array=False),
	))

