# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BatchTransferResponseV04 import BatchTransferResponseV04

class CAAD_004_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caad.004.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BtchTrfRspn"]
		@property
		def BtchTrfRspn(self):
			return self._BtchTrfRspn

		@BtchTrfRspn.setter
		def BtchTrfRspn(self, value):
			self._BtchTrfRspn = value if type(value) != base_types.auto else self.make_default("BtchTrfRspn")

		@BtchTrfRspn.deleter
		def BtchTrfRspn(self):
			del self._BtchTrfRspn
			self._BtchTrfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchTrfRspn', type=BatchTransferResponseV04, min=1, max=1, mutex_group=None, array=False),
		))