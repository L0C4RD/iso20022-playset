# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1Choice
from . import SecurityIdentification19

class UnderlyingRatio2(base_types._BaseFieldType):

	__slots__ = ["_RltdFinInstrmId", "_UndrlygQtyDnmtr", "_UndrlygQtyNmrtr"]
	@property
	def RltdFinInstrmId(self):
		return self._RltdFinInstrmId

	@RltdFinInstrmId.setter
	def RltdFinInstrmId(self, value):
		self._RltdFinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'RltdFinInstrmId', SecurityIdentification19, True)

	@RltdFinInstrmId.deleter
	def RltdFinInstrmId(self):
		del self._RltdFinInstrmId
		self._RltdFinInstrmId = base_types.UninitialisedField(self, 'RltdFinInstrmId', SecurityIdentification19, True)

	@property
	def UndrlygQtyDnmtr(self):
		return self._UndrlygQtyDnmtr

	@UndrlygQtyDnmtr.setter
	def UndrlygQtyDnmtr(self, value):
		self._UndrlygQtyDnmtr = value if value is not None else base_types.UninitialisedField(self, 'UndrlygQtyDnmtr', FinancialInstrumentQuantity1Choice, False)

	@UndrlygQtyDnmtr.deleter
	def UndrlygQtyDnmtr(self):
		del self._UndrlygQtyDnmtr
		self._UndrlygQtyDnmtr = base_types.UninitialisedField(self, 'UndrlygQtyDnmtr', FinancialInstrumentQuantity1Choice, False)

	@property
	def UndrlygQtyNmrtr(self):
		return self._UndrlygQtyNmrtr

	@UndrlygQtyNmrtr.setter
	def UndrlygQtyNmrtr(self, value):
		self._UndrlygQtyNmrtr = value if value is not None else base_types.UninitialisedField(self, 'UndrlygQtyNmrtr', FinancialInstrumentQuantity1Choice, False)

	@UndrlygQtyNmrtr.deleter
	def UndrlygQtyNmrtr(self):
		del self._UndrlygQtyNmrtr
		self._UndrlygQtyNmrtr = base_types.UninitialisedField(self, 'UndrlygQtyNmrtr', FinancialInstrumentQuantity1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdFinInstrmId', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygQtyDnmtr', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygQtyNmrtr', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
	))