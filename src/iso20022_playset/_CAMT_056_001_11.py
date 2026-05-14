# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFIPaymentCancellationRequestV11 import FIToFIPaymentCancellationRequestV11

class CAMT_056_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FIToFIPmtCxlReq"]
		@property
		def FIToFIPmtCxlReq(self):
			return self._FIToFIPmtCxlReq

		@FIToFIPmtCxlReq.setter
		def FIToFIPmtCxlReq(self, value):
			self._FIToFIPmtCxlReq = value if type(value) != base_types.auto else self.make_default("FIToFIPmtCxlReq")

		@FIToFIPmtCxlReq.deleter
		def FIToFIPmtCxlReq(self):
			del self._FIToFIPmtCxlReq
			self._FIToFIPmtCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtCxlReq', type=FIToFIPaymentCancellationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))