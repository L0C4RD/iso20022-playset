from . import base_types
import DerivativesTradeMarginDataTransactionStateReportV02

class AUTH_109_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradMrgnDataTxStatRpt"]
		@property
		def DerivsTradMrgnDataTxStatRpt(self):
			return self._DerivsTradMrgnDataTxStatRpt

		@DerivsTradMrgnDataTxStatRpt.setter
		def DerivsTradMrgnDataTxStatRpt(self, value):
			self._DerivsTradMrgnDataTxStatRpt = value if type(value) != auto else self.make_default("DerivsTradMrgnDataTxStatRpt")

		@DerivsTradMrgnDataTxStatRpt.deleter
		def DerivsTradMrgnDataTxStatRpt(self):
			del self._DerivsTradMrgnDataTxStatRpt
			self._DerivsTradMrgnDataTxStatRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradMrgnDataTxStatRpt', type=DerivativesTradeMarginDataTransactionStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))

