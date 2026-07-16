# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradeMarginDataTransactionStateReportV02

class AUTH_109_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.109.001.02"
		_docname = "auth.109.001.02"

		__slots__ = ["_DerivsTradMrgnDataTxStatRpt"]
		@property
		def DerivsTradMrgnDataTxStatRpt(self):
			return self._DerivsTradMrgnDataTxStatRpt

		@DerivsTradMrgnDataTxStatRpt.setter
		def DerivsTradMrgnDataTxStatRpt(self, value):
			self._DerivsTradMrgnDataTxStatRpt = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradMrgnDataTxStatRpt', DerivativesTradeMarginDataTransactionStateReportV02, False)

		@DerivsTradMrgnDataTxStatRpt.deleter
		def DerivsTradMrgnDataTxStatRpt(self):
			del self._DerivsTradMrgnDataTxStatRpt
			self._DerivsTradMrgnDataTxStatRpt = base_types.UninitialisedField(self, 'DerivsTradMrgnDataTxStatRpt', DerivativesTradeMarginDataTransactionStateReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradMrgnDataTxStatRpt', type=DerivativesTradeMarginDataTransactionStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))