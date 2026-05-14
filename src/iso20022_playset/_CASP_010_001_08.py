from . import base_types
from ._SaleToPOIReportResponseV08 import SaleToPOIReportResponseV08

class CASP_010_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIRptRspn"]
		@property
		def SaleToPOIRptRspn(self):
			return self._SaleToPOIRptRspn

		@SaleToPOIRptRspn.setter
		def SaleToPOIRptRspn(self, value):
			self._SaleToPOIRptRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIRptRspn")

		@SaleToPOIRptRspn.deleter
		def SaleToPOIRptRspn(self):
			del self._SaleToPOIRptRspn
			self._SaleToPOIRptRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRptRspn', type=SaleToPOIReportResponseV08, min=1, max=1, mutex_group=None, array=False),
		))

