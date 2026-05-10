from . import base_types
from .RequestForOrderStatusReportV04 import RequestForOrderStatusReportV04

class SETR_018_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqForOrdrStsRpt"]
		@property
		def ReqForOrdrStsRpt(self):
			return self._ReqForOrdrStsRpt

		@ReqForOrdrStsRpt.setter
		def ReqForOrdrStsRpt(self, value):
			self._ReqForOrdrStsRpt = value if type(value) != auto else self.make_default("ReqForOrdrStsRpt")

		@ReqForOrdrStsRpt.deleter
		def ReqForOrdrStsRpt(self):
			del self._ReqForOrdrStsRpt
			self._ReqForOrdrStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForOrdrStsRpt', type=RequestForOrderStatusReportV04, min=1, max=1, mutex_group=None, array=False),
		))

