import base_types
import KEKIdentifier2
import IssuerAndSerialNumber1

class Recipient5Choice(base_types._BaseFieldType):

	__slots__ = ["_KeyIdr", "_IssrAndSrlNb"]
	@property
	def KeyIdr(self):
		return self._KeyIdr

	@KeyIdr.setter
	def KeyIdr(self, value):
		self._KeyIdr = value if type(value) != auto else self.make_default("KeyIdr")

	@KeyIdr.deleter
	def KeyIdr(self):
		del self._KeyIdr
		self._KeyIdr = None

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
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IssrAndSrlNb', type=IssuerAndSerialNumber1, min=0, max=1, mutex_group=1, array=False),
	))

