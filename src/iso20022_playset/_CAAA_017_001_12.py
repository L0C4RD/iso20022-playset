from . import base_types
from ._AcceptorCurrencyConversionResponseV12 import AcceptorCurrencyConversionResponseV12

class CAAA_017_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCcyConvsRspn"]
		@property
		def AccptrCcyConvsRspn(self):
			return self._AccptrCcyConvsRspn

		@AccptrCcyConvsRspn.setter
		def AccptrCcyConvsRspn(self, value):
			self._AccptrCcyConvsRspn = value if type(value) != base_types.auto else self.make_default("AccptrCcyConvsRspn")

		@AccptrCcyConvsRspn.deleter
		def AccptrCcyConvsRspn(self):
			del self._AccptrCcyConvsRspn
			self._AccptrCcyConvsRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsRspn', type=AcceptorCurrencyConversionResponseV12, min=1, max=1, mutex_group=None, array=False),
		))

