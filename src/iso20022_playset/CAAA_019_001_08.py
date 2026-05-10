from . import base_types
import AcceptorCurrencyConversionAdviceResponseV08

class CAAA_019_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCcyConvsAdvcRspn"]
		@property
		def AccptrCcyConvsAdvcRspn(self):
			return self._AccptrCcyConvsAdvcRspn

		@AccptrCcyConvsAdvcRspn.setter
		def AccptrCcyConvsAdvcRspn(self, value):
			self._AccptrCcyConvsAdvcRspn = value if type(value) != auto else self.make_default("AccptrCcyConvsAdvcRspn")

		@AccptrCcyConvsAdvcRspn.deleter
		def AccptrCcyConvsAdvcRspn(self):
			del self._AccptrCcyConvsAdvcRspn
			self._AccptrCcyConvsAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsAdvcRspn', type=AcceptorCurrencyConversionAdviceResponseV08, min=1, max=1, mutex_group=None, array=False),
		))

