# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CancelTransactionV11 import CancelTransactionV11

class CAMT_008_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.008.001.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CclTx"]
		@property
		def CclTx(self):
			return self._CclTx

		@CclTx.setter
		def CclTx(self, value):
			self._CclTx = value if type(value) != base_types.auto else self.make_default("CclTx")

		@CclTx.deleter
		def CclTx(self):
			del self._CclTx
			self._CclTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CclTx', type=CancelTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))