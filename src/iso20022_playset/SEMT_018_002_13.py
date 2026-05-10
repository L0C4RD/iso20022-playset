import base_types
import SecuritiesTransactionPendingReport002V13

class SEMT_018_002_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxPdgRpt"]
		@property
		def SctiesTxPdgRpt(self):
			return self._SctiesTxPdgRpt

		@SctiesTxPdgRpt.setter
		def SctiesTxPdgRpt(self, value):
			self._SctiesTxPdgRpt = value if type(value) != auto else self.make_default("SctiesTxPdgRpt")

		@SctiesTxPdgRpt.deleter
		def SctiesTxPdgRpt(self):
			del self._SctiesTxPdgRpt
			self._SctiesTxPdgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPdgRpt', type=SecuritiesTransactionPendingReport002V13, min=1, max=1, mutex_group=None, array=False),
		))

