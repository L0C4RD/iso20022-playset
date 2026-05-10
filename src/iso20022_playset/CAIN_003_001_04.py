import base_types
import FinancialInitiationV04

class CAIN_003_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInitn"]
		@property
		def FinInitn(self):
			return self._FinInitn

		@FinInitn.setter
		def FinInitn(self, value):
			self._FinInitn = value if type(value) != auto else self.make_default("FinInitn")

		@FinInitn.deleter
		def FinInitn(self):
			del self._FinInitn
			self._FinInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInitn', type=FinancialInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))

