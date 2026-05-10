from . import base_types
from .AssetClassSubProductType19Code import AssetClassSubProductType19Code

class ForeignExchangeDerivative2(base_types._BaseFieldType):

	__slots__ = ["_CtrctSubTp"]
	@property
	def CtrctSubTp(self):
		return self._CtrctSubTp

	@CtrctSubTp.setter
	def CtrctSubTp(self, value):
		self._CtrctSubTp = value if type(value) != auto else self.make_default("CtrctSubTp")

	@CtrctSubTp.deleter
	def CtrctSubTp(self):
		del self._CtrctSubTp
		self._CtrctSubTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctSubTp', type=AssetClassSubProductType19Code, min=1, max=1, mutex_group=None, array=False),
	))

