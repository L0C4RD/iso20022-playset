from . import base_types
from .Price14 import Price14
from .QuantityOrAmount2Choice import QuantityOrAmount2Choice
from .MarketIdentification97 import MarketIdentification97
from .TradeDate7Choice import TradeDate7Choice
from .Quantity6Choice import Quantity6Choice

class PartialFill4(base_types._BaseFieldType):

	__slots__ = ["_OrgnlOrdrdQty", "_ConfQty", "_RmngQty", "_PlcOfTrad", "_DealPric", "_TradDt", "_MtchIncrmtQty", "_PrevslyExctdQty"]
	@property
	def OrgnlOrdrdQty(self):
		return self._OrgnlOrdrdQty

	@OrgnlOrdrdQty.setter
	def OrgnlOrdrdQty(self, value):
		self._OrgnlOrdrdQty = value if type(value) != auto else self.make_default("OrgnlOrdrdQty")

	@OrgnlOrdrdQty.deleter
	def OrgnlOrdrdQty(self):
		del self._OrgnlOrdrdQty
		self._OrgnlOrdrdQty = None

	@property
	def ConfQty(self):
		return self._ConfQty

	@ConfQty.setter
	def ConfQty(self, value):
		self._ConfQty = value if type(value) != auto else self.make_default("ConfQty")

	@ConfQty.deleter
	def ConfQty(self):
		del self._ConfQty
		self._ConfQty = None

	@property
	def RmngQty(self):
		return self._RmngQty

	@RmngQty.setter
	def RmngQty(self, value):
		self._RmngQty = value if type(value) != auto else self.make_default("RmngQty")

	@RmngQty.deleter
	def RmngQty(self):
		del self._RmngQty
		self._RmngQty = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def MtchIncrmtQty(self):
		return self._MtchIncrmtQty

	@MtchIncrmtQty.setter
	def MtchIncrmtQty(self, value):
		self._MtchIncrmtQty = value if type(value) != auto else self.make_default("MtchIncrmtQty")

	@MtchIncrmtQty.deleter
	def MtchIncrmtQty(self):
		del self._MtchIncrmtQty
		self._MtchIncrmtQty = None

	@property
	def PrevslyExctdQty(self):
		return self._PrevslyExctdQty

	@PrevslyExctdQty.setter
	def PrevslyExctdQty(self, value):
		self._PrevslyExctdQty = value if type(value) != auto else self.make_default("PrevslyExctdQty")

	@PrevslyExctdQty.deleter
	def PrevslyExctdQty(self):
		del self._PrevslyExctdQty
		self._PrevslyExctdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlOrdrdQty', type=QuantityOrAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfQty', type=Quantity6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQty', type=QuantityOrAmount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification97, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIncrmtQty', type=QuantityOrAmount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslyExctdQty', type=QuantityOrAmount2Choice, min=1, max=1, mutex_group=None, array=False),
	))

