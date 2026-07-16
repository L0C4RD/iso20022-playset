# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionAuditTrailReport002V05

class SEMT_022_002_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.022.002.05"
		_docname = "semt.022.002.05"

		__slots__ = ["_SctiesSttlmTxAudtTrlRpt"]
		@property
		def SctiesSttlmTxAudtTrlRpt(self):
			return self._SctiesSttlmTxAudtTrlRpt

		@SctiesSttlmTxAudtTrlRpt.setter
		def SctiesSttlmTxAudtTrlRpt(self, value):
			self._SctiesSttlmTxAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxAudtTrlRpt', SecuritiesSettlementTransactionAuditTrailReport002V05, False)

		@SctiesSttlmTxAudtTrlRpt.deleter
		def SctiesSttlmTxAudtTrlRpt(self):
			del self._SctiesSttlmTxAudtTrlRpt
			self._SctiesSttlmTxAudtTrlRpt = base_types.UninitialisedField(self, 'SctiesSttlmTxAudtTrlRpt', SecuritiesSettlementTransactionAuditTrailReport002V05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAudtTrlRpt', type=SecuritiesSettlementTransactionAuditTrailReport002V05, min=1, max=1, mutex_group=None, array=False),
		))