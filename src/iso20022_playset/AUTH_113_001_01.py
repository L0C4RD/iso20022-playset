from . import base_types
import OrderBookReportV01

class AUTH_113_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_OrdrBookRpt"]
		@property
		def OrdrBookRpt(self):
			return self._OrdrBookRpt

		@OrdrBookRpt.setter
		def OrdrBookRpt(self, value):
			self._OrdrBookRpt = value if type(value) != auto else self.make_default("OrdrBookRpt")

		@OrdrBookRpt.deleter
		def OrdrBookRpt(self):
			del self._OrdrBookRpt
			self._OrdrBookRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrBookRpt', type=OrderBookReportV01, min=1, max=1, mutex_group=None, array=False),
		))

