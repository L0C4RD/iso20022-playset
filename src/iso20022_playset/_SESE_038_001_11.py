# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionModificationRequestV11 import SecuritiesSettlementTransactionModificationRequestV11

class SESE_038_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.038.001.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxModReq"]
		@property
		def SctiesSttlmTxModReq(self):
			return self._SctiesSttlmTxModReq

		@SctiesSttlmTxModReq.setter
		def SctiesSttlmTxModReq(self, value):
			self._SctiesSttlmTxModReq = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxModReq")

		@SctiesSttlmTxModReq.deleter
		def SctiesSttlmTxModReq(self):
			del self._SctiesSttlmTxModReq
			self._SctiesSttlmTxModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReq', type=SecuritiesSettlementTransactionModificationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))