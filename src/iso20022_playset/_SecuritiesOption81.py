# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity34Choice
from . import FinancialInstrumentQuantity35Choice

class SecuritiesOption81(base_types._BaseFieldType):

	__slots__ = ["_BckEndOddLotQty", "_FrntEndOddLotQty", "_MaxQtyToInst", "_MinMltplQtyToInst", "_MinQtyToInst", "_NewBrdLotQty", "_NewDnmtnQty"]
	@property
	def BckEndOddLotQty(self):
		return self._BckEndOddLotQty

	@BckEndOddLotQty.setter
	def BckEndOddLotQty(self, value):
		self._BckEndOddLotQty = value if value is not None else base_types.UninitialisedField(self, 'BckEndOddLotQty', FinancialInstrumentQuantity35Choice, False)

	@BckEndOddLotQty.deleter
	def BckEndOddLotQty(self):
		del self._BckEndOddLotQty
		self._BckEndOddLotQty = base_types.UninitialisedField(self, 'BckEndOddLotQty', FinancialInstrumentQuantity35Choice, False)

	@property
	def FrntEndOddLotQty(self):
		return self._FrntEndOddLotQty

	@FrntEndOddLotQty.setter
	def FrntEndOddLotQty(self, value):
		self._FrntEndOddLotQty = value if value is not None else base_types.UninitialisedField(self, 'FrntEndOddLotQty', FinancialInstrumentQuantity35Choice, False)

	@FrntEndOddLotQty.deleter
	def FrntEndOddLotQty(self):
		del self._FrntEndOddLotQty
		self._FrntEndOddLotQty = base_types.UninitialisedField(self, 'FrntEndOddLotQty', FinancialInstrumentQuantity35Choice, False)

	@property
	def MaxQtyToInst(self):
		return self._MaxQtyToInst

	@MaxQtyToInst.setter
	def MaxQtyToInst(self, value):
		self._MaxQtyToInst = value if value is not None else base_types.UninitialisedField(self, 'MaxQtyToInst', FinancialInstrumentQuantity34Choice, False)

	@MaxQtyToInst.deleter
	def MaxQtyToInst(self):
		del self._MaxQtyToInst
		self._MaxQtyToInst = base_types.UninitialisedField(self, 'MaxQtyToInst', FinancialInstrumentQuantity34Choice, False)

	@property
	def MinMltplQtyToInst(self):
		return self._MinMltplQtyToInst

	@MinMltplQtyToInst.setter
	def MinMltplQtyToInst(self, value):
		self._MinMltplQtyToInst = value if value is not None else base_types.UninitialisedField(self, 'MinMltplQtyToInst', FinancialInstrumentQuantity35Choice, False)

	@MinMltplQtyToInst.deleter
	def MinMltplQtyToInst(self):
		del self._MinMltplQtyToInst
		self._MinMltplQtyToInst = base_types.UninitialisedField(self, 'MinMltplQtyToInst', FinancialInstrumentQuantity35Choice, False)

	@property
	def MinQtyToInst(self):
		return self._MinQtyToInst

	@MinQtyToInst.setter
	def MinQtyToInst(self, value):
		self._MinQtyToInst = value if value is not None else base_types.UninitialisedField(self, 'MinQtyToInst', FinancialInstrumentQuantity34Choice, False)

	@MinQtyToInst.deleter
	def MinQtyToInst(self):
		del self._MinQtyToInst
		self._MinQtyToInst = base_types.UninitialisedField(self, 'MinQtyToInst', FinancialInstrumentQuantity34Choice, False)

	@property
	def NewBrdLotQty(self):
		return self._NewBrdLotQty

	@NewBrdLotQty.setter
	def NewBrdLotQty(self, value):
		self._NewBrdLotQty = value if value is not None else base_types.UninitialisedField(self, 'NewBrdLotQty', FinancialInstrumentQuantity35Choice, False)

	@NewBrdLotQty.deleter
	def NewBrdLotQty(self):
		del self._NewBrdLotQty
		self._NewBrdLotQty = base_types.UninitialisedField(self, 'NewBrdLotQty', FinancialInstrumentQuantity35Choice, False)

	@property
	def NewDnmtnQty(self):
		return self._NewDnmtnQty

	@NewDnmtnQty.setter
	def NewDnmtnQty(self, value):
		self._NewDnmtnQty = value if value is not None else base_types.UninitialisedField(self, 'NewDnmtnQty', FinancialInstrumentQuantity35Choice, False)

	@NewDnmtnQty.deleter
	def NewDnmtnQty(self):
		del self._NewDnmtnQty
		self._NewDnmtnQty = base_types.UninitialisedField(self, 'NewDnmtnQty', FinancialInstrumentQuantity35Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BckEndOddLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrntEndOddLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxQtyToInst', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQtyToInst', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtyToInst', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
	))