# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DerivativesTradeWarningsReportV01 import DerivativesTradeWarningsReportV01

class AUTH_106_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_DerivsTradWrnngsRpt"]
		@property
		def DerivsTradWrnngsRpt(self):
			return self._DerivsTradWrnngsRpt

		@DerivsTradWrnngsRpt.setter
		def DerivsTradWrnngsRpt(self, value):
			self._DerivsTradWrnngsRpt = value if type(value) != base_types.auto else self.make_default("DerivsTradWrnngsRpt")

		@DerivsTradWrnngsRpt.deleter
		def DerivsTradWrnngsRpt(self):
			del self._DerivsTradWrnngsRpt
			self._DerivsTradWrnngsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradWrnngsRpt', type=DerivativesTradeWarningsReportV01, min=1, max=1, mutex_group=None, array=False),
		))