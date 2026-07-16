# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalBankTransactionFamily1Code
from . import ExternalBankTransactionSubFamily1Code

class BankTransactionCodeStructure6(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_SubFmlyCd"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', ExternalBankTransactionFamily1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', ExternalBankTransactionFamily1Code, False)

	@property
	def SubFmlyCd(self):
		return self._SubFmlyCd

	@SubFmlyCd.setter
	def SubFmlyCd(self, value):
		self._SubFmlyCd = value if value is not None else base_types.UninitialisedField(self, 'SubFmlyCd', ExternalBankTransactionSubFamily1Code, False)

	@SubFmlyCd.deleter
	def SubFmlyCd(self):
		del self._SubFmlyCd
		self._SubFmlyCd = base_types.UninitialisedField(self, 'SubFmlyCd', ExternalBankTransactionSubFamily1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ExternalBankTransactionFamily1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubFmlyCd', type=ExternalBankTransactionSubFamily1Code, min=1, max=1, mutex_group=None, array=False),
	))