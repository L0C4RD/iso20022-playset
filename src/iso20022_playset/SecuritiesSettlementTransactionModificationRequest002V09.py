import base_types
import TransactionDetails159
import UpdateType38Choice

class SecuritiesSettlementTransactionModificationRequest002V09(base_types._BaseFieldType):

	__slots__ = ["_UpdTp", "_ModfdTxDtls"]
	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	@property
	def ModfdTxDtls(self):
		return self._ModfdTxDtls

	@ModfdTxDtls.setter
	def ModfdTxDtls(self, value):
		self._ModfdTxDtls = value if type(value) != auto else self.make_default("ModfdTxDtls")

	@ModfdTxDtls.deleter
	def ModfdTxDtls(self):
		del self._ModfdTxDtls
		self._ModfdTxDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UpdTp', type=UpdateType38Choice, min=1, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdTxDtls', type=TransactionDetails159, min=1, max=1, mutex_group=None, array=False),
	))

