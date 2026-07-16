# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradeReportV04

class AUTH_030_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04"
		_docname = "auth.030.001.04"

		__slots__ = ["_DerivsTradRpt"]
		@property
		def DerivsTradRpt(self):
			return self._DerivsTradRpt

		@DerivsTradRpt.setter
		def DerivsTradRpt(self, value):
			self._DerivsTradRpt = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradRpt', DerivativesTradeReportV04, False)

		@DerivsTradRpt.deleter
		def DerivsTradRpt(self):
			del self._DerivsTradRpt
			self._DerivsTradRpt = base_types.UninitialisedField(self, 'DerivsTradRpt', DerivativesTradeReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRpt', type=DerivativesTradeReportV04, min=1, max=1, mutex_group=None, array=False),
		))