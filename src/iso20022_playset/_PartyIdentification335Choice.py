# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification84Choice
from . import PartyIdentification336Choice

class PartyIdentification335Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Pty"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', AccountIdentification84Choice, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', AccountIdentification84Choice, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyIdentification336Choice, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyIdentification336Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=AccountIdentification84Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification336Choice, min=0, max=1, mutex_group=1, array=False),
	))