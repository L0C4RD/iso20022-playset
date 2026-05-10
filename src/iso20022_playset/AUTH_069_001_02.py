from . import base_types
import CCPClearedProductReportV02

class AUTH_069_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPClrdPdctRpt"]
		@property
		def CCPClrdPdctRpt(self):
			return self._CCPClrdPdctRpt

		@CCPClrdPdctRpt.setter
		def CCPClrdPdctRpt(self, value):
			self._CCPClrdPdctRpt = value if type(value) != auto else self.make_default("CCPClrdPdctRpt")

		@CCPClrdPdctRpt.deleter
		def CCPClrdPdctRpt(self):
			del self._CCPClrdPdctRpt
			self._CCPClrdPdctRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPClrdPdctRpt', type=CCPClearedProductReportV02, min=1, max=1, mutex_group=None, array=False),
		))

