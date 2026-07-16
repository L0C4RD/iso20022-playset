# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractModification9
from . import ContractType15
from . import TradeTransaction50

class CommonTradeDataReport72(base_types._BaseFieldType):

	__slots__ = ["_CtrctData", "_CtrctMod", "_TxData"]
	@property
	def CtrctData(self):
		return self._CtrctData

	@CtrctData.setter
	def CtrctData(self, value):
		self._CtrctData = value if value is not None else base_types.UninitialisedField(self, 'CtrctData', ContractType15, False)

	@CtrctData.deleter
	def CtrctData(self):
		del self._CtrctData
		self._CtrctData = base_types.UninitialisedField(self, 'CtrctData', ContractType15, False)

	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if value is not None else base_types.UninitialisedField(self, 'CtrctMod', ContractModification9, False)

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = base_types.UninitialisedField(self, 'CtrctMod', ContractModification9, False)

	@property
	def TxData(self):
		return self._TxData

	@TxData.setter
	def TxData(self, value):
		self._TxData = value if value is not None else base_types.UninitialisedField(self, 'TxData', TradeTransaction50, False)

	@TxData.deleter
	def TxData(self):
		del self._TxData
		self._TxData = base_types.UninitialisedField(self, 'TxData', TradeTransaction50, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctData', type=ContractType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMod', type=ContractModification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxData', type=TradeTransaction50, min=1, max=1, mutex_group=None, array=False),
	))