from . import base_types
from ._FraudReportingResponseV03 import FraudReportingResponseV03

class CAFR_002_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FrdRptgRspn"]
		@property
		def FrdRptgRspn(self):
			return self._FrdRptgRspn

		@FrdRptgRspn.setter
		def FrdRptgRspn(self, value):
			self._FrdRptgRspn = value if type(value) != base_types.auto else self.make_default("FrdRptgRspn")

		@FrdRptgRspn.deleter
		def FrdRptgRspn(self):
			del self._FrdRptgRspn
			self._FrdRptgRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdRptgRspn', type=FraudReportingResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

