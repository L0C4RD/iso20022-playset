import base_types
import AcceptorCompletionAdviceResponseV13

class CAAA_004_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCmpltnAdvcRspn"]
		@property
		def AccptrCmpltnAdvcRspn(self):
			return self._AccptrCmpltnAdvcRspn

		@AccptrCmpltnAdvcRspn.setter
		def AccptrCmpltnAdvcRspn(self, value):
			self._AccptrCmpltnAdvcRspn = value if type(value) != auto else self.make_default("AccptrCmpltnAdvcRspn")

		@AccptrCmpltnAdvcRspn.deleter
		def AccptrCmpltnAdvcRspn(self):
			del self._AccptrCmpltnAdvcRspn
			self._AccptrCmpltnAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCmpltnAdvcRspn', type=AcceptorCompletionAdviceResponseV13, min=1, max=1, mutex_group=None, array=False),
		))

