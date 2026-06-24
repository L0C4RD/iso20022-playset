# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentStatusTrackerReportV04 import PaymentStatusTrackerReportV04

class TRCK_002_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:trck.002.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PmtStsTrckrRpt"]
		@property
		def PmtStsTrckrRpt(self):
			return self._PmtStsTrckrRpt

		@PmtStsTrckrRpt.setter
		def PmtStsTrckrRpt(self, value):
			self._PmtStsTrckrRpt = value if type(value) != base_types.auto else self.make_default("PmtStsTrckrRpt")

		@PmtStsTrckrRpt.deleter
		def PmtStsTrckrRpt(self):
			del self._PmtStsTrckrRpt
			self._PmtStsTrckrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsTrckrRpt', type=PaymentStatusTrackerReportV04, min=1, max=1, mutex_group=None, array=False),
		))