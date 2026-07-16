# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionGenerationNotificationV13

class SESE_032_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.032.001.13"
		_docname = "sese.032.001.13"

		__slots__ = ["_SctiesSttlmTxGnrtnNtfctn"]
		@property
		def SctiesSttlmTxGnrtnNtfctn(self):
			return self._SctiesSttlmTxGnrtnNtfctn

		@SctiesSttlmTxGnrtnNtfctn.setter
		def SctiesSttlmTxGnrtnNtfctn(self, value):
			self._SctiesSttlmTxGnrtnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxGnrtnNtfctn', SecuritiesSettlementTransactionGenerationNotificationV13, False)

		@SctiesSttlmTxGnrtnNtfctn.deleter
		def SctiesSttlmTxGnrtnNtfctn(self):
			del self._SctiesSttlmTxGnrtnNtfctn
			self._SctiesSttlmTxGnrtnNtfctn = base_types.UninitialisedField(self, 'SctiesSttlmTxGnrtnNtfctn', SecuritiesSettlementTransactionGenerationNotificationV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxGnrtnNtfctn', type=SecuritiesSettlementTransactionGenerationNotificationV13, min=1, max=1, mutex_group=None, array=False),
		))