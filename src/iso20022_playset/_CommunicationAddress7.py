# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2048Text
from . import Max35Text
from . import PhoneNumber

class CommunicationAddress7(base_types._BaseFieldType):

	__slots__ = ["_Email", "_FaxNb", "_MobNb", "_PhneNb", "_TlxAdr", "_URLAdr"]
	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if value is not None else base_types.UninitialisedField(self, 'Email', Max2048Text, False)

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = base_types.UninitialisedField(self, 'Email', Max2048Text, False)

	@property
	def FaxNb(self):
		return self._FaxNb

	@FaxNb.setter
	def FaxNb(self, value):
		self._FaxNb = value if value is not None else base_types.UninitialisedField(self, 'FaxNb', PhoneNumber, False)

	@FaxNb.deleter
	def FaxNb(self):
		del self._FaxNb
		self._FaxNb = base_types.UninitialisedField(self, 'FaxNb', PhoneNumber, False)

	@property
	def MobNb(self):
		return self._MobNb

	@MobNb.setter
	def MobNb(self, value):
		self._MobNb = value if value is not None else base_types.UninitialisedField(self, 'MobNb', PhoneNumber, False)

	@MobNb.deleter
	def MobNb(self):
		del self._MobNb
		self._MobNb = base_types.UninitialisedField(self, 'MobNb', PhoneNumber, False)

	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if value is not None else base_types.UninitialisedField(self, 'PhneNb', PhoneNumber, False)

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = base_types.UninitialisedField(self, 'PhneNb', PhoneNumber, False)

	@property
	def TlxAdr(self):
		return self._TlxAdr

	@TlxAdr.setter
	def TlxAdr(self, value):
		self._TlxAdr = value if value is not None else base_types.UninitialisedField(self, 'TlxAdr', Max35Text, False)

	@TlxAdr.deleter
	def TlxAdr(self):
		del self._TlxAdr
		self._TlxAdr = base_types.UninitialisedField(self, 'TlxAdr', Max35Text, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Email', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TlxAdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))