# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentStatusCustomerTrackerReportV03 import PaymentStatusCustomerTrackerReportV03

class TRCK_004_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:trck.004.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_PmtStsCstmrTrckrRpt"]
		@property
		def PmtStsCstmrTrckrRpt(self):
			return self._PmtStsCstmrTrckrRpt

		@PmtStsCstmrTrckrRpt.setter
		def PmtStsCstmrTrckrRpt(self, value):
			self._PmtStsCstmrTrckrRpt = value if type(value) != base_types.auto else self.make_default("PmtStsCstmrTrckrRpt")

		@PmtStsCstmrTrckrRpt.deleter
		def PmtStsCstmrTrckrRpt(self):
			del self._PmtStsCstmrTrckrRpt
			self._PmtStsCstmrTrckrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsCstmrTrckrRpt', type=PaymentStatusCustomerTrackerReportV03, min=1, max=1, mutex_group=None, array=False),
		))