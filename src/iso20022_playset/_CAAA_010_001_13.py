from . import base_types
from ._AcceptorReconciliationResponseV13 import AcceptorReconciliationResponseV13

class CAAA_010_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrRcncltnRspn"]
		@property
		def AccptrRcncltnRspn(self):
			return self._AccptrRcncltnRspn

		@AccptrRcncltnRspn.setter
		def AccptrRcncltnRspn(self, value):
			self._AccptrRcncltnRspn = value if type(value) != base_types.auto else self.make_default("AccptrRcncltnRspn")

		@AccptrRcncltnRspn.deleter
		def AccptrRcncltnRspn(self):
			del self._AccptrRcncltnRspn
			self._AccptrRcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRcncltnRspn', type=AcceptorReconciliationResponseV13, min=1, max=1, mutex_group=None, array=False),
		))

