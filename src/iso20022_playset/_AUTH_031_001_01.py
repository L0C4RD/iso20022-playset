# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentReportingStatusAdviceV01

class AUTH_031_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01"
		_docname = "auth.031.001.01"

		__slots__ = ["_FinInstrmRptgStsAdvc"]
		@property
		def FinInstrmRptgStsAdvc(self):
			return self._FinInstrmRptgStsAdvc

		@FinInstrmRptgStsAdvc.setter
		def FinInstrmRptgStsAdvc(self, value):
			self._FinInstrmRptgStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmRptgStsAdvc', FinancialInstrumentReportingStatusAdviceV01, False)

		@FinInstrmRptgStsAdvc.deleter
		def FinInstrmRptgStsAdvc(self):
			del self._FinInstrmRptgStsAdvc
			self._FinInstrmRptgStsAdvc = base_types.UninitialisedField(self, 'FinInstrmRptgStsAdvc', FinancialInstrumentReportingStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgStsAdvc', type=FinancialInstrumentReportingStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))