from . import base_types
import AssetClassSubProductType7Code
import AssetClassDetailedSubProductType31Code
import AssetClassProductType2Code

class EnergyCommodityNaturalGas2(base_types._BaseFieldType):

	__slots__ = ["_BasePdct", "_SubPdct", "_AddtlSubPdct"]
	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if type(value) != auto else self.make_default("BasePdct")

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = None

	@property
	def SubPdct(self):
		return self._SubPdct

	@SubPdct.setter
	def SubPdct(self, value):
		self._SubPdct = value if type(value) != auto else self.make_default("SubPdct")

	@SubPdct.deleter
	def SubPdct(self):
		del self._SubPdct
		self._SubPdct = None

	@property
	def AddtlSubPdct(self):
		return self._AddtlSubPdct

	@AddtlSubPdct.setter
	def AddtlSubPdct(self, value):
		self._AddtlSubPdct = value if type(value) != auto else self.make_default("AddtlSubPdct")

	@AddtlSubPdct.deleter
	def AddtlSubPdct(self):
		del self._AddtlSubPdct
		self._AddtlSubPdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubPdct', type=AssetClassSubProductType7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSubPdct', type=AssetClassDetailedSubProductType31Code, min=1, max=1, mutex_group=None, array=False),
	))

