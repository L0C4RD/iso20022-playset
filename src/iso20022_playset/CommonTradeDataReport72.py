from . import base_types
import TradeTransaction50
import ContractType15
import ContractModification9

class CommonTradeDataReport72(base_types._BaseFieldType):

	__slots__ = ["_CtrctMod", "_TxData", "_CtrctData"]
	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if type(value) != auto else self.make_default("CtrctMod")

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = None

	@property
	def TxData(self):
		return self._TxData

	@TxData.setter
	def TxData(self, value):
		self._TxData = value if type(value) != auto else self.make_default("TxData")

	@TxData.deleter
	def TxData(self):
		del self._TxData
		self._TxData = None

	@property
	def CtrctData(self):
		return self._CtrctData

	@CtrctData.setter
	def CtrctData(self, value):
		self._CtrctData = value if type(value) != auto else self.make_default("CtrctData")

	@CtrctData.deleter
	def CtrctData(self):
		del self._CtrctData
		self._CtrctData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctMod', type=ContractModification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxData', type=TradeTransaction50, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctData', type=ContractType15, min=0, max=1, mutex_group=None, array=False),
	))

