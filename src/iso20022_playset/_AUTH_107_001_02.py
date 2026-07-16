# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradeStateReportV02

class AUTH_107_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.107.001.02"
		_docname = "auth.107.001.02"

		__slots__ = ["_DerivsTradStatRpt"]
		@property
		def DerivsTradStatRpt(self):
			return self._DerivsTradStatRpt

		@DerivsTradStatRpt.setter
		def DerivsTradStatRpt(self, value):
			self._DerivsTradStatRpt = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradStatRpt', DerivativesTradeStateReportV02, False)

		@DerivsTradStatRpt.deleter
		def DerivsTradStatRpt(self):
			del self._DerivsTradStatRpt
			self._DerivsTradStatRpt = base_types.UninitialisedField(self, 'DerivsTradStatRpt', DerivativesTradeStateReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradStatRpt', type=DerivativesTradeStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))