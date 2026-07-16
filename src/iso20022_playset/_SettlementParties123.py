# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification316
from . import PartyIdentificationAndAccount163

class SettlementParties123(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_Pty1", "_Pty2", "_Pty3"]
	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if value is not None else base_types.UninitialisedField(self, 'Dpstry', PartyIdentification316, False)

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = base_types.UninitialisedField(self, 'Dpstry', PartyIdentification316, False)

	@property
	def Pty1(self):
		return self._Pty1

	@Pty1.setter
	def Pty1(self, value):
		self._Pty1 = value if value is not None else base_types.UninitialisedField(self, 'Pty1', PartyIdentificationAndAccount163, False)

	@Pty1.deleter
	def Pty1(self):
		del self._Pty1
		self._Pty1 = base_types.UninitialisedField(self, 'Pty1', PartyIdentificationAndAccount163, False)

	@property
	def Pty2(self):
		return self._Pty2

	@Pty2.setter
	def Pty2(self, value):
		self._Pty2 = value if value is not None else base_types.UninitialisedField(self, 'Pty2', PartyIdentificationAndAccount163, False)

	@Pty2.deleter
	def Pty2(self):
		del self._Pty2
		self._Pty2 = base_types.UninitialisedField(self, 'Pty2', PartyIdentificationAndAccount163, False)

	@property
	def Pty3(self):
		return self._Pty3

	@Pty3.setter
	def Pty3(self, value):
		self._Pty3 = value if value is not None else base_types.UninitialisedField(self, 'Pty3', PartyIdentificationAndAccount163, False)

	@Pty3.deleter
	def Pty3(self):
		del self._Pty3
		self._Pty3 = base_types.UninitialisedField(self, 'Pty3', PartyIdentificationAndAccount163, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification316, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty1', type=PartyIdentificationAndAccount163, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty2', type=PartyIdentificationAndAccount163, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty3', type=PartyIdentificationAndAccount163, min=0, max=1, mutex_group=None, array=False),
	))