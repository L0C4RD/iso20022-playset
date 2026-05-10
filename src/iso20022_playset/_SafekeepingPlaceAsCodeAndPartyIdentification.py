from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification3 import PartyIdentification3
from ._SafekeepingPlace1Code import SafekeepingPlace1Code

class SafekeepingPlaceAsCodeAndPartyIdentification(base_types._BaseFieldType):

	__slots__ = ["_Nrrtv", "_PlcSfkpg", "_Pty"]
	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if type(value) != base_types.auto else self.make_default("Nrrtv")

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = None

	@property
	def PlcSfkpg(self):
		return self._PlcSfkpg

	@PlcSfkpg.setter
	def PlcSfkpg(self, value):
		self._PlcSfkpg = value if type(value) != base_types.auto else self.make_default("PlcSfkpg")

	@PlcSfkpg.deleter
	def PlcSfkpg(self):
		del self._PlcSfkpg
		self._PlcSfkpg = None

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
		base_types.FieldEntry(name='Nrrtv', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcSfkpg', type=SafekeepingPlace1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification3, min=0, max=1, mutex_group=None, array=False),
	))

