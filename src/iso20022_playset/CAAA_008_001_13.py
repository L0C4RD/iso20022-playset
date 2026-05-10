from . import base_types
import AcceptorCancellationAdviceResponseV13

class CAAA_008_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCxlAdvcRspn"]
		@property
		def AccptrCxlAdvcRspn(self):
			return self._AccptrCxlAdvcRspn

		@AccptrCxlAdvcRspn.setter
		def AccptrCxlAdvcRspn(self, value):
			self._AccptrCxlAdvcRspn = value if type(value) != auto else self.make_default("AccptrCxlAdvcRspn")

		@AccptrCxlAdvcRspn.deleter
		def AccptrCxlAdvcRspn(self):
			del self._AccptrCxlAdvcRspn
			self._AccptrCxlAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlAdvcRspn', type=AcceptorCancellationAdviceResponseV13, min=1, max=1, mutex_group=None, array=False),
		))

