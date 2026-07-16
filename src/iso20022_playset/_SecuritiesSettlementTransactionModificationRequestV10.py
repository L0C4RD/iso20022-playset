# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionDetails176
from . import UpdateType39Choice

class SecuritiesSettlementTransactionModificationRequestV10(base_types._BaseFieldType):

	__slots__ = ["_ModfdTxDtls", "_UpdTp"]
	@property
	def ModfdTxDtls(self):
		return self._ModfdTxDtls

	@ModfdTxDtls.setter
	def ModfdTxDtls(self, value):
		self._ModfdTxDtls = value if value is not None else base_types.UninitialisedField(self, 'ModfdTxDtls', TransactionDetails176, False)

	@ModfdTxDtls.deleter
	def ModfdTxDtls(self):
		del self._ModfdTxDtls
		self._ModfdTxDtls = base_types.UninitialisedField(self, 'ModfdTxDtls', TransactionDetails176, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType39Choice, True)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType39Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModfdTxDtls', type=TransactionDetails176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType39Choice, min=1, max=3, mutex_group=None, array=True),
	))