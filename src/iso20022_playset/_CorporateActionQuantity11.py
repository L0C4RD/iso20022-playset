# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity34Choice
from . import FinancialInstrumentQuantity35Choice

class CorporateActionQuantity11(base_types._BaseFieldType):

	__slots__ = ["_BaseDnmtn", "_IncrmtlDnmtn", "_MaxQty", "_MinQtySght", "_NewBrdLotQty", "_NewDnmtnQty"]
	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if value is not None else base_types.UninitialisedField(self, 'BaseDnmtn', FinancialInstrumentQuantity35Choice, False)

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = base_types.UninitialisedField(self, 'BaseDnmtn', FinancialInstrumentQuantity35Choice, False)

	@property
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if value is not None else base_types.UninitialisedField(self, 'IncrmtlDnmtn', FinancialInstrumentQuantity35Choice, False)

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = base_types.UninitialisedField(self, 'IncrmtlDnmtn', FinancialInstrumentQuantity35Choice, False)

	@property
	def MaxQty(self):
		return self._MaxQty

	@MaxQty.setter
	def MaxQty(self, value):
		self._MaxQty = value if value is not None else base_types.UninitialisedField(self, 'MaxQty', FinancialInstrumentQuantity34Choice, False)

	@MaxQty.deleter
	def MaxQty(self):
		del self._MaxQty
		self._MaxQty = base_types.UninitialisedField(self, 'MaxQty', FinancialInstrumentQuantity34Choice, False)

	@property
	def MinQtySght(self):
		return self._MinQtySght

	@MinQtySght.setter
	def MinQtySght(self, value):
		self._MinQtySght = value if value is not None else base_types.UninitialisedField(self, 'MinQtySght', FinancialInstrumentQuantity34Choice, False)

	@MinQtySght.deleter
	def MinQtySght(self):
		del self._MinQtySght
		self._MinQtySght = base_types.UninitialisedField(self, 'MinQtySght', FinancialInstrumentQuantity34Choice, False)

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
		base_types.FieldEntry(name='BaseDnmtn', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrmtlDnmtn', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxQty', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtySght', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
	))