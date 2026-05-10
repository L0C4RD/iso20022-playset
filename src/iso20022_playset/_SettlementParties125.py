from . import base_types
from ._PartyIdentificationAndAccount195 import PartyIdentificationAndAccount195
from ._PartyIdentification314 import PartyIdentification314

class SettlementParties125(base_types._BaseFieldType):

	__slots__ = ["_Pty3", "_Pty2", "_Pty5", "_Pty4", "_Pty1", "_Dpstry"]
	@property
	def Pty3(self):
		return self._Pty3

	@Pty3.setter
	def Pty3(self, value):
		self._Pty3 = value if type(value) != base_types.auto else self.make_default("Pty3")

	@Pty3.deleter
	def Pty3(self):
		del self._Pty3
		self._Pty3 = None

	@property
	def Pty2(self):
		return self._Pty2

	@Pty2.setter
	def Pty2(self, value):
		self._Pty2 = value if type(value) != base_types.auto else self.make_default("Pty2")

	@Pty2.deleter
	def Pty2(self):
		del self._Pty2
		self._Pty2 = None

	@property
	def Pty5(self):
		return self._Pty5

	@Pty5.setter
	def Pty5(self, value):
		self._Pty5 = value if type(value) != base_types.auto else self.make_default("Pty5")

	@Pty5.deleter
	def Pty5(self):
		del self._Pty5
		self._Pty5 = None

	@property
	def Pty4(self):
		return self._Pty4

	@Pty4.setter
	def Pty4(self, value):
		self._Pty4 = value if type(value) != base_types.auto else self.make_default("Pty4")

	@Pty4.deleter
	def Pty4(self):
		del self._Pty4
		self._Pty4 = None

	@property
	def Pty1(self):
		return self._Pty1

	@Pty1.setter
	def Pty1(self, value):
		self._Pty1 = value if type(value) != base_types.auto else self.make_default("Pty1")

	@Pty1.deleter
	def Pty1(self):
		del self._Pty1
		self._Pty1 = None

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != base_types.auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty3', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty2', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty5', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty4', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty1', type=PartyIdentificationAndAccount195, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification314, min=0, max=1, mutex_group=None, array=False),
	))

