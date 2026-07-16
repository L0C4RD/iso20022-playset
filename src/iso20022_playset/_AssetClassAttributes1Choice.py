# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassAttributes1
from . import DerivativeForeignExchange2
from . import DerivativeInterest2

class AssetClassAttributes1Choice(base_types._BaseFieldType):

	__slots__ = ["_Both", "_FX", "_Intrst"]
	@property
	def Both(self):
		return self._Both

	@Both.setter
	def Both(self, value):
		self._Both = value if value is not None else base_types.UninitialisedField(self, 'Both', AssetClassAttributes1, False)

	@Both.deleter
	def Both(self):
		del self._Both
		self._Both = base_types.UninitialisedField(self, 'Both', AssetClassAttributes1, False)

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if value is not None else base_types.UninitialisedField(self, 'FX', DerivativeForeignExchange2, False)

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = base_types.UninitialisedField(self, 'FX', DerivativeForeignExchange2, False)

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if value is not None else base_types.UninitialisedField(self, 'Intrst', DerivativeInterest2, False)

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = base_types.UninitialisedField(self, 'Intrst', DerivativeInterest2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Both', type=AssetClassAttributes1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FX', type=DerivativeForeignExchange2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intrst', type=DerivativeInterest2, min=0, max=1, mutex_group=1, array=False),
	))