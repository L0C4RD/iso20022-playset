from . import base_types
from .BaselineMatchReportV03 import BaselineMatchReportV03

class TSMT_010_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BaselnMtchRpt"]
		@property
		def BaselnMtchRpt(self):
			return self._BaselnMtchRpt

		@BaselnMtchRpt.setter
		def BaselnMtchRpt(self, value):
			self._BaselnMtchRpt = value if type(value) != base_types.auto else self.make_default("BaselnMtchRpt")

		@BaselnMtchRpt.deleter
		def BaselnMtchRpt(self):
			del self._BaselnMtchRpt
			self._BaselnMtchRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnMtchRpt', type=BaselineMatchReportV03, min=1, max=1, mutex_group=None, array=False),
		))

