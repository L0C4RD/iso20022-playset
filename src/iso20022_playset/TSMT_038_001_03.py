import base_types
import StatusReportRequestV03

class TSMT_038_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsRptReq"]
		@property
		def StsRptReq(self):
			return self._StsRptReq

		@StsRptReq.setter
		def StsRptReq(self, value):
			self._StsRptReq = value if type(value) != auto else self.make_default("StsRptReq")

		@StsRptReq.deleter
		def StsRptReq(self):
			del self._StsRptReq
			self._StsRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsRptReq', type=StatusReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

