# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._MICIdentifier import MICIdentifier
from ._Number import Number
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice

class TradingParameters2(base_types._BaseFieldType):

	__slots__ = ["_MaxTraddNmnlQty", "_MinTraddNmnlQty", "_MinTradgPricgIncrmt", "_MktId", "_PmryPlcOfListgId", "_RndLot", "_ScndryPlcOfListg", "_TradLotSz"]
	@property
	def MaxTraddNmnlQty(self):
		return self._MaxTraddNmnlQty

	@MaxTraddNmnlQty.setter
	def MaxTraddNmnlQty(self, value):
		self._MaxTraddNmnlQty = value if type(value) != base_types.auto else self.make_default("MaxTraddNmnlQty")

	@MaxTraddNmnlQty.deleter
	def MaxTraddNmnlQty(self):
		del self._MaxTraddNmnlQty
		self._MaxTraddNmnlQty = None

	@property
	def MinTraddNmnlQty(self):
		return self._MinTraddNmnlQty

	@MinTraddNmnlQty.setter
	def MinTraddNmnlQty(self, value):
		self._MinTraddNmnlQty = value if type(value) != base_types.auto else self.make_default("MinTraddNmnlQty")

	@MinTraddNmnlQty.deleter
	def MinTraddNmnlQty(self):
		del self._MinTraddNmnlQty
		self._MinTraddNmnlQty = None

	@property
	def MinTradgPricgIncrmt(self):
		return self._MinTradgPricgIncrmt

	@MinTradgPricgIncrmt.setter
	def MinTradgPricgIncrmt(self, value):
		self._MinTradgPricgIncrmt = value if type(value) != base_types.auto else self.make_default("MinTradgPricgIncrmt")

	@MinTradgPricgIncrmt.deleter
	def MinTradgPricgIncrmt(self):
		del self._MinTradgPricgIncrmt
		self._MinTradgPricgIncrmt = None

	@property
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if type(value) != base_types.auto else self.make_default("MktId")

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = None

	@property
	def PmryPlcOfListgId(self):
		return self._PmryPlcOfListgId

	@PmryPlcOfListgId.setter
	def PmryPlcOfListgId(self, value):
		self._PmryPlcOfListgId = value if type(value) != base_types.auto else self.make_default("PmryPlcOfListgId")

	@PmryPlcOfListgId.deleter
	def PmryPlcOfListgId(self):
		del self._PmryPlcOfListgId
		self._PmryPlcOfListgId = None

	@property
	def RndLot(self):
		return self._RndLot

	@RndLot.setter
	def RndLot(self, value):
		self._RndLot = value if type(value) != base_types.auto else self.make_default("RndLot")

	@RndLot.deleter
	def RndLot(self):
		del self._RndLot
		self._RndLot = None

	@property
	def ScndryPlcOfListg(self):
		return self._ScndryPlcOfListg

	@ScndryPlcOfListg.setter
	def ScndryPlcOfListg(self, value):
		self._ScndryPlcOfListg = value if type(value) != base_types.auto else self.make_default("ScndryPlcOfListg")

	@ScndryPlcOfListg.deleter
	def ScndryPlcOfListg(self):
		del self._ScndryPlcOfListg
		self._ScndryPlcOfListg = None

	@property
	def TradLotSz(self):
		return self._TradLotSz

	@TradLotSz.setter
	def TradLotSz(self, value):
		self._TradLotSz = value if type(value) != base_types.auto else self.make_default("TradLotSz")

	@TradLotSz.deleter
	def TradLotSz(self):
		del self._TradLotSz
		self._TradLotSz = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxTraddNmnlQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinTraddNmnlQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinTradgPricgIncrmt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktId', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryPlcOfListgId', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndLot', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryPlcOfListg', type=MICIdentifier, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradLotSz', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
	))