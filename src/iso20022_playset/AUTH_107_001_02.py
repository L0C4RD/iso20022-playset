from . import base_types
import DerivativesTradeStateReportV02

class AUTH_107_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradStatRpt"]
		@property
		def DerivsTradStatRpt(self):
			return self._DerivsTradStatRpt

		@DerivsTradStatRpt.setter
		def DerivsTradStatRpt(self, value):
			self._DerivsTradStatRpt = value if type(value) != auto else self.make_default("DerivsTradStatRpt")

		@DerivsTradStatRpt.deleter
		def DerivsTradStatRpt(self):
			del self._DerivsTradStatRpt
			self._DerivsTradStatRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradStatRpt', type=DerivativesTradeStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))

