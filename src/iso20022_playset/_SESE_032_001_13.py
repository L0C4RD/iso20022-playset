# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionGenerationNotificationV13 import SecuritiesSettlementTransactionGenerationNotificationV13

class SESE_032_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.032.001.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxGnrtnNtfctn"]
		@property
		def SctiesSttlmTxGnrtnNtfctn(self):
			return self._SctiesSttlmTxGnrtnNtfctn

		@SctiesSttlmTxGnrtnNtfctn.setter
		def SctiesSttlmTxGnrtnNtfctn(self, value):
			self._SctiesSttlmTxGnrtnNtfctn = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxGnrtnNtfctn")

		@SctiesSttlmTxGnrtnNtfctn.deleter
		def SctiesSttlmTxGnrtnNtfctn(self):
			del self._SctiesSttlmTxGnrtnNtfctn
			self._SctiesSttlmTxGnrtnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxGnrtnNtfctn', type=SecuritiesSettlementTransactionGenerationNotificationV13, min=1, max=1, mutex_group=None, array=False),
		))