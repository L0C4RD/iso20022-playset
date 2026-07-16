# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradeMarginDataReportV02

class AUTH_108_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02"
		_docname = "auth.108.001.02"

		__slots__ = ["_DerivsTradMrgnDataRpt"]
		@property
		def DerivsTradMrgnDataRpt(self):
			return self._DerivsTradMrgnDataRpt

		@DerivsTradMrgnDataRpt.setter
		def DerivsTradMrgnDataRpt(self, value):
			self._DerivsTradMrgnDataRpt = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradMrgnDataRpt', DerivativesTradeMarginDataReportV02, False)

		@DerivsTradMrgnDataRpt.deleter
		def DerivsTradMrgnDataRpt(self):
			del self._DerivsTradMrgnDataRpt
			self._DerivsTradMrgnDataRpt = base_types.UninitialisedField(self, 'DerivsTradMrgnDataRpt', DerivativesTradeMarginDataReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradMrgnDataRpt', type=DerivativesTradeMarginDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))