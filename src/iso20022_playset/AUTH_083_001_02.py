from . import base_types
import SecuritiesFinancingReportingMissingCollateralRequestV02

class AUTH_083_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgMssngCollReq"]
		@property
		def SctiesFincgRptgMssngCollReq(self):
			return self._SctiesFincgRptgMssngCollReq

		@SctiesFincgRptgMssngCollReq.setter
		def SctiesFincgRptgMssngCollReq(self, value):
			self._SctiesFincgRptgMssngCollReq = value if type(value) != auto else self.make_default("SctiesFincgRptgMssngCollReq")

		@SctiesFincgRptgMssngCollReq.deleter
		def SctiesFincgRptgMssngCollReq(self):
			del self._SctiesFincgRptgMssngCollReq
			self._SctiesFincgRptgMssngCollReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgMssngCollReq', type=SecuritiesFinancingReportingMissingCollateralRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

