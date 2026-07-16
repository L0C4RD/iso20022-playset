# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionAllegementReport002V10

class SEMT_019_002_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.019.002.10"
		_docname = "semt.019.002.10"

		__slots__ = ["_SctiesSttlmTxAllgmtRpt"]
		@property
		def SctiesSttlmTxAllgmtRpt(self):
			return self._SctiesSttlmTxAllgmtRpt

		@SctiesSttlmTxAllgmtRpt.setter
		def SctiesSttlmTxAllgmtRpt(self, value):
			self._SctiesSttlmTxAllgmtRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtRpt', SecuritiesSettlementTransactionAllegementReport002V10, False)

		@SctiesSttlmTxAllgmtRpt.deleter
		def SctiesSttlmTxAllgmtRpt(self):
			del self._SctiesSttlmTxAllgmtRpt
			self._SctiesSttlmTxAllgmtRpt = base_types.UninitialisedField(self, 'SctiesSttlmTxAllgmtRpt', SecuritiesSettlementTransactionAllegementReport002V10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtRpt', type=SecuritiesSettlementTransactionAllegementReport002V10, min=1, max=1, mutex_group=None, array=False),
		))