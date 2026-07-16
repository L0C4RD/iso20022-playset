# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceRateOrAmount1Choice
from . import YieldedOrValueType1Choice

class Price3(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Val"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', YieldedOrValueType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', YieldedOrValueType1Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceRateOrAmount1Choice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceRateOrAmount1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=YieldedOrValueType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmount1Choice, min=1, max=1, mutex_group=None, array=False),
	))