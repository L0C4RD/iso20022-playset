from . import base_types
from ._SecuritiesFinancingReportingReconciliationStatusAdviceV02 import SecuritiesFinancingReportingReconciliationStatusAdviceV02

class AUTH_080_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgRcncltnStsAdvc"]
		@property
		def SctiesFincgRptgRcncltnStsAdvc(self):
			return self._SctiesFincgRptgRcncltnStsAdvc

		@SctiesFincgRptgRcncltnStsAdvc.setter
		def SctiesFincgRptgRcncltnStsAdvc(self, value):
			self._SctiesFincgRptgRcncltnStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgRcncltnStsAdvc")

		@SctiesFincgRptgRcncltnStsAdvc.deleter
		def SctiesFincgRptgRcncltnStsAdvc(self):
			del self._SctiesFincgRptgRcncltnStsAdvc
			self._SctiesFincgRptgRcncltnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgRcncltnStsAdvc', type=SecuritiesFinancingReportingReconciliationStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

