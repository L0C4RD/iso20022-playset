# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MoneyMarketStatisticalReportStatusAdviceV01 import MoneyMarketStatisticalReportStatusAdviceV01

class AUTH_028_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.028.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_MnyMktSttstclRptStsAdvc"]
		@property
		def MnyMktSttstclRptStsAdvc(self):
			return self._MnyMktSttstclRptStsAdvc

		@MnyMktSttstclRptStsAdvc.setter
		def MnyMktSttstclRptStsAdvc(self, value):
			self._MnyMktSttstclRptStsAdvc = value if type(value) != base_types.auto else self.make_default("MnyMktSttstclRptStsAdvc")

		@MnyMktSttstclRptStsAdvc.deleter
		def MnyMktSttstclRptStsAdvc(self):
			del self._MnyMktSttstclRptStsAdvc
			self._MnyMktSttstclRptStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktSttstclRptStsAdvc', type=MoneyMarketStatisticalReportStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))