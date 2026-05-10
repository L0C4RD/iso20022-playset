from . import base_types
from .Max210Text import Max210Text
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class Result1(base_types._BaseFieldType):

	__slots__ = ["_DueToPtyA", "_DueToPtyB", "_AddtlInf"]
	@property
	def DueToPtyA(self):
		return self._DueToPtyA

	@DueToPtyA.setter
	def DueToPtyA(self, value):
		self._DueToPtyA = value if type(value) != auto else self.make_default("DueToPtyA")

	@DueToPtyA.deleter
	def DueToPtyA(self):
		del self._DueToPtyA
		self._DueToPtyA = None

	@property
	def DueToPtyB(self):
		return self._DueToPtyB

	@DueToPtyB.setter
	def DueToPtyB(self, value):
		self._DueToPtyB = value if type(value) != auto else self.make_default("DueToPtyB")

	@DueToPtyB.deleter
	def DueToPtyB(self):
		del self._DueToPtyB
		self._DueToPtyB = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DueToPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueToPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
	))

