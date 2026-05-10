from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class MarginCollateral1(base_types._BaseFieldType):

	__slots__ = ["_InTrnstToPtyB", "_HeldByPtyB", "_InTrnstToPtyA", "_PrrAgrdToPtyA", "_HeldByPtyA", "_PrrAgrdToPtyB"]
	@property
	def InTrnstToPtyB(self):
		return self._InTrnstToPtyB

	@InTrnstToPtyB.setter
	def InTrnstToPtyB(self, value):
		self._InTrnstToPtyB = value if type(value) != auto else self.make_default("InTrnstToPtyB")

	@InTrnstToPtyB.deleter
	def InTrnstToPtyB(self):
		del self._InTrnstToPtyB
		self._InTrnstToPtyB = None

	@property
	def HeldByPtyB(self):
		return self._HeldByPtyB

	@HeldByPtyB.setter
	def HeldByPtyB(self, value):
		self._HeldByPtyB = value if type(value) != auto else self.make_default("HeldByPtyB")

	@HeldByPtyB.deleter
	def HeldByPtyB(self):
		del self._HeldByPtyB
		self._HeldByPtyB = None

	@property
	def InTrnstToPtyA(self):
		return self._InTrnstToPtyA

	@InTrnstToPtyA.setter
	def InTrnstToPtyA(self, value):
		self._InTrnstToPtyA = value if type(value) != auto else self.make_default("InTrnstToPtyA")

	@InTrnstToPtyA.deleter
	def InTrnstToPtyA(self):
		del self._InTrnstToPtyA
		self._InTrnstToPtyA = None

	@property
	def PrrAgrdToPtyA(self):
		return self._PrrAgrdToPtyA

	@PrrAgrdToPtyA.setter
	def PrrAgrdToPtyA(self, value):
		self._PrrAgrdToPtyA = value if type(value) != auto else self.make_default("PrrAgrdToPtyA")

	@PrrAgrdToPtyA.deleter
	def PrrAgrdToPtyA(self):
		del self._PrrAgrdToPtyA
		self._PrrAgrdToPtyA = None

	@property
	def HeldByPtyA(self):
		return self._HeldByPtyA

	@HeldByPtyA.setter
	def HeldByPtyA(self, value):
		self._HeldByPtyA = value if type(value) != auto else self.make_default("HeldByPtyA")

	@HeldByPtyA.deleter
	def HeldByPtyA(self):
		del self._HeldByPtyA
		self._HeldByPtyA = None

	@property
	def PrrAgrdToPtyB(self):
		return self._PrrAgrdToPtyB

	@PrrAgrdToPtyB.setter
	def PrrAgrdToPtyB(self, value):
		self._PrrAgrdToPtyB = value if type(value) != auto else self.make_default("PrrAgrdToPtyB")

	@PrrAgrdToPtyB.deleter
	def PrrAgrdToPtyB(self):
		del self._PrrAgrdToPtyB
		self._PrrAgrdToPtyB = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InTrnstToPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HeldByPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InTrnstToPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrAgrdToPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HeldByPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrAgrdToPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

