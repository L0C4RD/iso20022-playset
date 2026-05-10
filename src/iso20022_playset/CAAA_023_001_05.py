import base_types
import AcceptorNonFinancialResponseV05

class CAAA_023_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrNonFinRspn"]
		@property
		def AccptrNonFinRspn(self):
			return self._AccptrNonFinRspn

		@AccptrNonFinRspn.setter
		def AccptrNonFinRspn(self, value):
			self._AccptrNonFinRspn = value if type(value) != auto else self.make_default("AccptrNonFinRspn")

		@AccptrNonFinRspn.deleter
		def AccptrNonFinRspn(self):
			del self._AccptrNonFinRspn
			self._AccptrNonFinRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrNonFinRspn', type=AcceptorNonFinancialResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

