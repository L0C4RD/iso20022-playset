# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DecimalNumber import DecimalNumber
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max70Text import Max70Text
from ._UnitOfMeasure6Code import UnitOfMeasure6Code

class Product5(base_types._BaseFieldType):

	__slots__ = ["_AddtlPdctCd", "_AmtLmt", "_PdctCd", "_QtyLmt", "_UnitOfMeasr"]
	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if type(value) != base_types.auto else self.make_default("AddtlPdctCd")

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = None

	@property
	def AmtLmt(self):
		return self._AmtLmt

	@AmtLmt.setter
	def AmtLmt(self, value):
		self._AmtLmt = value if type(value) != base_types.auto else self.make_default("AmtLmt")

	@AmtLmt.deleter
	def AmtLmt(self):
		del self._AmtLmt
		self._AmtLmt = None

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != base_types.auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

	@property
	def QtyLmt(self):
		return self._QtyLmt

	@QtyLmt.setter
	def QtyLmt(self, value):
		self._QtyLmt = value if type(value) != base_types.auto else self.make_default("QtyLmt")

	@QtyLmt.deleter
	def QtyLmt(self):
		del self._QtyLmt
		self._QtyLmt = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlPdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtLmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyLmt', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure6Code, min=0, max=1, mutex_group=None, array=False),
	))