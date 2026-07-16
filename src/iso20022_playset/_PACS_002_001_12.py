# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FIToFIPaymentStatusReportV12

class PACS_002_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12"
		_docname = "pacs.002.001.12"

		__slots__ = ["_FIToFIPmtStsRpt"]
		@property
		def FIToFIPmtStsRpt(self):
			return self._FIToFIPmtStsRpt

		@FIToFIPmtStsRpt.setter
		def FIToFIPmtStsRpt(self, value):
			self._FIToFIPmtStsRpt = value if value is not None else base_types.UninitialisedField(self, 'FIToFIPmtStsRpt', FIToFIPaymentStatusReportV12, False)

		@FIToFIPmtStsRpt.deleter
		def FIToFIPmtStsRpt(self):
			del self._FIToFIPmtStsRpt
			self._FIToFIPmtStsRpt = base_types.UninitialisedField(self, 'FIToFIPmtStsRpt', FIToFIPaymentStatusReportV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtStsRpt', type=FIToFIPaymentStatusReportV12, min=1, max=1, mutex_group=None, array=False),
		))