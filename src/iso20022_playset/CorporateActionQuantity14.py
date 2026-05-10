import base_types
import FinancialInstrumentQuantity43Choice
import FinancialInstrumentQuantity44Choice

class CorporateActionQuantity14(base_types._BaseFieldType):

	__slots__ = ["_IncrmtlDnmtn", "_MaxQty", "_NewDnmtnQty", "_BaseDnmtn", "_MinQtySght", "_NewBrdLotQty"]
	@property
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if type(value) != auto else self.make_default("IncrmtlDnmtn")

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = None

	@property
	def MaxQty(self):
		return self._MaxQty

	@MaxQty.setter
	def MaxQty(self, value):
		self._MaxQty = value if type(value) != auto else self.make_default("MaxQty")

	@MaxQty.deleter
	def MaxQty(self):
		del self._MaxQty
		self._MaxQty = None

	@property
	def NewDnmtnQty(self):
		return self._NewDnmtnQty

	@NewDnmtnQty.setter
	def NewDnmtnQty(self, value):
		self._NewDnmtnQty = value if type(value) != auto else self.make_default("NewDnmtnQty")

	@NewDnmtnQty.deleter
	def NewDnmtnQty(self):
		del self._NewDnmtnQty
		self._NewDnmtnQty = None

	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if type(value) != auto else self.make_default("BaseDnmtn")

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = None

	@property
	def MinQtySght(self):
		return self._MinQtySght

	@MinQtySght.setter
	def MinQtySght(self, value):
		self._MinQtySght = value if type(value) != auto else self.make_default("MinQtySght")

	@MinQtySght.deleter
	def MinQtySght(self):
		del self._MinQtySght
		self._MinQtySght = None

	@property
	def NewBrdLotQty(self):
		return self._NewBrdLotQty

	@NewBrdLotQty.setter
	def NewBrdLotQty(self, value):
		self._NewBrdLotQty = value if type(value) != auto else self.make_default("NewBrdLotQty")

	@NewBrdLotQty.deleter
	def NewBrdLotQty(self):
		del self._NewBrdLotQty
		self._NewBrdLotQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncrmtlDnmtn', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxQty', type=FinancialInstrumentQuantity44Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnQty', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseDnmtn', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQtySght', type=FinancialInstrumentQuantity44Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotQty', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
	))

