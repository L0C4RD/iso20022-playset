# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LongPostalAddress1Choice
from . import Max2048Text
from . import PhoneNumber

class CommunicationAddress10(base_types._BaseFieldType):

	__slots__ = ["_EmailAdr", "_FaxNb", "_PhneNb", "_PstlAdr"]
	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max2048Text, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max2048Text, False)

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
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', LongPostalAddress1Choice, False)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', LongPostalAddress1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmailAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=LongPostalAddress1Choice, min=1, max=1, mutex_group=None, array=False),
	))