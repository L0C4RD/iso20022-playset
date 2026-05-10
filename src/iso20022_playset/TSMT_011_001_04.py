from . import base_types
import BaselineReportV04

class TSMT_011_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BaselnRpt"]
		@property
		def BaselnRpt(self):
			return self._BaselnRpt

		@BaselnRpt.setter
		def BaselnRpt(self, value):
			self._BaselnRpt = value if type(value) != auto else self.make_default("BaselnRpt")

		@BaselnRpt.deleter
		def BaselnRpt(self):
			del self._BaselnRpt
			self._BaselnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnRpt', type=BaselineReportV04, min=1, max=1, mutex_group=None, array=False),
		))

