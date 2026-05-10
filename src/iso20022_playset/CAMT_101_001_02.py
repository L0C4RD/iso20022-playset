from . import base_types
import CreateLimitV02

class CAMT_101_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CretLmt"]
		@property
		def CretLmt(self):
			return self._CretLmt

		@CretLmt.setter
		def CretLmt(self, value):
			self._CretLmt = value if type(value) != auto else self.make_default("CretLmt")

		@CretLmt.deleter
		def CretLmt(self):
			del self._CretLmt
			self._CretLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CretLmt', type=CreateLimitV02, min=1, max=1, mutex_group=None, array=False),
		))

