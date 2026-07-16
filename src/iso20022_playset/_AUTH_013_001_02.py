# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MoneyMarketUnsecuredMarketStatisticalReportV02

class AUTH_013_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02"
		_docname = "auth.013.001.02"

		__slots__ = ["_MnyMktUscrdMktSttstclRpt"]
		@property
		def MnyMktUscrdMktSttstclRpt(self):
			return self._MnyMktUscrdMktSttstclRpt

		@MnyMktUscrdMktSttstclRpt.setter
		def MnyMktUscrdMktSttstclRpt(self, value):
			self._MnyMktUscrdMktSttstclRpt = value if value is not None else base_types.UninitialisedField(self, 'MnyMktUscrdMktSttstclRpt', MoneyMarketUnsecuredMarketStatisticalReportV02, False)

		@MnyMktUscrdMktSttstclRpt.deleter
		def MnyMktUscrdMktSttstclRpt(self):
			del self._MnyMktUscrdMktSttstclRpt
			self._MnyMktUscrdMktSttstclRpt = base_types.UninitialisedField(self, 'MnyMktUscrdMktSttstclRpt', MoneyMarketUnsecuredMarketStatisticalReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktUscrdMktSttstclRpt', type=MoneyMarketUnsecuredMarketStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))