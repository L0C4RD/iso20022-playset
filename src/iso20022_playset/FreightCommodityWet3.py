import base_types
import AssetClassSubProductType32Code
import AssetClassDetailedSubProductType34Code
import AssetClassProductType4Code

class FreightCommodityWet3(base_types._BaseFieldType):

	__slots__ = ["_SubPdct", "_AddtlSubPdct", "_BasePdct"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubPdct', type=AssetClassSubProductType32Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSubPdct', type=AssetClassDetailedSubProductType34Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType4Code, min=1, max=1, mutex_group=None, array=False),
	))

