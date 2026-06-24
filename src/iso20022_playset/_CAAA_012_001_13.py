# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorBatchTransferResponseV13 import AcceptorBatchTransferResponseV13

class CAAA_012_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:caaa.012.001.13",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AccptrBtchTrfRspn"]
		@property
		def AccptrBtchTrfRspn(self):
			return self._AccptrBtchTrfRspn

		@AccptrBtchTrfRspn.setter
		def AccptrBtchTrfRspn(self, value):
			self._AccptrBtchTrfRspn = value if type(value) != base_types.auto else self.make_default("AccptrBtchTrfRspn")

		@AccptrBtchTrfRspn.deleter
		def AccptrBtchTrfRspn(self):
			del self._AccptrBtchTrfRspn
			self._AccptrBtchTrfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrBtchTrfRspn', type=AcceptorBatchTransferResponseV13, min=1, max=1, mutex_group=None, array=False),
		))