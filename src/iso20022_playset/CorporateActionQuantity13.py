from . import base_types
from .FinancialInstrumentQuantity43Choice import FinancialInstrumentQuantity43Choice

class CorporateActionQuantity13(base_types._BaseFieldType):

	__slots__ = ["_IncrmtlDnmtn", "_BaseDnmtn"]
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
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if type(value) != auto else self.make_default("BaseDnmtn")

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncrmtlDnmtn', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseDnmtn', type=FinancialInstrumentQuantity43Choice, min=0, max=1, mutex_group=None, array=False),
	))

