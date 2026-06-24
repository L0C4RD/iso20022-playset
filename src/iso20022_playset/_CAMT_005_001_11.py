# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GetTransactionV11 import GetTransactionV11

class CAMT_005_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.005.001.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_GetTx"]
		@property
		def GetTx(self):
			return self._GetTx

		@GetTx.setter
		def GetTx(self, value):
			self._GetTx = value if type(value) != base_types.auto else self.make_default("GetTx")

		@GetTx.deleter
		def GetTx(self):
			del self._GetTx
			self._GetTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetTx', type=GetTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))