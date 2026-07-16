# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankTransactionCodeStructure6
from . import ExternalBankTransactionDomain1Code

class BankTransactionCodeStructure5(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Fmly"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', ExternalBankTransactionDomain1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', ExternalBankTransactionDomain1Code, False)

	@property
	def Fmly(self):
		return self._Fmly

	@Fmly.setter
	def Fmly(self, value):
		self._Fmly = value if value is not None else base_types.UninitialisedField(self, 'Fmly', BankTransactionCodeStructure6, False)

	@Fmly.deleter
	def Fmly(self):
		del self._Fmly
		self._Fmly = base_types.UninitialisedField(self, 'Fmly', BankTransactionCodeStructure6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ExternalBankTransactionDomain1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fmly', type=BankTransactionCodeStructure6, min=1, max=1, mutex_group=None, array=False),
	))