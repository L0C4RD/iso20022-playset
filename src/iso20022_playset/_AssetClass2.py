# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativeCommodity2
from . import DerivativeForeignExchange3
from . import DerivativeInterest3

class AssetClass2(base_types._BaseFieldType):

	__slots__ = ["_Cmmdty", "_FX", "_Intrst"]
	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', DerivativeCommodity2, False)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', DerivativeCommodity2, False)

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if value is not None else base_types.UninitialisedField(self, 'FX', DerivativeForeignExchange3, False)

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = base_types.UninitialisedField(self, 'FX', DerivativeForeignExchange3, False)

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if value is not None else base_types.UninitialisedField(self, 'Intrst', DerivativeInterest3, False)

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = base_types.UninitialisedField(self, 'Intrst', DerivativeInterest3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmmdty', type=DerivativeCommodity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FX', type=DerivativeForeignExchange3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=DerivativeInterest3, min=0, max=1, mutex_group=None, array=False),
	))