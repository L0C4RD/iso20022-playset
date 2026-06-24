# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionCancellationRequestV09 import SecuritiesTransactionCancellationRequestV09

class SESE_020_001_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.020.001.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesTxCxlReq"]
		@property
		def SctiesTxCxlReq(self):
			return self._SctiesTxCxlReq

		@SctiesTxCxlReq.setter
		def SctiesTxCxlReq(self, value):
			self._SctiesTxCxlReq = value if type(value) != base_types.auto else self.make_default("SctiesTxCxlReq")

		@SctiesTxCxlReq.deleter
		def SctiesTxCxlReq(self):
			del self._SctiesTxCxlReq
			self._SctiesTxCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReq', type=SecuritiesTransactionCancellationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))