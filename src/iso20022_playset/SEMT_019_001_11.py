from . import base_types
import SecuritiesSettlementTransactionAllegementReportV11

class SEMT_019_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmTxAllgmtRpt"]
		@property
		def SctiesSttlmTxAllgmtRpt(self):
			return self._SctiesSttlmTxAllgmtRpt

		@SctiesSttlmTxAllgmtRpt.setter
		def SctiesSttlmTxAllgmtRpt(self, value):
			self._SctiesSttlmTxAllgmtRpt = value if type(value) != auto else self.make_default("SctiesSttlmTxAllgmtRpt")

		@SctiesSttlmTxAllgmtRpt.deleter
		def SctiesSttlmTxAllgmtRpt(self):
			del self._SctiesSttlmTxAllgmtRpt
			self._SctiesSttlmTxAllgmtRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAllgmtRpt', type=SecuritiesSettlementTransactionAllegementReportV11, min=1, max=1, mutex_group=None, array=False),
		))

