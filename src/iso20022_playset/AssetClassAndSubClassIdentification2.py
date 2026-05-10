from . import base_types
import NonEquityAssetClass1Code
import NonEquitySubClass1
import NonEquityInstrumentReportingClassification1Code

class AssetClassAndSubClassIdentification2(base_types._BaseFieldType):

	__slots__ = ["_DerivSubClss", "_FinInstrmClssfctn", "_AsstClss"]
	@property
	def DerivSubClss(self):
		return self._DerivSubClss

	@DerivSubClss.setter
	def DerivSubClss(self, value):
		self._DerivSubClss = value if type(value) != auto else self.make_default("DerivSubClss")

	@DerivSubClss.deleter
	def DerivSubClss(self):
		del self._DerivSubClss
		self._DerivSubClss = None

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if type(value) != auto else self.make_default("FinInstrmClssfctn")

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = None

	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if type(value) != auto else self.make_default("AsstClss")

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivSubClss', type=NonEquitySubClass1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=NonEquityInstrumentReportingClassification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstClss', type=NonEquityAssetClass1Code, min=1, max=1, mutex_group=None, array=False),
	))

