from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._UnderlyingContractForDifferenceType3Code import UnderlyingContractForDifferenceType3Code

class ContractForDifference2(base_types._BaseFieldType):

	__slots__ = ["_NtnlCcy2", "_UndrlygTp", "_NtnlCcy1"]
	@property
	def NtnlCcy1(self):
		return self._NtnlCcy1

	@NtnlCcy1.setter
	def NtnlCcy1(self, value):
		self._NtnlCcy1 = value if type(value) != base_types.auto else self.make_default("NtnlCcy1")

	@NtnlCcy1.deleter
	def NtnlCcy1(self):
		del self._NtnlCcy1
		self._NtnlCcy1 = None

	@property
	def NtnlCcy2(self):
		return self._NtnlCcy2

	@NtnlCcy2.setter
	def NtnlCcy2(self, value):
		self._NtnlCcy2 = value if type(value) != base_types.auto else self.make_default("NtnlCcy2")

	@NtnlCcy2.deleter
	def NtnlCcy2(self):
		del self._NtnlCcy2
		self._NtnlCcy2 = None

	@property
	def UndrlygTp(self):
		return self._UndrlygTp

	@UndrlygTp.setter
	def UndrlygTp(self, value):
		self._UndrlygTp = value if type(value) != base_types.auto else self.make_default("UndrlygTp")

	@UndrlygTp.deleter
	def UndrlygTp(self):
		del self._UndrlygTp
		self._UndrlygTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlCcy1', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcy2', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTp', type=UnderlyingContractForDifferenceType3Code, min=1, max=1, mutex_group=None, array=False),
	))

