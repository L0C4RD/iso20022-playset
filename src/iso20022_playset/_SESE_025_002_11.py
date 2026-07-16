# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionConfirmation002V11

class SESE_025_002_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.025.002.11"
		_docname = "sese.025.002.11"

		__slots__ = ["_SctiesSttlmTxConf"]
		@property
		def SctiesSttlmTxConf(self):
			return self._SctiesSttlmTxConf

		@SctiesSttlmTxConf.setter
		def SctiesSttlmTxConf(self, value):
			self._SctiesSttlmTxConf = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxConf', SecuritiesSettlementTransactionConfirmation002V11, False)

		@SctiesSttlmTxConf.deleter
		def SctiesSttlmTxConf(self):
			del self._SctiesSttlmTxConf
			self._SctiesSttlmTxConf = base_types.UninitialisedField(self, 'SctiesSttlmTxConf', SecuritiesSettlementTransactionConfirmation002V11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxConf', type=SecuritiesSettlementTransactionConfirmation002V11, min=1, max=1, mutex_group=None, array=False),
		))