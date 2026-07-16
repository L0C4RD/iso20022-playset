# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount231
from . import PartyIdentificationAndAccount232

class CashParties44(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_MktClmCtrPty"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentificationAndAccount231, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentificationAndAccount231, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', PartyIdentificationAndAccount232, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', PartyIdentificationAndAccount232, False)

	@property
	def MktClmCtrPty(self):
		return self._MktClmCtrPty

	@MktClmCtrPty.setter
	def MktClmCtrPty(self, value):
		self._MktClmCtrPty = value if value is not None else base_types.UninitialisedField(self, 'MktClmCtrPty', PartyIdentificationAndAccount231, False)

	@MktClmCtrPty.deleter
	def MktClmCtrPty(self):
		del self._MktClmCtrPty
		self._MktClmCtrPty = base_types.UninitialisedField(self, 'MktClmCtrPty', PartyIdentificationAndAccount231, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount231, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount232, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmCtrPty', type=PartyIdentificationAndAccount231, min=0, max=1, mutex_group=None, array=False),
	))