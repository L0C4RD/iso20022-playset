# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressType1Choice
from . import Max256Text
from . import Max35Text
from . import PhoneNumber

class CommunicationAddress6(base_types._BaseFieldType):

	__slots__ = ["_AdrTp", "_Email", "_FaxNb", "_Mob", "_Phne", "_TlxAdr", "_URLAdr"]
	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if value is not None else base_types.UninitialisedField(self, 'AdrTp', AddressType1Choice, False)

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = base_types.UninitialisedField(self, 'AdrTp', AddressType1Choice, False)

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if value is not None else base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = base_types.UninitialisedField(self, 'Email', Max256Text, False)

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
	def Mob(self):
		return self._Mob

	@Mob.setter
	def Mob(self, value):
		self._Mob = value if value is not None else base_types.UninitialisedField(self, 'Mob', PhoneNumber, False)

	@Mob.deleter
	def Mob(self):
		del self._Mob
		self._Mob = base_types.UninitialisedField(self, 'Mob', PhoneNumber, False)

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if value is not None else base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

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
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrTp', type=AddressType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mob', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TlxAdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))