# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFIPaymentStatusRequestV06 import FIToFIPaymentStatusRequestV06

class PACS_028_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FIToFIPmtStsReq"]
		@property
		def FIToFIPmtStsReq(self):
			return self._FIToFIPmtStsReq

		@FIToFIPmtStsReq.setter
		def FIToFIPmtStsReq(self, value):
			self._FIToFIPmtStsReq = value if type(value) != base_types.auto else self.make_default("FIToFIPmtStsReq")

		@FIToFIPmtStsReq.deleter
		def FIToFIPmtStsReq(self):
			del self._FIToFIPmtStsReq
			self._FIToFIPmtStsReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtStsReq', type=FIToFIPaymentStatusRequestV06, min=1, max=1, mutex_group=None, array=False),
		))