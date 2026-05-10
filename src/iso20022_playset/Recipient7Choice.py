import base_types
import KeyTransport6
import KEK6
import KEKIdentifier6

class Recipient7Choice(base_types._BaseFieldType):

	__slots__ = ["_KEK", "_KeyTrnsprt", "_KeyIdr"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='KEK', type=KEK6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyTrnsprt', type=KeyTransport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier6, min=0, max=1, mutex_group=1, array=False),
	))

