from . import base_types
import SaleToPOIReportResponseV07

class CASP_010_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIRptRspn"]
		@property
		def SaleToPOIRptRspn(self):
			return self._SaleToPOIRptRspn

		@SaleToPOIRptRspn.setter
		def SaleToPOIRptRspn(self, value):
			self._SaleToPOIRptRspn = value if type(value) != auto else self.make_default("SaleToPOIRptRspn")

		@SaleToPOIRptRspn.deleter
		def SaleToPOIRptRspn(self):
			del self._SaleToPOIRptRspn
			self._SaleToPOIRptRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptRspn', type=SaleToPOIReportResponseV07, min=1, max=1, mutex_group=None, array=False),
		))

