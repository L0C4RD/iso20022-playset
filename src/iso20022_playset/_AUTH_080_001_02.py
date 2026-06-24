# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingReconciliationStatusAdviceV02 import SecuritiesFinancingReportingReconciliationStatusAdviceV02

class AUTH_080_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.080.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesFincgRptgRcncltnStsAdvc"]
		@property
		def SctiesFincgRptgRcncltnStsAdvc(self):
			return self._SctiesFincgRptgRcncltnStsAdvc

		@SctiesFincgRptgRcncltnStsAdvc.setter
		def SctiesFincgRptgRcncltnStsAdvc(self, value):
			self._SctiesFincgRptgRcncltnStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgRcncltnStsAdvc")

		@SctiesFincgRptgRcncltnStsAdvc.deleter
		def SctiesFincgRptgRcncltnStsAdvc(self):
			del self._SctiesFincgRptgRcncltnStsAdvc
			self._SctiesFincgRptgRcncltnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgRcncltnStsAdvc', type=SecuritiesFinancingReportingReconciliationStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))