from . import base_types
from .SubBalanceBreakdown1 import SubBalanceBreakdown1
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice

class FinancialInstrumentAggregateBalance2(base_types._BaseFieldType):

	__slots__ = ["_SttldBal", "_BalBrkdwn", "_TraddBal"]
	@property
	def SttldBal(self):
		return self._SttldBal

	@SttldBal.setter
	def SttldBal(self, value):
		self._SttldBal = value if type(value) != auto else self.make_default("SttldBal")

	@SttldBal.deleter
	def SttldBal(self):
		del self._SttldBal
		self._SttldBal = None

	@property
	def BalBrkdwn(self):
		return self._BalBrkdwn

	@BalBrkdwn.setter
	def BalBrkdwn(self, value):
		self._BalBrkdwn = value if type(value) != auto else self.make_default("BalBrkdwn")

	@BalBrkdwn.deleter
	def BalBrkdwn(self):
		del self._BalBrkdwn
		self._BalBrkdwn = None

	@property
	def TraddBal(self):
		return self._TraddBal

	@TraddBal.setter
	def TraddBal(self, value):
		self._TraddBal = value if type(value) != auto else self.make_default("TraddBal")

	@TraddBal.deleter
	def TraddBal(self):
		del self._TraddBal
		self._TraddBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttldBal', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceBreakdown1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TraddBal', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
	))

