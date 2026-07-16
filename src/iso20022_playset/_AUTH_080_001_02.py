# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingReportingReconciliationStatusAdviceV02

class AUTH_080_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.080.001.02"
		_docname = "auth.080.001.02"

		__slots__ = ["_SctiesFincgRptgRcncltnStsAdvc"]
		@property
		def SctiesFincgRptgRcncltnStsAdvc(self):
			return self._SctiesFincgRptgRcncltnStsAdvc

		@SctiesFincgRptgRcncltnStsAdvc.setter
		def SctiesFincgRptgRcncltnStsAdvc(self, value):
			self._SctiesFincgRptgRcncltnStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgRptgRcncltnStsAdvc', SecuritiesFinancingReportingReconciliationStatusAdviceV02, False)

		@SctiesFincgRptgRcncltnStsAdvc.deleter
		def SctiesFincgRptgRcncltnStsAdvc(self):
			del self._SctiesFincgRptgRcncltnStsAdvc
			self._SctiesFincgRptgRcncltnStsAdvc = base_types.UninitialisedField(self, 'SctiesFincgRptgRcncltnStsAdvc', SecuritiesFinancingReportingReconciliationStatusAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgRcncltnStsAdvc', type=SecuritiesFinancingReportingReconciliationStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))