from . import base_types
from ._PhoneNumber import PhoneNumber
from ._Max2048Text import Max2048Text
from ._LongPostalAddress1Choice import LongPostalAddress1Choice

class CommunicationAddress10(base_types._BaseFieldType):

	__slots__ = ["_EmailAdr", "_FaxNb", "_PhneNb", "_PstlAdr"]
	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != base_types.auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

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
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmailAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=LongPostalAddress1Choice, min=1, max=1, mutex_group=None, array=False),
	))

