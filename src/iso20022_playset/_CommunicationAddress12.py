from . import base_types
from ._Max2048Text import Max2048Text

class CommunicationAddress12(base_types._BaseFieldType):

	__slots__ = ["_URLAdr"]
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
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))

