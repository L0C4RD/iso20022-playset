# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionAuditTrailReportV07 import SecuritiesSettlementTransactionAuditTrailReportV07

class SEMT_022_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxAudtTrlRpt"]
		@property
		def SctiesSttlmTxAudtTrlRpt(self):
			return self._SctiesSttlmTxAudtTrlRpt

		@SctiesSttlmTxAudtTrlRpt.setter
		def SctiesSttlmTxAudtTrlRpt(self, value):
			self._SctiesSttlmTxAudtTrlRpt = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAudtTrlRpt")

		@SctiesSttlmTxAudtTrlRpt.deleter
		def SctiesSttlmTxAudtTrlRpt(self):
			del self._SctiesSttlmTxAudtTrlRpt
			self._SctiesSttlmTxAudtTrlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAudtTrlRpt', type=SecuritiesSettlementTransactionAuditTrailReportV07, min=1, max=1, mutex_group=None, array=False),
		))