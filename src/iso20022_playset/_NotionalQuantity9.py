# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LongFraction19DecimalNumber
from . import QuantityOrTerm1Choice
from . import UnitOfMeasure8Choice

class NotionalQuantity9(base_types._BaseFieldType):

	__slots__ = ["_Dtls", "_TtlQty", "_UnitOfMeasr"]
	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if value is not None else base_types.UninitialisedField(self, 'Dtls', QuantityOrTerm1Choice, False)

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = base_types.UninitialisedField(self, 'Dtls', QuantityOrTerm1Choice, False)

	@property
	def TtlQty(self):
		return self._TtlQty

	@TtlQty.setter
	def TtlQty(self, value):
		self._TtlQty = value if value is not None else base_types.UninitialisedField(self, 'TtlQty', LongFraction19DecimalNumber, False)

	@TtlQty.deleter
	def TtlQty(self):
		del self._TtlQty
		self._TtlQty = base_types.UninitialisedField(self, 'TtlQty', LongFraction19DecimalNumber, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure8Choice, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtls', type=QuantityOrTerm1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlQty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))