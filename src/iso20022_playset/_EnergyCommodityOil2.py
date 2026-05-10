from . import base_types
from ._AssetClassSubProductType8Code import AssetClassSubProductType8Code
from ._AssetClassDetailedSubProductType32Code import AssetClassDetailedSubProductType32Code
from ._AssetClassProductType2Code import AssetClassProductType2Code

class EnergyCommodityOil2(base_types._BaseFieldType):

	__slots__ = ["_AddtlSubPdct", "_BasePdct", "_SubPdct"]
	@property
	def AddtlSubPdct(self):
		return self._AddtlSubPdct

	@AddtlSubPdct.setter
	def AddtlSubPdct(self, value):
		self._AddtlSubPdct = value if type(value) != base_types.auto else self.make_default("AddtlSubPdct")

	@AddtlSubPdct.deleter
	def AddtlSubPdct(self):
		del self._AddtlSubPdct
		self._AddtlSubPdct = None

	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if type(value) != base_types.auto else self.make_default("BasePdct")

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = None

	@property
	def SubPdct(self):
		return self._SubPdct

	@SubPdct.setter
	def SubPdct(self, value):
		self._SubPdct = value if type(value) != base_types.auto else self.make_default("SubPdct")

	@SubPdct.deleter
	def SubPdct(self):
		del self._SubPdct
		self._SubPdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSubPdct', type=AssetClassDetailedSubProductType32Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubPdct', type=AssetClassSubProductType8Code, min=1, max=1, mutex_group=None, array=False),
	))

