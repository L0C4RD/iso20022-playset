# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionAllegementNotificationV11

class SESE_028_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.028.001.11"
		_docname = "sese.028.001.11"

		__slots__ = ["_SctiesSttlmTxAllgmtNtfctn"]
		@property
		def SctiesSttlmTxAllgmtNtfctn(self):
			return self._SctiesSttlmTxAllgmtNtfctn

		@SctiesSttlmTxAllgmtNtfctn.setter
		def SctiesSttlmTxAllgmtNtfctn(self, value):
			self._SctiesSttlmTxAllgmtNtfctn = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtNtfctn', SecuritiesSettlementTransactionAllegementNotificationV11, False)

		@SctiesSttlmTxAllgmtNtfctn.deleter
		def SctiesSttlmTxAllgmtNtfctn(self):
			del self._SctiesSttlmTxAllgmtNtfctn
			self._SctiesSttlmTxAllgmtNtfctn = base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtNtfctn', SecuritiesSettlementTransactionAllegementNotificationV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtNtfctn', type=SecuritiesSettlementTransactionAllegementNotificationV11, min=1, max=1, mutex_group=None, array=False),
		))