# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionAllegementNotification002V10 import SecuritiesSettlementTransactionAllegementNotification002V10

class SESE_028_002_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxAllgmtNtfctn"]
		@property
		def SctiesSttlmTxAllgmtNtfctn(self):
			return self._SctiesSttlmTxAllgmtNtfctn

		@SctiesSttlmTxAllgmtNtfctn.setter
		def SctiesSttlmTxAllgmtNtfctn(self, value):
			self._SctiesSttlmTxAllgmtNtfctn = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAllgmtNtfctn")

		@SctiesSttlmTxAllgmtNtfctn.deleter
		def SctiesSttlmTxAllgmtNtfctn(self):
			del self._SctiesSttlmTxAllgmtNtfctn
			self._SctiesSttlmTxAllgmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtNtfctn', type=SecuritiesSettlementTransactionAllegementNotification002V10, min=1, max=1, mutex_group=None, array=False),
		))