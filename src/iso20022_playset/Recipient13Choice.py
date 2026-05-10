import base_types
import Max140Binary
import IssuerAndSerialNumber2

class Recipient13Choice(base_types._BaseFieldType):

	__slots__ = ["_SbjtKeyIdr", "_IssrAndSrlNb"]
	@property
	def SbjtKeyIdr(self):
		return self._SbjtKeyIdr

	@SbjtKeyIdr.setter
	def SbjtKeyIdr(self, value):
		self._SbjtKeyIdr = value if type(value) != auto else self.make_default("SbjtKeyIdr")

	@SbjtKeyIdr.deleter
	def SbjtKeyIdr(self):
		del self._SbjtKeyIdr
		self._SbjtKeyIdr = None

	@property
	def IssrAndSrlNb(self):
		return self._IssrAndSrlNb

	@IssrAndSrlNb.setter
	def IssrAndSrlNb(self, value):
		self._IssrAndSrlNb = value if type(value) != auto else self.make_default("IssrAndSrlNb")

	@IssrAndSrlNb.deleter
	def IssrAndSrlNb(self):
		del self._IssrAndSrlNb
		self._IssrAndSrlNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SbjtKeyIdr', type=Max140Binary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IssrAndSrlNb', type=IssuerAndSerialNumber2, min=0, max=1, mutex_group=1, array=False),
	))

