from . import base_types
from ._BillingReportV01 import BillingReportV01

class CAMT_077_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BllgRpt"]
		@property
		def BllgRpt(self):
			return self._BllgRpt

		@BllgRpt.setter
		def BllgRpt(self, value):
			self._BllgRpt = value if type(value) != base_types.auto else self.make_default("BllgRpt")

		@BllgRpt.deleter
		def BllgRpt(self):
			del self._BllgRpt
			self._BllgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BllgRpt', type=BillingReportV01, min=1, max=1, mutex_group=None, array=False),
		))

