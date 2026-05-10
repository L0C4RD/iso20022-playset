import base_types
import SaleToPOIReportRequestV07

class CASP_009_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIRptReq"]
		@property
		def SaleToPOIRptReq(self):
			return self._SaleToPOIRptReq

		@SaleToPOIRptReq.setter
		def SaleToPOIRptReq(self, value):
			self._SaleToPOIRptReq = value if type(value) != auto else self.make_default("SaleToPOIRptReq")

		@SaleToPOIRptReq.deleter
		def SaleToPOIRptReq(self):
			del self._SaleToPOIRptReq
			self._SaleToPOIRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptReq', type=SaleToPOIReportRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

