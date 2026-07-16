# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import AssetFXSubProductType1Code

class DerivativeForeignExchange3(base_types._BaseFieldType):

	__slots__ = ["_FxTp", "_OthrNtnlCcy"]
	@property
	def FxTp(self):
		return self._FxTp

	@FxTp.setter
	def FxTp(self, value):
		self._FxTp = value if value is not None else base_types.UninitialisedField(self, 'FxTp', AssetFXSubProductType1Code, False)

	@FxTp.deleter
	def FxTp(self):
		del self._FxTp
		self._FxTp = base_types.UninitialisedField(self, 'FxTp', AssetFXSubProductType1Code, False)

	@property
	def OthrNtnlCcy(self):
		return self._OthrNtnlCcy

	@OthrNtnlCcy.setter
	def OthrNtnlCcy(self, value):
		self._OthrNtnlCcy = value if value is not None else base_types.UninitialisedField(self, 'OthrNtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@OthrNtnlCcy.deleter
	def OthrNtnlCcy(self):
		del self._OthrNtnlCcy
		self._OthrNtnlCcy = base_types.UninitialisedField(self, 'OthrNtnlCcy', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxTp', type=AssetFXSubProductType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNtnlCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))