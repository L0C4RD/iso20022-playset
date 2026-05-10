from . import base_types
from ._QuantityOrTerm1Choice import QuantityOrTerm1Choice
from ._LongFraction19DecimalNumber import LongFraction19DecimalNumber
from ._UnitOfMeasure8Choice import UnitOfMeasure8Choice

class NotionalQuantity9(base_types._BaseFieldType):

	__slots__ = ["_TtlQty", "_UnitOfMeasr", "_Dtls"]
	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if type(value) != base_types.auto else self.make_default("Dtls")

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = None

	@property
	def TtlQty(self):
		return self._TtlQty

	@TtlQty.setter
	def TtlQty(self, value):
		self._TtlQty = value if type(value) != base_types.auto else self.make_default("TtlQty")

	@TtlQty.deleter
	def TtlQty(self):
		del self._TtlQty
		self._TtlQty = None

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
		base_types.FieldEntry(name='Dtls', type=QuantityOrTerm1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlQty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))

