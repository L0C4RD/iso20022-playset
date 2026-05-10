from . import base_types
from .SecuritiesBalanceAccountingReport002V11 import SecuritiesBalanceAccountingReport002V11

class SEMT_003_002_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesBalAcctgRpt"]
		@property
		def SctiesBalAcctgRpt(self):
			return self._SctiesBalAcctgRpt

		@SctiesBalAcctgRpt.setter
		def SctiesBalAcctgRpt(self, value):
			self._SctiesBalAcctgRpt = value if type(value) != base_types.auto else self.make_default("SctiesBalAcctgRpt")

		@SctiesBalAcctgRpt.deleter
		def SctiesBalAcctgRpt(self):
			del self._SctiesBalAcctgRpt
			self._SctiesBalAcctgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalAcctgRpt', type=SecuritiesBalanceAccountingReport002V11, min=1, max=1, mutex_group=None, array=False),
		))

