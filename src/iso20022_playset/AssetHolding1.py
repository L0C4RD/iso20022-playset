import base_types
import CollateralAccountType3Code
import ActiveCurrencyAnd24Amount
import AssetHolding1Choice

class AssetHolding1(base_types._BaseFieldType):

	__slots__ = ["_CollRqrmnt", "_PstHrcutVal", "_AsstTp"]
	@property
	def CollRqrmnt(self):
		return self._CollRqrmnt

	@CollRqrmnt.setter
	def CollRqrmnt(self, value):
		self._CollRqrmnt = value if type(value) != auto else self.make_default("CollRqrmnt")

	@CollRqrmnt.deleter
	def CollRqrmnt(self):
		del self._CollRqrmnt
		self._CollRqrmnt = None

	@property
	def PstHrcutVal(self):
		return self._PstHrcutVal

	@PstHrcutVal.setter
	def PstHrcutVal(self, value):
		self._PstHrcutVal = value if type(value) != auto else self.make_default("PstHrcutVal")

	@PstHrcutVal.deleter
	def PstHrcutVal(self):
		del self._PstHrcutVal
		self._PstHrcutVal = None

	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollRqrmnt', type=CollateralAccountType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstHrcutVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstTp', type=AssetHolding1Choice, min=1, max=1, mutex_group=None, array=False),
	))

