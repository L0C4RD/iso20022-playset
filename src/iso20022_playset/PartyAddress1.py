from . import base_types
from .Max256Text import Max256Text
from .AnyBICDec2014Identifier import AnyBICDec2014Identifier
from .PostalAddress26 import PostalAddress26
from .Max2048Text import Max2048Text

class PartyAddress1(base_types._BaseFieldType):

	__slots__ = ["_URLAdr", "_EmailAdr", "_PstlAdr", "_AnyBIC"]
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
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != base_types.auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
	))

