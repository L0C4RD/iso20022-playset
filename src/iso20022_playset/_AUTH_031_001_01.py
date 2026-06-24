# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingStatusAdviceV01 import FinancialInstrumentReportingStatusAdviceV01

class AUTH_031_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.031.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FinInstrmRptgStsAdvc"]
		@property
		def FinInstrmRptgStsAdvc(self):
			return self._FinInstrmRptgStsAdvc

		@FinInstrmRptgStsAdvc.setter
		def FinInstrmRptgStsAdvc(self, value):
			self._FinInstrmRptgStsAdvc = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgStsAdvc")

		@FinInstrmRptgStsAdvc.deleter
		def FinInstrmRptgStsAdvc(self):
			del self._FinInstrmRptgStsAdvc
			self._FinInstrmRptgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgStsAdvc', type=FinancialInstrumentReportingStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))