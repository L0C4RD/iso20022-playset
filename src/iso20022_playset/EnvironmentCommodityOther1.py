import base_types
import AssetClassSubProductType49Code
import AssetClassProductType3Code

class EnvironmentCommodityOther1(base_types._BaseFieldType):

	__slots__ = ["_BasePdct", "_SubPdct"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubPdct', type=AssetClassSubProductType49Code, min=1, max=1, mutex_group=None, array=False),
	))

