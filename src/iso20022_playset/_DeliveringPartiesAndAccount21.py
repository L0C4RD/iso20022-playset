from . import base_types
from .Max35Text import Max35Text
from .PartyIdentificationAndAccount228 import PartyIdentificationAndAccount228
from .PartyIdentification255Choice import PartyIdentification255Choice

class DeliveringPartiesAndAccount21(base_types._BaseFieldType):

	__slots__ = ["_SctiesSttlmSys", "_Pty2", "_Pty1", "_Dpstry"]
	@property
	def SctiesSttlmSys(self):
		return self._SctiesSttlmSys

	@SctiesSttlmSys.setter
	def SctiesSttlmSys(self, value):
		self._SctiesSttlmSys = value if type(value) != base_types.auto else self.make_default("SctiesSttlmSys")

	@SctiesSttlmSys.deleter
	def SctiesSttlmSys(self):
		del self._SctiesSttlmSys
		self._SctiesSttlmSys = None

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
		base_types.FieldEntry(name='SctiesSttlmSys', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty2', type=PartyIdentificationAndAccount228, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty1', type=PartyIdentificationAndAccount228, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification255Choice, min=1, max=1, mutex_group=None, array=False),
	))

