# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DerivativesTradeRejectionStatisticalReportV04 import DerivativesTradeRejectionStatisticalReportV04

class AUTH_092_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.092.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_DerivsTradRjctnSttstclRpt"]
		@property
		def DerivsTradRjctnSttstclRpt(self):
			return self._DerivsTradRjctnSttstclRpt

		@DerivsTradRjctnSttstclRpt.setter
		def DerivsTradRjctnSttstclRpt(self, value):
			self._DerivsTradRjctnSttstclRpt = value if type(value) != base_types.auto else self.make_default("DerivsTradRjctnSttstclRpt")

		@DerivsTradRjctnSttstclRpt.deleter
		def DerivsTradRjctnSttstclRpt(self):
			del self._DerivsTradRjctnSttstclRpt
			self._DerivsTradRjctnSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRjctnSttstclRpt', type=DerivativesTradeRejectionStatisticalReportV04, min=1, max=1, mutex_group=None, array=False),
		))