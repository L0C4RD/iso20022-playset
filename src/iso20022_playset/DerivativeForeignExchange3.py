from . import base_types
import ActiveOrHistoricCurrencyCode
import AssetFXSubProductType1Code

class DerivativeForeignExchange3(base_types._BaseFieldType):

	__slots__ = ["_FxTp", "_OthrNtnlCcy"]
	@property
	def FxTp(self):
		return self._FxTp

	@FxTp.setter
	def FxTp(self, value):
		self._FxTp = value if type(value) != auto else self.make_default("FxTp")

	@FxTp.deleter
	def FxTp(self):
		del self._FxTp
		self._FxTp = None

	@property
	def OthrNtnlCcy(self):
		return self._OthrNtnlCcy

	@OthrNtnlCcy.setter
	def OthrNtnlCcy(self, value):
		self._OthrNtnlCcy = value if type(value) != auto else self.make_default("OthrNtnlCcy")

	@OthrNtnlCcy.deleter
	def OthrNtnlCcy(self):
		del self._OthrNtnlCcy
		self._OthrNtnlCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxTp', type=AssetFXSubProductType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNtnlCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

