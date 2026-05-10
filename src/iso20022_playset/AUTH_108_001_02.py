from . import base_types
from .DerivativesTradeMarginDataReportV02 import DerivativesTradeMarginDataReportV02

class AUTH_108_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradMrgnDataRpt"]
		@property
		def DerivsTradMrgnDataRpt(self):
			return self._DerivsTradMrgnDataRpt

		@DerivsTradMrgnDataRpt.setter
		def DerivsTradMrgnDataRpt(self, value):
			self._DerivsTradMrgnDataRpt = value if type(value) != auto else self.make_default("DerivsTradMrgnDataRpt")

		@DerivsTradMrgnDataRpt.deleter
		def DerivsTradMrgnDataRpt(self):
			del self._DerivsTradMrgnDataRpt
			self._DerivsTradMrgnDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradMrgnDataRpt', type=DerivativesTradeMarginDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))

