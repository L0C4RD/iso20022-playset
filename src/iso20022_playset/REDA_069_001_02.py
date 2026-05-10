from . import base_types
import RequestToPayCreditorEnrolmentStatusReportV02

class REDA_069_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayCdtrEnrlmntStsRpt"]
		@property
		def ReqToPayCdtrEnrlmntStsRpt(self):
			return self._ReqToPayCdtrEnrlmntStsRpt

		@ReqToPayCdtrEnrlmntStsRpt.setter
		def ReqToPayCdtrEnrlmntStsRpt(self, value):
			self._ReqToPayCdtrEnrlmntStsRpt = value if type(value) != auto else self.make_default("ReqToPayCdtrEnrlmntStsRpt")

		@ReqToPayCdtrEnrlmntStsRpt.deleter
		def ReqToPayCdtrEnrlmntStsRpt(self):
			del self._ReqToPayCdtrEnrlmntStsRpt
			self._ReqToPayCdtrEnrlmntStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntStsRpt', type=RequestToPayCreditorEnrolmentStatusReportV02, min=1, max=1, mutex_group=None, array=False),
		))

