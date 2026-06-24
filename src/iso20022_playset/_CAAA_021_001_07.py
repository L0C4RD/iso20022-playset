# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransactionAdviceResponseV07 import TransactionAdviceResponseV07

class CAAA_021_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.021.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TxAdvcRspn"]
		@property
		def TxAdvcRspn(self):
			return self._TxAdvcRspn

		@TxAdvcRspn.setter
		def TxAdvcRspn(self, value):
			self._TxAdvcRspn = value if type(value) != base_types.auto else self.make_default("TxAdvcRspn")

		@TxAdvcRspn.deleter
		def TxAdvcRspn(self):
			del self._TxAdvcRspn
			self._TxAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxAdvcRspn', type=TransactionAdviceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))