import base_types
import KEK9
import KEKIdentifier7
import KeyTransport10

class Recipient15Choice(base_types._BaseFieldType):

	__slots__ = ["_KeyIdr", "_KEK", "_KeyTrnsprt"]
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
	def KEK(self):
		return self._KEK

	@KEK.setter
	def KEK(self, value):
		self._KEK = value if type(value) != auto else self.make_default("KEK")

	@KEK.deleter
	def KEK(self):
		del self._KEK
		self._KEK = None

	@property
	def KeyTrnsprt(self):
		return self._KeyTrnsprt

	@KeyTrnsprt.setter
	def KeyTrnsprt(self, value):
		self._KeyTrnsprt = value if type(value) != auto else self.make_default("KeyTrnsprt")

	@KeyTrnsprt.deleter
	def KeyTrnsprt(self):
		del self._KeyTrnsprt
		self._KeyTrnsprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KEK', type=KEK9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyTrnsprt', type=KeyTransport10, min=0, max=1, mutex_group=1, array=False),
	))

