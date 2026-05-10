from . import base_types
from .ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from .AssetClassDetailedSubProductType1Choice import AssetClassDetailedSubProductType1Choice

class Commodity2(base_types._BaseFieldType):

	__slots__ = ["_MktVal", "_CmmdtyTp"]
	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	@property
	def CmmdtyTp(self):
		return self._CmmdtyTp

	@CmmdtyTp.setter
	def CmmdtyTp(self, value):
		self._CmmdtyTp = value if type(value) != auto else self.make_default("CmmdtyTp")

	@CmmdtyTp.deleter
	def CmmdtyTp(self):
		del self._CmmdtyTp
		self._CmmdtyTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmmdtyTp', type=AssetClassDetailedSubProductType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

