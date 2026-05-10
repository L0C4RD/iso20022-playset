from . import base_types
import ActivityReportRequestV03

class TSMT_003_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ActvtyReqRpt"]
		@property
		def ActvtyReqRpt(self):
			return self._ActvtyReqRpt

		@ActvtyReqRpt.setter
		def ActvtyReqRpt(self, value):
			self._ActvtyReqRpt = value if type(value) != auto else self.make_default("ActvtyReqRpt")

		@ActvtyReqRpt.deleter
		def ActvtyReqRpt(self):
			del self._ActvtyReqRpt
			self._ActvtyReqRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ActvtyReqRpt', type=ActivityReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

