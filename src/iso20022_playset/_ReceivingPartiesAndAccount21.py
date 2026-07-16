# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification255Choice
from . import PartyIdentificationAndAccount228

class ReceivingPartiesAndAccount21(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_Pty1", "_Pty2", "_SctiesSttlmSys"]
	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', PartyIdentification255Choice, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', PartyIdentification255Choice, False)

	@property
	def Pty1(self):
		return self._Pty1

	@Pty1.setter
	def Pty1(self, value):
		self._Pty1 = value if value is not None else base_types.UninitialisedField(self, 'Pty1', PartyIdentificationAndAccount228, False)

	@Pty1.deleter
	def Pty1(self):
		del self._Pty1
		self._Pty1 = base_types.UninitialisedField(self, 'Pty1', PartyIdentificationAndAccount228, False)

	@property
	def Pty2(self):
		return self._Pty2

	@Pty2.setter
	def Pty2(self, value):
		self._Pty2 = value if value is not None else base_types.UninitialisedField(self, 'Pty2', PartyIdentificationAndAccount228, False)

	@Pty2.deleter
	def Pty2(self):
		del self._Pty2
		self._Pty2 = base_types.UninitialisedField(self, 'Pty2', PartyIdentificationAndAccount228, False)

	@property
	def SctiesSttlmSys(self):
		return self._SctiesSttlmSys

	@SctiesSttlmSys.setter
	def SctiesSttlmSys(self, value):
		self._SctiesSttlmSys = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmSys', Max35Text, False)

	@SctiesSttlmSys.deleter
	def SctiesSttlmSys(self):
		del self._SctiesSttlmSys
		self._SctiesSttlmSys = base_types.UninitialisedField(self, 'SctiesSttlmSys', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification255Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty1', type=PartyIdentificationAndAccount228, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty2', type=PartyIdentificationAndAccount228, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmSys', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))