# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity34Choice
from . import FinancialInstrumentQuantity35Choice

class CorporateActionQuantity15(base_types._BaseFieldType):

	__slots__ = ["_BaseDnmtn", "_IncrmtlDnmtn", "_MaxQty", "_MinQtySght", "_NewBrdLotQty", "_NewDnmtnQty", "_NewOutsdngQty", "_SctyClldQty", "_TtlOutsdngQty"]
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

	@property
	def NewOutsdngQty(self):
		return self._NewOutsdngQty

	@NewOutsdngQty.setter
	def NewOutsdngQty(self, value):
		self._NewOutsdngQty = value if value is not None else base_types.UninitialisedField(self, 'NewOutsdngQty', FinancialInstrumentQuantity35Choice, False)

	@NewOutsdngQty.deleter
	def NewOutsdngQty(self):
		del self._NewOutsdngQty
		self._NewOutsdngQty = base_types.UninitialisedField(self, 'NewOutsdngQty', FinancialInstrumentQuantity35Choice, False)

	@property
	def SctyClldQty(self):
		return self._SctyClldQty

	@SctyClldQty.setter
	def SctyClldQty(self, value):
		self._SctyClldQty = value if value is not None else base_types.UninitialisedField(self, 'SctyClldQty', FinancialInstrumentQuantity35Choice, False)

	@SctyClldQty.deleter
	def SctyClldQty(self):
		del self._SctyClldQty
		self._SctyClldQty = base_types.UninitialisedField(self, 'SctyClldQty', FinancialInstrumentQuantity35Choice, False)

	@property
	def TtlOutsdngQty(self):
		return self._TtlOutsdngQty

	@TtlOutsdngQty.setter
	def TtlOutsdngQty(self, value):
		self._TtlOutsdngQty = value if value is not None else base_types.UninitialisedField(self, 'TtlOutsdngQty', FinancialInstrumentQuantity35Choice, False)

	@TtlOutsdngQty.deleter
	def TtlOutsdngQty(self):
		del self._TtlOutsdngQty
		self._TtlOutsdngQty = base_types.UninitialisedField(self, 'TtlOutsdngQty', FinancialInstrumentQuantity35Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseDnmtn', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrmtlDnmtn', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxQty', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtySght', type=FinancialInstrumentQuantity34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewOutsdngQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyClldQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOutsdngQty', type=FinancialInstrumentQuantity35Choice, min=0, max=1, mutex_group=None, array=False),
	))