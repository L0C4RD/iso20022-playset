# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionModificationRequestV11

class SESE_038_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.038.001.11"
		_docname = "sese.038.001.11"

		__slots__ = ["_SctiesSttlmTxModReq"]
		@property
		def SctiesSttlmTxModReq(self):
			return self._SctiesSttlmTxModReq

		@SctiesSttlmTxModReq.setter
		def SctiesSttlmTxModReq(self, value):
			self._SctiesSttlmTxModReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxModReq', SecuritiesSettlementTransactionModificationRequestV11, False)

		@SctiesSttlmTxModReq.deleter
		def SctiesSttlmTxModReq(self):
			del self._SctiesSttlmTxModReq
			self._SctiesSttlmTxModReq = base_types.UninitialisedField(self, 'SctiesSttlmTxModReq', SecuritiesSettlementTransactionModificationRequestV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReq', type=SecuritiesSettlementTransactionModificationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))