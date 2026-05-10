from . import base_types
from .DerivativesTradePositionSetReportV02 import DerivativesTradePositionSetReportV02

class AUTH_090_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradPosSetRpt"]
		@property
		def DerivsTradPosSetRpt(self):
			return self._DerivsTradPosSetRpt

		@DerivsTradPosSetRpt.setter
		def DerivsTradPosSetRpt(self, value):
			self._DerivsTradPosSetRpt = value if type(value) != base_types.auto else self.make_default("DerivsTradPosSetRpt")

		@DerivsTradPosSetRpt.deleter
		def DerivsTradPosSetRpt(self):
			del self._DerivsTradPosSetRpt
			self._DerivsTradPosSetRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradPosSetRpt', type=DerivativesTradePositionSetReportV02, min=1, max=1, mutex_group=None, array=False),
		))

