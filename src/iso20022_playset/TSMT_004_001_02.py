import base_types
import ActivityReportSetUpRequestV02

class TSMT_004_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ActvtyRptSetUpReq"]
		@property
		def ActvtyRptSetUpReq(self):
			return self._ActvtyRptSetUpReq

		@ActvtyRptSetUpReq.setter
		def ActvtyRptSetUpReq(self, value):
			self._ActvtyRptSetUpReq = value if type(value) != auto else self.make_default("ActvtyRptSetUpReq")

		@ActvtyRptSetUpReq.deleter
		def ActvtyRptSetUpReq(self):
			del self._ActvtyRptSetUpReq
			self._ActvtyRptSetUpReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyRptSetUpReq', type=ActivityReportSetUpRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

