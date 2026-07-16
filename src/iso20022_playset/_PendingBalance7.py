# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementTypeAndIdentification25
from . import SignedQuantityFormat10

class PendingBalance7(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_PdgTxs"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat10, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat10, False)

	@property
	def PdgTxs(self):
		return self._PdgTxs

	@PdgTxs.setter
	def PdgTxs(self, value):
		self._PdgTxs = value if value is not None else base_types.UninitialisedField(self, 'PdgTxs', SettlementTypeAndIdentification25, True)

	@PdgTxs.deleter
	def PdgTxs(self):
		del self._PdgTxs
		self._PdgTxs = base_types.UninitialisedField(self, 'PdgTxs', SettlementTypeAndIdentification25, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgTxs', type=SettlementTypeAndIdentification25, min=0, max=None, mutex_group=None, array=True),
	))