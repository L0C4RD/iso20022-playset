from . import base_types
import AcceptorReconciliationRequestV13

class CAAA_009_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrRcncltnReq"]
		@property
		def AccptrRcncltnReq(self):
			return self._AccptrRcncltnReq

		@AccptrRcncltnReq.setter
		def AccptrRcncltnReq(self, value):
			self._AccptrRcncltnReq = value if type(value) != auto else self.make_default("AccptrRcncltnReq")

		@AccptrRcncltnReq.deleter
		def AccptrRcncltnReq(self):
			del self._AccptrRcncltnReq
			self._AccptrRcncltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRcncltnReq', type=AcceptorReconciliationRequestV13, min=1, max=1, mutex_group=None, array=False),
		))

