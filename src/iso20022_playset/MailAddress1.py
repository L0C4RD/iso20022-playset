from . import base_types
import Max256Text
import PostalAddress1

class MailAddress1(base_types._BaseFieldType):

	__slots__ = ["_EmailAdr", "_Crspdc"]
	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

	@property
	def Crspdc(self):
		return self._Crspdc

	@Crspdc.setter
	def Crspdc(self, value):
		self._Crspdc = value if type(value) != auto else self.make_default("Crspdc")

	@Crspdc.deleter
	def Crspdc(self):
		del self._Crspdc
		self._Crspdc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Crspdc', type=PostalAddress1, min=0, max=5, mutex_group=None, array=True),
	))

