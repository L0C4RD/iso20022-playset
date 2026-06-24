# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DerivativesTradeReconciliationStatisticalReportV03 import DerivativesTradeReconciliationStatisticalReportV03

class AUTH_091_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.091.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_DerivsTradRcncltnSttstclRpt"]
		@property
		def DerivsTradRcncltnSttstclRpt(self):
			return self._DerivsTradRcncltnSttstclRpt

		@DerivsTradRcncltnSttstclRpt.setter
		def DerivsTradRcncltnSttstclRpt(self, value):
			self._DerivsTradRcncltnSttstclRpt = value if type(value) != base_types.auto else self.make_default("DerivsTradRcncltnSttstclRpt")

		@DerivsTradRcncltnSttstclRpt.deleter
		def DerivsTradRcncltnSttstclRpt(self):
			del self._DerivsTradRcncltnSttstclRpt
			self._DerivsTradRcncltnSttstclRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRcncltnSttstclRpt', type=DerivativesTradeReconciliationStatisticalReportV03, min=1, max=1, mutex_group=None, array=False),
		))