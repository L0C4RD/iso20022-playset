from . import base_types
from .OrderInstructionStatusReportV04 import OrderInstructionStatusReportV04

class SETR_016_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_OrdrInstrStsRpt"]
		@property
		def OrdrInstrStsRpt(self):
			return self._OrdrInstrStsRpt

		@OrdrInstrStsRpt.setter
		def OrdrInstrStsRpt(self, value):
			self._OrdrInstrStsRpt = value if type(value) != base_types.auto else self.make_default("OrdrInstrStsRpt")

		@OrdrInstrStsRpt.deleter
		def OrdrInstrStsRpt(self):
			del self._OrdrInstrStsRpt
			self._OrdrInstrStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrInstrStsRpt', type=OrderInstructionStatusReportV04, min=1, max=1, mutex_group=None, array=False),
		))

