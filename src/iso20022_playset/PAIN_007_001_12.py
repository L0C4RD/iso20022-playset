import base_types
import CustomerPaymentReversalV12

class PAIN_007_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CstmrPmtRvsl"]
		@property
		def CstmrPmtRvsl(self):
			return self._CstmrPmtRvsl

		@CstmrPmtRvsl.setter
		def CstmrPmtRvsl(self, value):
			self._CstmrPmtRvsl = value if type(value) != auto else self.make_default("CstmrPmtRvsl")

		@CstmrPmtRvsl.deleter
		def CstmrPmtRvsl(self):
			del self._CstmrPmtRvsl
			self._CstmrPmtRvsl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtRvsl', type=CustomerPaymentReversalV12, min=1, max=1, mutex_group=None, array=False),
		))

