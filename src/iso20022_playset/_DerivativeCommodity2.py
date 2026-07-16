# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassCommodity3Choice
from . import AssetClassTransactionType1Code
from . import AssetPriceType1Code

class DerivativeCommodity2(base_types._BaseFieldType):

	__slots__ = ["_FnlPricTp", "_Pdct", "_TxTp"]
	@property
	def FnlPricTp(self):
		return self._FnlPricTp

	@FnlPricTp.setter
	def FnlPricTp(self, value):
		self._FnlPricTp = value if value is not None else base_types.UninitialisedField(self, 'FnlPricTp', AssetPriceType1Code, False)

	@FnlPricTp.deleter
	def FnlPricTp(self):
		del self._FnlPricTp
		self._FnlPricTp = base_types.UninitialisedField(self, 'FnlPricTp', AssetPriceType1Code, False)

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if value is not None else base_types.UninitialisedField(self, 'Pdct', AssetClassCommodity3Choice, False)

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = base_types.UninitialisedField(self, 'Pdct', AssetClassCommodity3Choice, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', AssetClassTransactionType1Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', AssetClassTransactionType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FnlPricTp', type=AssetPriceType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdct', type=AssetClassCommodity3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=AssetClassTransactionType1Code, min=0, max=1, mutex_group=None, array=False),
	))