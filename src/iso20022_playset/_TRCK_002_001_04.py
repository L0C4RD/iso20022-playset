# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentStatusTrackerReportV04

class TRCK_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:trck.002.001.04"
		_docname = "trck.002.001.04"

		__slots__ = ["_PmtStsTrckrRpt"]
		@property
		def PmtStsTrckrRpt(self):
			return self._PmtStsTrckrRpt

		@PmtStsTrckrRpt.setter
		def PmtStsTrckrRpt(self, value):
			self._PmtStsTrckrRpt = value if value is not None else base_types.UninitialisedField(self, 'PmtStsTrckrRpt', PaymentStatusTrackerReportV04, False)

		@PmtStsTrckrRpt.deleter
		def PmtStsTrckrRpt(self):
			del self._PmtStsTrckrRpt
			self._PmtStsTrckrRpt = base_types.UninitialisedField(self, 'PmtStsTrckrRpt', PaymentStatusTrackerReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsTrckrRpt', type=PaymentStatusTrackerReportV04, min=1, max=1, mutex_group=None, array=False),
		))