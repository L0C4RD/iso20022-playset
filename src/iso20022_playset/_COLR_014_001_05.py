from . import base_types
from ._InterestPaymentResponseV05 import InterestPaymentResponseV05

class COLR_014_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntrstPmtRspn"]
		@property
		def IntrstPmtRspn(self):
			return self._IntrstPmtRspn

		@IntrstPmtRspn.setter
		def IntrstPmtRspn(self, value):
			self._IntrstPmtRspn = value if type(value) != base_types.auto else self.make_default("IntrstPmtRspn")

		@IntrstPmtRspn.deleter
		def IntrstPmtRspn(self):
			del self._IntrstPmtRspn
			self._IntrstPmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtRspn', type=InterestPaymentResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

