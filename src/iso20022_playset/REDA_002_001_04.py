from . import base_types
from .PriceReportCancellationV04 import PriceReportCancellationV04

class REDA_002_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PricRptCxl"]
		@property
		def PricRptCxl(self):
			return self._PricRptCxl

		@PricRptCxl.setter
		def PricRptCxl(self, value):
			self._PricRptCxl = value if type(value) != base_types.auto else self.make_default("PricRptCxl")

		@PricRptCxl.deleter
		def PricRptCxl(self):
			del self._PricRptCxl
			self._PricRptCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PricRptCxl', type=PriceReportCancellationV04, min=1, max=1, mutex_group=None, array=False),
		))

