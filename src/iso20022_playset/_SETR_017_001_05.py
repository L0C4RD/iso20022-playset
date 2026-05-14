from . import base_types
from ._OrderCancellationStatusReportV05 import OrderCancellationStatusReportV05

class SETR_017_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_OrdrCxlStsRpt"]
		@property
		def OrdrCxlStsRpt(self):
			return self._OrdrCxlStsRpt

		@OrdrCxlStsRpt.setter
		def OrdrCxlStsRpt(self, value):
			self._OrdrCxlStsRpt = value if type(value) != base_types.auto else self.make_default("OrdrCxlStsRpt")

		@OrdrCxlStsRpt.deleter
		def OrdrCxlStsRpt(self):
			del self._OrdrCxlStsRpt
			self._OrdrCxlStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrCxlStsRpt', type=OrderCancellationStatusReportV05, min=1, max=1, mutex_group=None, array=False),
		))

