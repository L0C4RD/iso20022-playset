from . import base_types
from ._YesNoIndicator import YesNoIndicator
from ._FinancialInstrumentAggregateBalance2 import FinancialInstrumentAggregateBalance2

class FinancialInstrumentAggregateBalance1Choice(base_types._BaseFieldType):

	__slots__ = ["_HldgBal", "_HldgsInd"]
	@property
	def HldgBal(self):
		return self._HldgBal

	@HldgBal.setter
	def HldgBal(self, value):
		self._HldgBal = value if type(value) != base_types.auto else self.make_default("HldgBal")

	@HldgBal.deleter
	def HldgBal(self):
		del self._HldgBal
		self._HldgBal = None

	@property
	def HldgsInd(self):
		return self._HldgsInd

	@HldgsInd.setter
	def HldgsInd(self, value):
		self._HldgsInd = value if type(value) != base_types.auto else self.make_default("HldgsInd")

	@HldgsInd.deleter
	def HldgsInd(self):
		del self._HldgsInd
		self._HldgsInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldgBal', type=FinancialInstrumentAggregateBalance2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HldgsInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))

