from . import base_types
import AcceptorCurrencyConversionRequestV12

class CAAA_016_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCcyConvsReq"]
		@property
		def AccptrCcyConvsReq(self):
			return self._AccptrCcyConvsReq

		@AccptrCcyConvsReq.setter
		def AccptrCcyConvsReq(self, value):
			self._AccptrCcyConvsReq = value if type(value) != auto else self.make_default("AccptrCcyConvsReq")

		@AccptrCcyConvsReq.deleter
		def AccptrCcyConvsReq(self):
			del self._AccptrCcyConvsReq
			self._AccptrCcyConvsReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsReq', type=AcceptorCurrencyConversionRequestV12, min=1, max=1, mutex_group=None, array=False),
		))

