# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NonEquityAssetClass1Code
from . import NonEquityInstrumentReportingClassification1Code
from . import NonEquitySubClass1

class AssetClassAndSubClassIdentification2(base_types._BaseFieldType):

	__slots__ = ["_AsstClss", "_DerivSubClss", "_FinInstrmClssfctn"]
	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if value is not None else base_types.UninitialisedField(self, 'AsstClss', NonEquityAssetClass1Code, False)

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = base_types.UninitialisedField(self, 'AsstClss', NonEquityAssetClass1Code, False)

	@property
	def DerivSubClss(self):
		return self._DerivSubClss

	@DerivSubClss.setter
	def DerivSubClss(self, value):
		self._DerivSubClss = value if value is not None else base_types.UninitialisedField(self, 'DerivSubClss', NonEquitySubClass1, False)

	@DerivSubClss.deleter
	def DerivSubClss(self):
		del self._DerivSubClss
		self._DerivSubClss = base_types.UninitialisedField(self, 'DerivSubClss', NonEquitySubClass1, False)

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmClssfctn', NonEquityInstrumentReportingClassification1Code, False)

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = base_types.UninitialisedField(self, 'FinInstrmClssfctn', NonEquityInstrumentReportingClassification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClss', type=NonEquityAssetClass1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivSubClss', type=NonEquitySubClass1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=NonEquityInstrumentReportingClassification1Code, min=0, max=1, mutex_group=None, array=False),
	))