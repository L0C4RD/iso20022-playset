# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._PhoneNumber import PhoneNumber

class CommunicationAddress3(base_types._BaseFieldType):

	__slots__ = ["_Email", "_FaxNb", "_Mob", "_Phne", "_TlxAdr", "_URLAdr"]
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
	def Mob(self):
		return self._Mob

	@Mob.setter
	def Mob(self, value):
		self._Mob = value if type(value) != base_types.auto else self.make_default("Mob")

	@Mob.deleter
	def Mob(self):
		del self._Mob
		self._Mob = None

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if type(value) != base_types.auto else self.make_default("Phne")

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = None

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
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mob', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TlxAdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))