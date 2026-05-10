import base_types
import CaseStatusReportRequestV05

class CAMT_038_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CaseStsRptReq"]
		@property
		def CaseStsRptReq(self):
			return self._CaseStsRptReq

		@CaseStsRptReq.setter
		def CaseStsRptReq(self, value):
			self._CaseStsRptReq = value if type(value) != auto else self.make_default("CaseStsRptReq")

		@CaseStsRptReq.deleter
		def CaseStsRptReq(self):
			del self._CaseStsRptReq
			self._CaseStsRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CaseStsRptReq', type=CaseStatusReportRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

