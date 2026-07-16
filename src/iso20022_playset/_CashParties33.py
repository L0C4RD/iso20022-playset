# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount148

class CashParties33(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_Dbtr", "_DbtrAgt", "_Intrmy"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentificationAndAccount148, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentificationAndAccount148, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', PartyIdentificationAndAccount148, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', PartyIdentificationAndAccount148, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', PartyIdentificationAndAccount148, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', PartyIdentificationAndAccount148, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', PartyIdentificationAndAccount148, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', PartyIdentificationAndAccount148, False)

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if value is not None else base_types.UninitialisedField(self, 'Intrmy', PartyIdentificationAndAccount148, False)

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = base_types.UninitialisedField(self, 'Intrmy', PartyIdentificationAndAccount148, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount148, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount148, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentificationAndAccount148, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=PartyIdentificationAndAccount148, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=PartyIdentificationAndAccount148, min=0, max=1, mutex_group=None, array=False),
	))