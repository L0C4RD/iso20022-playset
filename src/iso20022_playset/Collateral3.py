from . import base_types
from .CollateralType2Code import CollateralType2Code
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class Collateral3(base_types._BaseFieldType):

	__slots__ = ["_PstHrcutVal", "_MktVal", "_CollTp"]
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
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if type(value) != auto else self.make_default("CollTp")

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstHrcutVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTp', type=CollateralType2Code, min=1, max=1, mutex_group=None, array=False),
	))

