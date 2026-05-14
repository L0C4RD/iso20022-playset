# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification84Choice import AccountIdentification84Choice
from ._PartyIdentification336Choice import PartyIdentification336Choice

class PartyIdentification335Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Pty"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=AccountIdentification84Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification336Choice, min=0, max=1, mutex_group=1, array=False),
	))