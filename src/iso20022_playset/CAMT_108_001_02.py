import base_types
import ChequeCancellationOrStopRequestV02

class CAMT_108_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ChqCxlOrStopReq"]
		@property
		def ChqCxlOrStopReq(self):
			return self._ChqCxlOrStopReq

		@ChqCxlOrStopReq.setter
		def ChqCxlOrStopReq(self, value):
			self._ChqCxlOrStopReq = value if type(value) != auto else self.make_default("ChqCxlOrStopReq")

		@ChqCxlOrStopReq.deleter
		def ChqCxlOrStopReq(self):
			del self._ChqCxlOrStopReq
			self._ChqCxlOrStopReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChqCxlOrStopReq', type=ChequeCancellationOrStopRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

