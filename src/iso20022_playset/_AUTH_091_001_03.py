from . import base_types
from ._DerivativesTradeReconciliationStatisticalReportV03 import DerivativesTradeReconciliationStatisticalReportV03

class AUTH_091_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradRcncltnSttstclRpt"]
		@property
		def DerivsTradRcncltnSttstclRpt(self):
			return self._DerivsTradRcncltnSttstclRpt

		@DerivsTradRcncltnSttstclRpt.setter
		def DerivsTradRcncltnSttstclRpt(self, value):
			self._DerivsTradRcncltnSttstclRpt = value if type(value) != base_types.auto else self.make_default("DerivsTradRcncltnSttstclRpt")

		@DerivsTradRcncltnSttstclRpt.deleter
		def DerivsTradRcncltnSttstclRpt(self):
			del self._DerivsTradRcncltnSttstclRpt
			self._DerivsTradRcncltnSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRcncltnSttstclRpt', type=DerivativesTradeReconciliationStatisticalReportV03, min=1, max=1, mutex_group=None, array=False),
		))

