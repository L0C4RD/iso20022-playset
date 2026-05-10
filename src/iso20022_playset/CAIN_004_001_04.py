from . import base_types
import FinancialResponseV04

class CAIN_004_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinRspn"]
		@property
		def FinRspn(self):
			return self._FinRspn

		@FinRspn.setter
		def FinRspn(self, value):
			self._FinRspn = value if type(value) != auto else self.make_default("FinRspn")

		@FinRspn.deleter
		def FinRspn(self):
			del self._FinRspn
			self._FinRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinRspn', type=FinancialResponseV04, min=1, max=1, mutex_group=None, array=False),
		))

