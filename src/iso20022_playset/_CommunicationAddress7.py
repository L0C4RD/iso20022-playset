from . import base_types
from ._Max2048Text import Max2048Text
from ._Max35Text import Max35Text
from ._PhoneNumber import PhoneNumber

class CommunicationAddress7(base_types._BaseFieldType):

	__slots__ = ["_Email", "_FaxNb", "_MobNb", "_PhneNb", "_TlxAdr", "_URLAdr"]
	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if type(value) != base_types.auto else self.make_default("Email")

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = None

	@property
	def FaxNb(self):
		return self._FaxNb

	@FaxNb.setter
	def FaxNb(self, value):
		self._FaxNb = value if type(value) != base_types.auto else self.make_default("FaxNb")

	@FaxNb.deleter
	def FaxNb(self):
		del self._FaxNb
		self._FaxNb = None

	@property
	def MobNb(self):
		return self._MobNb

	@MobNb.setter
	def MobNb(self, value):
		self._MobNb = value if type(value) != base_types.auto else self.make_default("MobNb")

	@MobNb.deleter
	def MobNb(self):
		del self._MobNb
		self._MobNb = None

	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if type(value) != base_types.auto else self.make_default("PhneNb")

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = None

	@property
	def TlxAdr(self):
		return self._TlxAdr

	@TlxAdr.setter
	def TlxAdr(self, value):
		self._TlxAdr = value if type(value) != base_types.auto else self.make_default("TlxAdr")

	@TlxAdr.deleter
	def TlxAdr(self):
		del self._TlxAdr
		self._TlxAdr = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != base_types.auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Email', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TlxAdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))

