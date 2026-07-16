# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ModificationLevel1Code
from . import TransactionOperationType10Code

class ContractModification9(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_Lvl"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType10Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType10Code, False)

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if value is not None else base_types.UninitialisedField(self, 'Lvl', ModificationLevel1Code, False)

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = base_types.UninitialisedField(self, 'Lvl', ModificationLevel1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lvl', type=ModificationLevel1Code, min=0, max=1, mutex_group=None, array=False),
	))