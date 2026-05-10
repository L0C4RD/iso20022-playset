from . import base_types
from ._TotalAmountAndCurrency1 import TotalAmountAndCurrency1

class StandingOrderTotalAmount1(base_types._BaseFieldType):

	__slots__ = ["_SetStgOrdr", "_PdgPrdfndOrdr", "_PdgStgOrdr", "_SetPrdfndOrdr"]
	@property
	def PdgPrdfndOrdr(self):
		return self._PdgPrdfndOrdr

	@PdgPrdfndOrdr.setter
	def PdgPrdfndOrdr(self, value):
		self._PdgPrdfndOrdr = value if type(value) != base_types.auto else self.make_default("PdgPrdfndOrdr")

	@PdgPrdfndOrdr.deleter
	def PdgPrdfndOrdr(self):
		del self._PdgPrdfndOrdr
		self._PdgPrdfndOrdr = None

	@property
	def PdgStgOrdr(self):
		return self._PdgStgOrdr

	@PdgStgOrdr.setter
	def PdgStgOrdr(self, value):
		self._PdgStgOrdr = value if type(value) != base_types.auto else self.make_default("PdgStgOrdr")

	@PdgStgOrdr.deleter
	def PdgStgOrdr(self):
		del self._PdgStgOrdr
		self._PdgStgOrdr = None

	@property
	def SetPrdfndOrdr(self):
		return self._SetPrdfndOrdr

	@SetPrdfndOrdr.setter
	def SetPrdfndOrdr(self, value):
		self._SetPrdfndOrdr = value if type(value) != base_types.auto else self.make_default("SetPrdfndOrdr")

	@SetPrdfndOrdr.deleter
	def SetPrdfndOrdr(self):
		del self._SetPrdfndOrdr
		self._SetPrdfndOrdr = None

	@property
	def SetStgOrdr(self):
		return self._SetStgOrdr

	@SetStgOrdr.setter
	def SetStgOrdr(self, value):
		self._SetStgOrdr = value if type(value) != base_types.auto else self.make_default("SetStgOrdr")

	@SetStgOrdr.deleter
	def SetStgOrdr(self):
		del self._SetStgOrdr
		self._SetStgOrdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgPrdfndOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgStgOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SetPrdfndOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SetStgOrdr', type=TotalAmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
	))

