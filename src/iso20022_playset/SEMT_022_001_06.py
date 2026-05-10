import base_types
import SecuritiesSettlementTransactionAuditTrailReportV06

class SEMT_022_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxAudtTrlRpt"]
		@property
		def SctiesSttlmTxAudtTrlRpt(self):
			return self._SctiesSttlmTxAudtTrlRpt

		@SctiesSttlmTxAudtTrlRpt.setter
		def SctiesSttlmTxAudtTrlRpt(self, value):
			self._SctiesSttlmTxAudtTrlRpt = value if type(value) != auto else self.make_default("SctiesSttlmTxAudtTrlRpt")

		@SctiesSttlmTxAudtTrlRpt.deleter
		def SctiesSttlmTxAudtTrlRpt(self):
			del self._SctiesSttlmTxAudtTrlRpt
			self._SctiesSttlmTxAudtTrlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAudtTrlRpt', type=SecuritiesSettlementTransactionAuditTrailReportV06, min=1, max=1, mutex_group=None, array=False),
		))

