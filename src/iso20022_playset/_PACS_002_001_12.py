# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFIPaymentStatusReportV12 import FIToFIPaymentStatusReportV12

class PACS_002_001_12():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:pacs.002.001.12"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

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
			base_types.FieldEntry(name='FIToFIPmtStsRpt', type=FIToFIPaymentStatusReportV12, min=1, max=1, mutex_group=None, array=False),
		))