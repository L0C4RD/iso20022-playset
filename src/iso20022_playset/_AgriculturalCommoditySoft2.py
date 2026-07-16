# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassDetailedSubProductType2Code
from . import AssetClassProductType1Code
from . import AssetClassSubProductType2Code

class AgriculturalCommoditySoft2(base_types._BaseFieldType):

	__slots__ = ["_AddtlSubPdct", "_BasePdct", "_SubPdct"]
	@property
	def AddtlSubPdct(self):
		return self._AddtlSubPdct

	@AddtlSubPdct.setter
	def AddtlSubPdct(self, value):
		self._AddtlSubPdct = value if value is not None else base_types.UninitialisedField(self, 'AddtlSubPdct', AssetClassDetailedSubProductType2Code, False)

	@AddtlSubPdct.deleter
	def AddtlSubPdct(self):
		del self._AddtlSubPdct
		self._AddtlSubPdct = base_types.UninitialisedField(self, 'AddtlSubPdct', AssetClassDetailedSubProductType2Code, False)

	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if value is not None else base_types.UninitialisedField(self, 'BasePdct', AssetClassProductType1Code, False)

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = base_types.UninitialisedField(self, 'BasePdct', AssetClassProductType1Code, False)

	@property
	def SubPdct(self):
		return self._SubPdct

	@SubPdct.setter
	def SubPdct(self, value):
		self._SubPdct = value if value is not None else base_types.UninitialisedField(self, 'SubPdct', AssetClassSubProductType2Code, False)

	@SubPdct.deleter
	def SubPdct(self):
		del self._SubPdct
		self._SubPdct = base_types.UninitialisedField(self, 'SubPdct', AssetClassSubProductType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSubPdct', type=AssetClassDetailedSubProductType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubPdct', type=AssetClassSubProductType2Code, min=0, max=1, mutex_group=None, array=False),
	))