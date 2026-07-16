# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsMonthlyReportV01

class AUTH_100_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01"
		_docname = "auth.100.001.01"

		__slots__ = ["_SttlmFlsMnthlyRpt"]
		@property
		def SttlmFlsMnthlyRpt(self):
			return self._SttlmFlsMnthlyRpt

		@SttlmFlsMnthlyRpt.setter
		def SttlmFlsMnthlyRpt(self, value):
			self._SttlmFlsMnthlyRpt = value if value is not None else base_types.UninitialisedField(self, 'SttlmFlsMnthlyRpt', SettlementFailsMonthlyReportV01, False)

		@SttlmFlsMnthlyRpt.deleter
		def SttlmFlsMnthlyRpt(self):
			del self._SttlmFlsMnthlyRpt
			self._SttlmFlsMnthlyRpt = base_types.UninitialisedField(self, 'SttlmFlsMnthlyRpt', SettlementFailsMonthlyReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmFlsMnthlyRpt', type=SettlementFailsMonthlyReportV01, min=1, max=1, mutex_group=None, array=False),
		))