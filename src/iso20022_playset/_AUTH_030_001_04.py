from . import base_types
from .DerivativesTradeReportV04 import DerivativesTradeReportV04

class AUTH_030_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradRpt"]
		@property
		def DerivsTradRpt(self):
			return self._DerivsTradRpt

		@DerivsTradRpt.setter
		def DerivsTradRpt(self, value):
			self._DerivsTradRpt = value if type(value) != base_types.auto else self.make_default("DerivsTradRpt")

		@DerivsTradRpt.deleter
		def DerivsTradRpt(self):
			del self._DerivsTradRpt
			self._DerivsTradRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRpt', type=DerivativesTradeReportV04, min=1, max=1, mutex_group=None, array=False),
		))

