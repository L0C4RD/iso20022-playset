# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionAllegementReportV12 import SecuritiesSettlementTransactionAllegementReportV12

class SEMT_019_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.019.001.12"
		_docname = "semt.019.001.12"

		__slots__ = ["_SctiesSttlmTxAllgmtRpt"]
		@property
		def SctiesSttlmTxAllgmtRpt(self):
			return self._SctiesSttlmTxAllgmtRpt

		@SctiesSttlmTxAllgmtRpt.setter
		def SctiesSttlmTxAllgmtRpt(self, value):
			self._SctiesSttlmTxAllgmtRpt = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAllgmtRpt")

		@SctiesSttlmTxAllgmtRpt.deleter
		def SctiesSttlmTxAllgmtRpt(self):
			del self._SctiesSttlmTxAllgmtRpt
			self._SctiesSttlmTxAllgmtRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtRpt', type=SecuritiesSettlementTransactionAllegementReportV12, min=1, max=1, mutex_group=None, array=False),
		))