from . import base_types
from .DerivativesTradeRejectionStatisticalReportV04 import DerivativesTradeRejectionStatisticalReportV04

class AUTH_092_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradRjctnSttstclRpt"]
		@property
		def DerivsTradRjctnSttstclRpt(self):
			return self._DerivsTradRjctnSttstclRpt

		@DerivsTradRjctnSttstclRpt.setter
		def DerivsTradRjctnSttstclRpt(self, value):
			self._DerivsTradRjctnSttstclRpt = value if type(value) != auto else self.make_default("DerivsTradRjctnSttstclRpt")

		@DerivsTradRjctnSttstclRpt.deleter
		def DerivsTradRjctnSttstclRpt(self):
			del self._DerivsTradRjctnSttstclRpt
			self._DerivsTradRjctnSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRjctnSttstclRpt', type=DerivativesTradeRejectionStatisticalReportV04, min=1, max=1, mutex_group=None, array=False),
		))

