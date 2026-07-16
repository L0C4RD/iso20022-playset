# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1Choice
from . import SubBalanceBreakdown1

class FinancialInstrumentAggregateBalance2(base_types._BaseFieldType):

	__slots__ = ["_BalBrkdwn", "_SttldBal", "_TraddBal"]
	@property
	def BalBrkdwn(self):
		return self._BalBrkdwn

	@BalBrkdwn.setter
	def BalBrkdwn(self, value):
		self._BalBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceBreakdown1, True)

	@BalBrkdwn.deleter
	def BalBrkdwn(self):
		del self._BalBrkdwn
		self._BalBrkdwn = base_types.UninitialisedField(self, 'BalBrkdwn', SubBalanceBreakdown1, True)

	@property
	def SttldBal(self):
		return self._SttldBal

	@SttldBal.setter
	def SttldBal(self, value):
		self._SttldBal = value if value is not None else base_types.UninitialisedField(self, 'SttldBal', FinancialInstrumentQuantity1Choice, False)

	@SttldBal.deleter
	def SttldBal(self):
		del self._SttldBal
		self._SttldBal = base_types.UninitialisedField(self, 'SttldBal', FinancialInstrumentQuantity1Choice, False)

	@property
	def TraddBal(self):
		return self._TraddBal

	@TraddBal.setter
	def TraddBal(self, value):
		self._TraddBal = value if value is not None else base_types.UninitialisedField(self, 'TraddBal', FinancialInstrumentQuantity1Choice, False)

	@TraddBal.deleter
	def TraddBal(self):
		del self._TraddBal
		self._TraddBal = base_types.UninitialisedField(self, 'TraddBal', FinancialInstrumentQuantity1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalBrkdwn', type=SubBalanceBreakdown1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttldBal', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TraddBal', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
	))