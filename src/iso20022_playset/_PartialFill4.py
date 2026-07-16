# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketIdentification97
from . import Price14
from . import Quantity6Choice
from . import QuantityOrAmount2Choice
from . import TradeDate7Choice

class PartialFill4(base_types._BaseFieldType):

	__slots__ = ["_ConfQty", "_DealPric", "_MtchIncrmtQty", "_OrgnlOrdrdQty", "_PlcOfTrad", "_PrevslyExctdQty", "_RmngQty", "_TradDt"]
	@property
	def ConfQty(self):
		return self._ConfQty

	@ConfQty.setter
	def ConfQty(self, value):
		self._ConfQty = value if value is not None else base_types.UninitialisedField(self, 'ConfQty', Quantity6Choice, False)

	@ConfQty.deleter
	def ConfQty(self):
		del self._ConfQty
		self._ConfQty = base_types.UninitialisedField(self, 'ConfQty', Quantity6Choice, False)

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if value is not None else base_types.UninitialisedField(self, 'DealPric', Price14, False)

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = base_types.UninitialisedField(self, 'DealPric', Price14, False)

	@property
	def MtchIncrmtQty(self):
		return self._MtchIncrmtQty

	@MtchIncrmtQty.setter
	def MtchIncrmtQty(self, value):
		self._MtchIncrmtQty = value if value is not None else base_types.UninitialisedField(self, 'MtchIncrmtQty', QuantityOrAmount2Choice, False)

	@MtchIncrmtQty.deleter
	def MtchIncrmtQty(self):
		del self._MtchIncrmtQty
		self._MtchIncrmtQty = base_types.UninitialisedField(self, 'MtchIncrmtQty', QuantityOrAmount2Choice, False)

	@property
	def OrgnlOrdrdQty(self):
		return self._OrgnlOrdrdQty

	@OrgnlOrdrdQty.setter
	def OrgnlOrdrdQty(self, value):
		self._OrgnlOrdrdQty = value if value is not None else base_types.UninitialisedField(self, 'OrgnlOrdrdQty', QuantityOrAmount2Choice, False)

	@OrgnlOrdrdQty.deleter
	def OrgnlOrdrdQty(self):
		del self._OrgnlOrdrdQty
		self._OrgnlOrdrdQty = base_types.UninitialisedField(self, 'OrgnlOrdrdQty', QuantityOrAmount2Choice, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification97, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification97, False)

	@property
	def PrevslyExctdQty(self):
		return self._PrevslyExctdQty

	@PrevslyExctdQty.setter
	def PrevslyExctdQty(self, value):
		self._PrevslyExctdQty = value if value is not None else base_types.UninitialisedField(self, 'PrevslyExctdQty', QuantityOrAmount2Choice, False)

	@PrevslyExctdQty.deleter
	def PrevslyExctdQty(self):
		del self._PrevslyExctdQty
		self._PrevslyExctdQty = base_types.UninitialisedField(self, 'PrevslyExctdQty', QuantityOrAmount2Choice, False)

	@property
	def RmngQty(self):
		return self._RmngQty

	@RmngQty.setter
	def RmngQty(self, value):
		self._RmngQty = value if value is not None else base_types.UninitialisedField(self, 'RmngQty', QuantityOrAmount2Choice, False)

	@RmngQty.deleter
	def RmngQty(self):
		del self._RmngQty
		self._RmngQty = base_types.UninitialisedField(self, 'RmngQty', QuantityOrAmount2Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate7Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfQty', type=Quantity6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIncrmtQty', type=QuantityOrAmount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlOrdrdQty', type=QuantityOrAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification97, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslyExctdQty', type=QuantityOrAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQty', type=QuantityOrAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate7Choice, min=0, max=1, mutex_group=None, array=False),
	))