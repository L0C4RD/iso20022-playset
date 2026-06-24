# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionQueryResponseV01 import SecuritiesSettlementTransactionQueryResponseV01

class SEMT_027_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.027.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxQryRspn"]
		@property
		def SctiesSttlmTxQryRspn(self):
			return self._SctiesSttlmTxQryRspn

		@SctiesSttlmTxQryRspn.setter
		def SctiesSttlmTxQryRspn(self, value):
			self._SctiesSttlmTxQryRspn = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxQryRspn")

		@SctiesSttlmTxQryRspn.deleter
		def SctiesSttlmTxQryRspn(self):
			del self._SctiesSttlmTxQryRspn
			self._SctiesSttlmTxQryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxQryRspn', type=SecuritiesSettlementTransactionQueryResponseV01, min=1, max=1, mutex_group=None, array=False),
		))