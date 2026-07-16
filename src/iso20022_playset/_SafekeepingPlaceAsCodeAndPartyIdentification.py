# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification3
from . import SafekeepingPlace1Code

class SafekeepingPlaceAsCodeAndPartyIdentification(base_types._BaseFieldType):

	__slots__ = ["_Nrrtv", "_PlcSfkpg", "_Pty"]
	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if value is not None else base_types.UninitialisedField(self, 'Nrrtv', Max35Text, False)

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = base_types.UninitialisedField(self, 'Nrrtv', Max35Text, False)

	@property
	def PlcSfkpg(self):
		return self._PlcSfkpg

	@PlcSfkpg.setter
	def PlcSfkpg(self, value):
		self._PlcSfkpg = value if value is not None else base_types.UninitialisedField(self, 'PlcSfkpg', SafekeepingPlace1Code, False)

	@PlcSfkpg.deleter
	def PlcSfkpg(self):
		del self._PlcSfkpg
		self._PlcSfkpg = base_types.UninitialisedField(self, 'PlcSfkpg', SafekeepingPlace1Code, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyIdentification3, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyIdentification3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nrrtv', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcSfkpg', type=SafekeepingPlace1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification3, min=0, max=1, mutex_group=None, array=False),
	))