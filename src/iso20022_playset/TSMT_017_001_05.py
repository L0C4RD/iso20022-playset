from . import base_types
from .ForwardDataSetSubmissionReportV05 import ForwardDataSetSubmissionReportV05

class TSMT_017_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FwdDataSetSubmissnRpt"]
		@property
		def FwdDataSetSubmissnRpt(self):
			return self._FwdDataSetSubmissnRpt

		@FwdDataSetSubmissnRpt.setter
		def FwdDataSetSubmissnRpt(self, value):
			self._FwdDataSetSubmissnRpt = value if type(value) != auto else self.make_default("FwdDataSetSubmissnRpt")

		@FwdDataSetSubmissnRpt.deleter
		def FwdDataSetSubmissnRpt(self):
			del self._FwdDataSetSubmissnRpt
			self._FwdDataSetSubmissnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FwdDataSetSubmissnRpt', type=ForwardDataSetSubmissionReportV05, min=1, max=1, mutex_group=None, array=False),
		))

