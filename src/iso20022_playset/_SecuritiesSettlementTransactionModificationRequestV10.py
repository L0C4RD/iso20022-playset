from . import base_types
from ._UpdateType39Choice import UpdateType39Choice
from ._TransactionDetails176 import TransactionDetails176

class SecuritiesSettlementTransactionModificationRequestV10(base_types._BaseFieldType):

	__slots__ = ["_ModfdTxDtls", "_UpdTp"]
	@property
	def ModfdTxDtls(self):
		return self._ModfdTxDtls

	@ModfdTxDtls.setter
	def ModfdTxDtls(self, value):
		self._ModfdTxDtls = value if type(value) != base_types.auto else self.make_default("ModfdTxDtls")

	@ModfdTxDtls.deleter
	def ModfdTxDtls(self):
		del self._ModfdTxDtls
		self._ModfdTxDtls = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModfdTxDtls', type=TransactionDetails176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType39Choice, min=1, max=3, mutex_group=None, array=True),
	))

