# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAggregateBalance2
from . import YesNoIndicator

class FinancialInstrumentAggregateBalance1Choice(base_types._BaseFieldType):

	__slots__ = ["_HldgBal", "_HldgsInd"]
	@property
	def HldgBal(self):
		return self._HldgBal

	@HldgBal.setter
	def HldgBal(self, value):
		self._HldgBal = value if value is not None else base_types.UninitialisedField(self, 'HldgBal', FinancialInstrumentAggregateBalance2, False)

	@HldgBal.deleter
	def HldgBal(self):
		del self._HldgBal
		self._HldgBal = base_types.UninitialisedField(self, 'HldgBal', FinancialInstrumentAggregateBalance2, False)

	@property
	def HldgsInd(self):
		return self._HldgsInd

	@HldgsInd.setter
	def HldgsInd(self, value):
		self._HldgsInd = value if value is not None else base_types.UninitialisedField(self, 'HldgsInd', YesNoIndicator, False)

	@HldgsInd.deleter
	def HldgsInd(self):
		del self._HldgsInd
		self._HldgsInd = base_types.UninitialisedField(self, 'HldgsInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldgBal', type=FinancialInstrumentAggregateBalance2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HldgsInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))