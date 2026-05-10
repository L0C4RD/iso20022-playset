from . import base_types
import TransferCancellationStatusReportV07

class SESE_010_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfCxlStsRpt"]
		@property
		def TrfCxlStsRpt(self):
			return self._TrfCxlStsRpt

		@TrfCxlStsRpt.setter
		def TrfCxlStsRpt(self, value):
			self._TrfCxlStsRpt = value if type(value) != auto else self.make_default("TrfCxlStsRpt")

		@TrfCxlStsRpt.deleter
		def TrfCxlStsRpt(self):
			del self._TrfCxlStsRpt
			self._TrfCxlStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfCxlStsRpt', type=TransferCancellationStatusReportV07, min=1, max=1, mutex_group=None, array=False),
		))

