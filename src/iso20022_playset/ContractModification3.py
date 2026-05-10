import base_types
import TransactionOperationType6Code
import ModificationLevel1Code

class ContractModification3(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_Lvl"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if type(value) != auto else self.make_default("Lvl")

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lvl', type=ModificationLevel1Code, min=0, max=1, mutex_group=None, array=False),
	))

