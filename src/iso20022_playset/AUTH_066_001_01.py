from . import base_types
import CCPBackTestingResultReportV01

class AUTH_066_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPBckTstgRsltRpt"]
		@property
		def CCPBckTstgRsltRpt(self):
			return self._CCPBckTstgRsltRpt

		@CCPBckTstgRsltRpt.setter
		def CCPBckTstgRsltRpt(self, value):
			self._CCPBckTstgRsltRpt = value if type(value) != auto else self.make_default("CCPBckTstgRsltRpt")

		@CCPBckTstgRsltRpt.deleter
		def CCPBckTstgRsltRpt(self):
			del self._CCPBckTstgRsltRpt
			self._CCPBckTstgRsltRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPBckTstgRsltRpt', type=CCPBackTestingResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))

