from . import base_types
from ._BalanceTransferFundingLimit1 import BalanceTransferFundingLimit1
from ._BalanceTransferReference1 import BalanceTransferReference1
from ._SettlementMethod7Choice import SettlementMethod7Choice

class BalanceTransfer7(base_types._BaseFieldType):

	__slots__ = ["_BalTrfFndgLmt", "_BalTrfMtd", "_BalTrfRef"]
	@property
	def BalTrfFndgLmt(self):
		return self._BalTrfFndgLmt

	@BalTrfFndgLmt.setter
	def BalTrfFndgLmt(self, value):
		self._BalTrfFndgLmt = value if type(value) != base_types.auto else self.make_default("BalTrfFndgLmt")

	@BalTrfFndgLmt.deleter
	def BalTrfFndgLmt(self):
		del self._BalTrfFndgLmt
		self._BalTrfFndgLmt = None

	@property
	def BalTrfMtd(self):
		return self._BalTrfMtd

	@BalTrfMtd.setter
	def BalTrfMtd(self, value):
		self._BalTrfMtd = value if type(value) != base_types.auto else self.make_default("BalTrfMtd")

	@BalTrfMtd.deleter
	def BalTrfMtd(self):
		del self._BalTrfMtd
		self._BalTrfMtd = None

	@property
	def BalTrfRef(self):
		return self._BalTrfRef

	@BalTrfRef.setter
	def BalTrfRef(self, value):
		self._BalTrfRef = value if type(value) != base_types.auto else self.make_default("BalTrfRef")

	@BalTrfRef.deleter
	def BalTrfRef(self):
		del self._BalTrfRef
		self._BalTrfRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTrfFndgLmt', type=BalanceTransferFundingLimit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrfMtd', type=SettlementMethod7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrfRef', type=BalanceTransferReference1, min=0, max=1, mutex_group=None, array=False),
	))

