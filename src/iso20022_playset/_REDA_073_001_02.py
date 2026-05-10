from . import base_types
from ._RequestToPayDebtorActivationStatusReportV02 import RequestToPayDebtorActivationStatusReportV02

class REDA_073_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqToPayDbtrActvtnStsRpt"]
		@property
		def ReqToPayDbtrActvtnStsRpt(self):
			return self._ReqToPayDbtrActvtnStsRpt

		@ReqToPayDbtrActvtnStsRpt.setter
		def ReqToPayDbtrActvtnStsRpt(self, value):
			self._ReqToPayDbtrActvtnStsRpt = value if type(value) != base_types.auto else self.make_default("ReqToPayDbtrActvtnStsRpt")

		@ReqToPayDbtrActvtnStsRpt.deleter
		def ReqToPayDbtrActvtnStsRpt(self):
			del self._ReqToPayDbtrActvtnStsRpt
			self._ReqToPayDbtrActvtnStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnStsRpt', type=RequestToPayDebtorActivationStatusReportV02, min=1, max=1, mutex_group=None, array=False),
		))

