# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount96
from . import PartyIdentificationAndAccount97

class CashParties24(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_Intrmy", "_Intrmy2"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentificationAndAccount96, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentificationAndAccount96, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', PartyIdentificationAndAccount97, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', PartyIdentificationAndAccount97, False)

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if value is not None else base_types.UninitialisedField(self, 'Intrmy', PartyIdentificationAndAccount97, False)

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = base_types.UninitialisedField(self, 'Intrmy', PartyIdentificationAndAccount97, False)

	@property
	def Intrmy2(self):
		return self._Intrmy2

	@Intrmy2.setter
	def Intrmy2(self, value):
		self._Intrmy2 = value if value is not None else base_types.UninitialisedField(self, 'Intrmy2', PartyIdentificationAndAccount97, False)

	@Intrmy2.deleter
	def Intrmy2(self):
		del self._Intrmy2
		self._Intrmy2 = base_types.UninitialisedField(self, 'Intrmy2', PartyIdentificationAndAccount97, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount96, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount97, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=PartyIdentificationAndAccount97, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy2', type=PartyIdentificationAndAccount97, min=0, max=1, mutex_group=None, array=False),
	))