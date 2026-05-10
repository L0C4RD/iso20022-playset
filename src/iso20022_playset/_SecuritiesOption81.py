from . import base_types
from .FinancialInstrumentQuantity34Choice import FinancialInstrumentQuantity34Choice
from .FinancialInstrumentQuantity35Choice import FinancialInstrumentQuantity35Choice

class SecuritiesOption81(base_types._BaseFieldType):

	__slots__ = ["_NewDnmtnQty", "_FrntEndOddLotQty", "_MaxQtyToInst", "_MinQtyToInst", "_NewBrdLotQty", "_MinMltplQtyToInst", "_BckEndOddLotQty"]
	@property
	def NewDnmtnQty(self):
		return self._NewDnmtnQty

	@NewDnmtnQty.setter
	def NewDnmtnQty(self, value):
		self._NewDnmtnQty = value if type(value) != base_types.auto else self.make_default("NewDnmtnQty")

	@NewDnmtnQty.deleter
	def NewDnmtnQty(self):
		del self._NewDnmtnQty
		self._NewDnmtnQty = None

	@property
	def FrntEndOddLotQty(self):
		return self._FrntEndOddLotQty

	@FrntEndOddLotQty.setter
	def FrntEndOddLotQty(self, value):
		self._FrntEndOddLotQty = value if type(value) != base_types.auto else self.make_default("FrntEndOddLotQty")

	@FrntEndOddLotQty.deleter
	def FrntEndOddLotQty(self):
		del self._FrntEndOddLotQty
		self._FrntEndOddLotQty = None

	@property
	def MaxQtyToInst(self):
		return self._MaxQtyToInst

	@MaxQtyToInst.setter
	def MaxQtyToInst(self, value):
		self._MaxQtyToInst = value if type(value) != base_types.auto else self.make_default("MaxQtyToInst")

	@MaxQtyToInst.deleter
	def MaxQtyToInst(self):
		del self._MaxQtyToInst
		self._MaxQtyToInst = None

	@property
	def MinQtyToInst(self):
		return self._MinQtyToInst

	@MinQtyToInst.setter
	def MinQtyToInst(self, value):
		self._MinQtyToInst = value if type(value) != base_types.auto else self.make_default("MinQtyToInst")

	@MinQtyToInst.deleter
	def MinQtyToInst(self):
		del self._MinQtyToInst
		self._MinQtyToInst = None

	@property
	def NewBrdLotQty(self):
		return self._NewBrdLotQty

	@NewBrdLotQty.setter
	def NewBrdLotQty(self, value):
		self._NewBrdLotQty = value if type(value) != base_types.auto else self.make_default("NewBrdLotQty")

	@NewBrdLotQty.deleter
	def NewBrdLotQty(self):
		del self._NewBrdLotQty
		self._NewBrdLotQty = None

	@property
	def MinMltplQtyToInst(self):
		return self._MinMltplQtyToInst

	@MinMltplQtyToInst.setter
	def MinMltplQtyToInst(self, value):
		self._MinMltplQtyToInst = value if type(value) != base_types.auto else self.make_default("MinMltplQtyToInst")

	@MinMltplQtyToInst.deleter
	def MinMltplQtyToInst(self):
		del self._MinMltplQtyToInst
		self._MinMltplQtyToInst = None

	@property
	def BckEndOddLotQty(self):
		return self._BckEndOddLotQty

	@BckEndOddLotQty.setter
	def BckEndOddLotQty(self, value):
		self._BckEndOddLotQty = value if type(value) != base_types.auto else self.make_default("BckEndOddLotQty")

	@BckEndOddLotQty.deleter
	def BckEndOddLotQty(self):
		del self._BckEndOddLotQty
		self._BckEndOddLotQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewDnmtnQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrntEndOddLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxQtyToInst', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtyToInst', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQtyToInst', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BckEndOddLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
	))

