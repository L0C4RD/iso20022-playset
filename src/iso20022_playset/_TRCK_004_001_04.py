# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentStatusCustomerTrackerReportV04

class TRCK_004_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:trck.004.001.04"
		_docname = "trck.004.001.04"

		__slots__ = ["_PmtStsCstmrTrckrRpt"]
		@property
		def PmtStsCstmrTrckrRpt(self):
			return self._PmtStsCstmrTrckrRpt

		@PmtStsCstmrTrckrRpt.setter
		def PmtStsCstmrTrckrRpt(self, value):
			self._PmtStsCstmrTrckrRpt = value if value is not None else base_types.UninitialisedField(self, 'PmtStsCstmrTrckrRpt', PaymentStatusCustomerTrackerReportV04, False)

		@PmtStsCstmrTrckrRpt.deleter
		def PmtStsCstmrTrckrRpt(self):
			del self._PmtStsCstmrTrckrRpt
			self._PmtStsCstmrTrckrRpt = base_types.UninitialisedField(self, 'PmtStsCstmrTrckrRpt', PaymentStatusCustomerTrackerReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsCstmrTrckrRpt', type=PaymentStatusCustomerTrackerReportV04, min=1, max=1, mutex_group=None, array=False),
		))