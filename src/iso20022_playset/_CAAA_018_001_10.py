from . import base_types
from ._AcceptorCurrencyConversionAdviceV10 import AcceptorCurrencyConversionAdviceV10

class CAAA_018_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCcyConvsAdvc"]
		@property
		def AccptrCcyConvsAdvc(self):
			return self._AccptrCcyConvsAdvc

		@AccptrCcyConvsAdvc.setter
		def AccptrCcyConvsAdvc(self, value):
			self._AccptrCcyConvsAdvc = value if type(value) != base_types.auto else self.make_default("AccptrCcyConvsAdvc")

		@AccptrCcyConvsAdvc.deleter
		def AccptrCcyConvsAdvc(self):
			del self._AccptrCcyConvsAdvc
			self._AccptrCcyConvsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsAdvc', type=AcceptorCurrencyConversionAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))

