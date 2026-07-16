# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import PartyIdentification272

class IdentificationInformation5(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Agt", "_Pty"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if value is not None else base_types.UninitialisedField(self, 'Agt', BranchAndFinancialInstitutionIdentification8, False)

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = base_types.UninitialisedField(self, 'Agt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyIdentification272, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyIdentification272, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))