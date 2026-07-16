# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradeRejectionStatisticalReportV04

class AUTH_092_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04"
		_docname = "auth.092.001.04"

		__slots__ = ["_DerivsTradRjctnSttstclRpt"]
		@property
		def DerivsTradRjctnSttstclRpt(self):
			return self._DerivsTradRjctnSttstclRpt

		@DerivsTradRjctnSttstclRpt.setter
		def DerivsTradRjctnSttstclRpt(self, value):
			self._DerivsTradRjctnSttstclRpt = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradRjctnSttstclRpt', DerivativesTradeRejectionStatisticalReportV04, False)

		@DerivsTradRjctnSttstclRpt.deleter
		def DerivsTradRjctnSttstclRpt(self):
			del self._DerivsTradRjctnSttstclRpt
			self._DerivsTradRjctnSttstclRpt = base_types.UninitialisedField(self, 'DerivsTradRjctnSttstclRpt', DerivativesTradeRejectionStatisticalReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRjctnSttstclRpt', type=DerivativesTradeRejectionStatisticalReportV04, min=1, max=1, mutex_group=None, array=False),
		))