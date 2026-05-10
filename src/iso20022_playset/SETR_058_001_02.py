import base_types
import RequestForOrderConfirmationStatusReportV02

class SETR_058_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqForOrdrConfStsRpt"]
		@property
		def ReqForOrdrConfStsRpt(self):
			return self._ReqForOrdrConfStsRpt

		@ReqForOrdrConfStsRpt.setter
		def ReqForOrdrConfStsRpt(self, value):
			self._ReqForOrdrConfStsRpt = value if type(value) != auto else self.make_default("ReqForOrdrConfStsRpt")

		@ReqForOrdrConfStsRpt.deleter
		def ReqForOrdrConfStsRpt(self):
			del self._ReqForOrdrConfStsRpt
			self._ReqForOrdrConfStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForOrdrConfStsRpt', type=RequestForOrderConfirmationStatusReportV02, min=1, max=1, mutex_group=None, array=False),
		))

