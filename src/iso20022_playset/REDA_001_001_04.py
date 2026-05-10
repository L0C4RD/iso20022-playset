import base_types
import PriceReportV04

class REDA_001_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PricRpt"]
		@property
		def PricRpt(self):
			return self._PricRpt

		@PricRpt.setter
		def PricRpt(self, value):
			self._PricRpt = value if type(value) != auto else self.make_default("PricRpt")

		@PricRpt.deleter
		def PricRpt(self):
			del self._PricRpt
			self._PricRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PricRpt', type=PriceReportV04, min=1, max=1, mutex_group=None, array=False),
		))

