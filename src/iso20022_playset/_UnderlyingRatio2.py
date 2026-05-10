from . import base_types
from .SecurityIdentification19 import SecurityIdentification19
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice

class UnderlyingRatio2(base_types._BaseFieldType):

	__slots__ = ["_UndrlygQtyDnmtr", "_UndrlygQtyNmrtr", "_RltdFinInstrmId"]
	@property
	def UndrlygQtyDnmtr(self):
		return self._UndrlygQtyDnmtr

	@UndrlygQtyDnmtr.setter
	def UndrlygQtyDnmtr(self, value):
		self._UndrlygQtyDnmtr = value if type(value) != base_types.auto else self.make_default("UndrlygQtyDnmtr")

	@UndrlygQtyDnmtr.deleter
	def UndrlygQtyDnmtr(self):
		del self._UndrlygQtyDnmtr
		self._UndrlygQtyDnmtr = None

	@property
	def UndrlygQtyNmrtr(self):
		return self._UndrlygQtyNmrtr

	@UndrlygQtyNmrtr.setter
	def UndrlygQtyNmrtr(self, value):
		self._UndrlygQtyNmrtr = value if type(value) != base_types.auto else self.make_default("UndrlygQtyNmrtr")

	@UndrlygQtyNmrtr.deleter
	def UndrlygQtyNmrtr(self):
		del self._UndrlygQtyNmrtr
		self._UndrlygQtyNmrtr = None

	@property
	def RltdFinInstrmId(self):
		return self._RltdFinInstrmId

	@RltdFinInstrmId.setter
	def RltdFinInstrmId(self, value):
		self._RltdFinInstrmId = value if type(value) != base_types.auto else self.make_default("RltdFinInstrmId")

	@RltdFinInstrmId.deleter
	def RltdFinInstrmId(self):
		del self._RltdFinInstrmId
		self._RltdFinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygQtyDnmtr', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygQtyNmrtr', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdFinInstrmId', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
	))

