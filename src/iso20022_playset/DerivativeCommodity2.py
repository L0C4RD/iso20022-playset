from . import base_types
from .AssetClassTransactionType1Code import AssetClassTransactionType1Code
from .AssetClassCommodity3Choice import AssetClassCommodity3Choice
from .AssetPriceType1Code import AssetPriceType1Code

class DerivativeCommodity2(base_types._BaseFieldType):

	__slots__ = ["_TxTp", "_Pdct", "_FnlPricTp"]
	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if type(value) != auto else self.make_default("Pdct")

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = None

	@property
	def FnlPricTp(self):
		return self._FnlPricTp

	@FnlPricTp.setter
	def FnlPricTp(self, value):
		self._FnlPricTp = value if type(value) != auto else self.make_default("FnlPricTp")

	@FnlPricTp.deleter
	def FnlPricTp(self):
		del self._FnlPricTp
		self._FnlPricTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxTp', type=AssetClassTransactionType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdct', type=AssetClassCommodity3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlPricTp', type=AssetPriceType1Code, min=0, max=1, mutex_group=None, array=False),
	))

