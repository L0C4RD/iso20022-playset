# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ImpliedCurrencyAndAmount
from . import Max70Text
from . import UnitOfMeasure6Code

class Product5(base_types._BaseFieldType):

	__slots__ = ["_AddtlPdctCd", "_AmtLmt", "_PdctCd", "_QtyLmt", "_UnitOfMeasr"]
	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if value is not None else base_types.UninitialisedField(self, 'AddtlPdctCd', Max70Text, False)

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = base_types.UninitialisedField(self, 'AddtlPdctCd', Max70Text, False)

	@property
	def AmtLmt(self):
		return self._AmtLmt

	@AmtLmt.setter
	def AmtLmt(self, value):
		self._AmtLmt = value if value is not None else base_types.UninitialisedField(self, 'AmtLmt', ImpliedCurrencyAndAmount, False)

	@AmtLmt.deleter
	def AmtLmt(self):
		del self._AmtLmt
		self._AmtLmt = base_types.UninitialisedField(self, 'AmtLmt', ImpliedCurrencyAndAmount, False)

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if value is not None else base_types.UninitialisedField(self, 'PdctCd', Max70Text, False)

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = base_types.UninitialisedField(self, 'PdctCd', Max70Text, False)

	@property
	def QtyLmt(self):
		return self._QtyLmt

	@QtyLmt.setter
	def QtyLmt(self, value):
		self._QtyLmt = value if value is not None else base_types.UninitialisedField(self, 'QtyLmt', DecimalNumber, False)

	@QtyLmt.deleter
	def QtyLmt(self):
		del self._QtyLmt
		self._QtyLmt = base_types.UninitialisedField(self, 'QtyLmt', DecimalNumber, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure6Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure6Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlPdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtLmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyLmt', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure6Code, min=0, max=1, mutex_group=None, array=False),
	))