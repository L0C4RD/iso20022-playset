# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFIPaymentStatusReportV15 import FIToFIPaymentStatusReportV15

class PACS_002_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.002.001.15"
		_docname = "pacs.002.001.15"

		__slots__ = ["_FIToFIPmtStsRpt"]
		@property
		def FIToFIPmtStsRpt(self):
			return self._FIToFIPmtStsRpt

		@FIToFIPmtStsRpt.setter
		def FIToFIPmtStsRpt(self, value):
			self._FIToFIPmtStsRpt = value if type(value) != base_types.auto else self.make_default("FIToFIPmtStsRpt")

		@FIToFIPmtStsRpt.deleter
		def FIToFIPmtStsRpt(self):
			del self._FIToFIPmtStsRpt
			self._FIToFIPmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtStsRpt', type=FIToFIPaymentStatusReportV15, min=1, max=1, mutex_group=None, array=False),
		))