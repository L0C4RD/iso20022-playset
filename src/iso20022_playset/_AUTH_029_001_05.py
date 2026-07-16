# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradeReportQueryV05

class AUTH_029_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05"
		_docname = "auth.029.001.05"

		__slots__ = ["_DerivsTradRptQry"]
		@property
		def DerivsTradRptQry(self):
			return self._DerivsTradRptQry

		@DerivsTradRptQry.setter
		def DerivsTradRptQry(self, value):
			self._DerivsTradRptQry = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradRptQry', DerivativesTradeReportQueryV05, False)

		@DerivsTradRptQry.deleter
		def DerivsTradRptQry(self):
			del self._DerivsTradRptQry
			self._DerivsTradRptQry = base_types.UninitialisedField(self, 'DerivsTradRptQry', DerivativesTradeReportQueryV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRptQry', type=DerivativesTradeReportQueryV05, min=1, max=1, mutex_group=None, array=False),
		))