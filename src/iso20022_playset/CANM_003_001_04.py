from . import base_types
from .KeyExchangeInitiationV04 import KeyExchangeInitiationV04

class CANM_003_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_KeyXchgInitn"]
		@property
		def KeyXchgInitn(self):
			return self._KeyXchgInitn

		@KeyXchgInitn.setter
		def KeyXchgInitn(self, value):
			self._KeyXchgInitn = value if type(value) != auto else self.make_default("KeyXchgInitn")

		@KeyXchgInitn.deleter
		def KeyXchgInitn(self):
			del self._KeyXchgInitn
			self._KeyXchgInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgInitn', type=KeyExchangeInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))

