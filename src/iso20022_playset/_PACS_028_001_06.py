# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FIToFIPaymentStatusRequestV06

class PACS_028_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.028.001.06"
		_docname = "pacs.028.001.06"

		__slots__ = ["_FIToFIPmtStsReq"]
		@property
		def FIToFIPmtStsReq(self):
			return self._FIToFIPmtStsReq

		@FIToFIPmtStsReq.setter
		def FIToFIPmtStsReq(self, value):
			self._FIToFIPmtStsReq = value if value is not None else base_types.UninitialisedField(self, 'FIToFIPmtStsReq', FIToFIPaymentStatusRequestV06, False)

		@FIToFIPmtStsReq.deleter
		def FIToFIPmtStsReq(self):
			del self._FIToFIPmtStsReq
			self._FIToFIPmtStsReq = base_types.UninitialisedField(self, 'FIToFIPmtStsReq', FIToFIPaymentStatusRequestV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtStsReq', type=FIToFIPaymentStatusRequestV06, min=1, max=1, mutex_group=None, array=False),
		))