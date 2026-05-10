from . import base_types
import KeyExchangeResponseV04

class CANM_004_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_KeyXchgRspn"]
		@property
		def KeyXchgRspn(self):
			return self._KeyXchgRspn

		@KeyXchgRspn.setter
		def KeyXchgRspn(self, value):
			self._KeyXchgRspn = value if type(value) != auto else self.make_default("KeyXchgRspn")

		@KeyXchgRspn.deleter
		def KeyXchgRspn(self):
			del self._KeyXchgRspn
			self._KeyXchgRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgRspn', type=KeyExchangeResponseV04, min=1, max=1, mutex_group=None, array=False),
		))

