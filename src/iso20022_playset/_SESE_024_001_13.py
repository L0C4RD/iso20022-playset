# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionStatusAdviceV13 import SecuritiesSettlementTransactionStatusAdviceV13

class SESE_024_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.024.001.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxStsAdvc"]
		@property
		def SctiesSttlmTxStsAdvc(self):
			return self._SctiesSttlmTxStsAdvc

		@SctiesSttlmTxStsAdvc.setter
		def SctiesSttlmTxStsAdvc(self, value):
			self._SctiesSttlmTxStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxStsAdvc")

		@SctiesSttlmTxStsAdvc.deleter
		def SctiesSttlmTxStsAdvc(self):
			del self._SctiesSttlmTxStsAdvc
			self._SctiesSttlmTxStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxStsAdvc', type=SecuritiesSettlementTransactionStatusAdviceV13, min=1, max=1, mutex_group=None, array=False),
		))