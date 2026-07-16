# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MoneyMarketOvernightIndexSwapsStatisticalReportV02

class AUTH_015_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.015.001.02"
		_docname = "auth.015.001.02"

		__slots__ = ["_MnyMktOvrnghtIndxSwpsSttstclRpt"]
		@property
		def MnyMktOvrnghtIndxSwpsSttstclRpt(self):
			return self._MnyMktOvrnghtIndxSwpsSttstclRpt

		@MnyMktOvrnghtIndxSwpsSttstclRpt.setter
		def MnyMktOvrnghtIndxSwpsSttstclRpt(self, value):
			self._MnyMktOvrnghtIndxSwpsSttstclRpt = value if value is not None else base_types.UninitialisedField(self, 'MnyMktOvrnghtIndxSwpsSttstclRpt', MoneyMarketOvernightIndexSwapsStatisticalReportV02, False)

		@MnyMktOvrnghtIndxSwpsSttstclRpt.deleter
		def MnyMktOvrnghtIndxSwpsSttstclRpt(self):
			del self._MnyMktOvrnghtIndxSwpsSttstclRpt
			self._MnyMktOvrnghtIndxSwpsSttstclRpt = base_types.UninitialisedField(self, 'MnyMktOvrnghtIndxSwpsSttstclRpt', MoneyMarketOvernightIndexSwapsStatisticalReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MnyMktOvrnghtIndxSwpsSttstclRpt', type=MoneyMarketOvernightIndexSwapsStatisticalReportV02, min=1, max=1, mutex_group=None, array=False),
		))