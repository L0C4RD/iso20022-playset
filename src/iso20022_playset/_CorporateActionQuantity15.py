from . import base_types
from ._FinancialInstrumentQuantity34Choice import FinancialInstrumentQuantity34Choice
from ._FinancialInstrumentQuantity35Choice import FinancialInstrumentQuantity35Choice

class CorporateActionQuantity15(base_types._BaseFieldType):

	__slots__ = ["_BaseDnmtn", "_IncrmtlDnmtn", "_MaxQty", "_MinQtySght", "_NewBrdLotQty", "_NewDnmtnQty", "_NewOutsdngQty", "_SctyClldQty", "_TtlOutsdngQty"]
	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if type(value) != base_types.auto else self.make_default("BaseDnmtn")

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = None

	@property
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if type(value) != base_types.auto else self.make_default("IncrmtlDnmtn")

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = None

	@property
	def MaxQty(self):
		return self._MaxQty

	@MaxQty.setter
	def MaxQty(self, value):
		self._MaxQty = value if type(value) != base_types.auto else self.make_default("MaxQty")

	@MaxQty.deleter
	def MaxQty(self):
		del self._MaxQty
		self._MaxQty = None

	@property
	def MinQtySght(self):
		return self._MinQtySght

	@MinQtySght.setter
	def MinQtySght(self, value):
		self._MinQtySght = value if type(value) != base_types.auto else self.make_default("MinQtySght")

	@MinQtySght.deleter
	def MinQtySght(self):
		del self._MinQtySght
		self._MinQtySght = None

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
	def NewOutsdngQty(self):
		return self._NewOutsdngQty

	@NewOutsdngQty.setter
	def NewOutsdngQty(self, value):
		self._NewOutsdngQty = value if type(value) != base_types.auto else self.make_default("NewOutsdngQty")

	@NewOutsdngQty.deleter
	def NewOutsdngQty(self):
		del self._NewOutsdngQty
		self._NewOutsdngQty = None

	@property
	def SctyClldQty(self):
		return self._SctyClldQty

	@SctyClldQty.setter
	def SctyClldQty(self, value):
		self._SctyClldQty = value if type(value) != base_types.auto else self.make_default("SctyClldQty")

	@SctyClldQty.deleter
	def SctyClldQty(self):
		del self._SctyClldQty
		self._SctyClldQty = None

	@property
	def TtlOutsdngQty(self):
		return self._TtlOutsdngQty

	@TtlOutsdngQty.setter
	def TtlOutsdngQty(self, value):
		self._TtlOutsdngQty = value if type(value) != base_types.auto else self.make_default("TtlOutsdngQty")

	@TtlOutsdngQty.deleter
	def TtlOutsdngQty(self):
		del self._TtlOutsdngQty
		self._TtlOutsdngQty = None

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

