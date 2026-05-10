from . import base_types
from ._Max256Text import Max256Text
from ._PostalAddress1 import PostalAddress1

class MailAddress1(base_types._BaseFieldType):

	__slots__ = ["_Crspdc", "_EmailAdr"]
	@property
	def Crspdc(self):
		return self._Crspdc

	@Crspdc.setter
	def Crspdc(self, value):
		self._Crspdc = value if type(value) != base_types.auto else self.make_default("Crspdc")

	@Crspdc.deleter
	def Crspdc(self):
		del self._Crspdc
		self._Crspdc = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Crspdc', type=PostalAddress1, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=5, mutex_group=None, array=True),
	))

