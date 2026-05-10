import base_types
import IntentToPayReportV01

class TSMT_046_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InttToPayRpt"]
		@property
		def InttToPayRpt(self):
			return self._InttToPayRpt

		@InttToPayRpt.setter
		def InttToPayRpt(self, value):
			self._InttToPayRpt = value if type(value) != auto else self.make_default("InttToPayRpt")

		@InttToPayRpt.deleter
		def InttToPayRpt(self):
			del self._InttToPayRpt
			self._InttToPayRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InttToPayRpt', type=IntentToPayReportV01, min=1, max=1, mutex_group=None, array=False),
		))

