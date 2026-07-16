# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODate
from . import LEIIdentifier
from . import MICIdentifier
from . import Max350Text
from . import Max35Text
from . import OrganisationType1Choice
from . import PartyIdentification177Choice
from . import PostalAddress21

class Organisation39(base_types._BaseFieldType):

	__slots__ = ["_Id", "_LglNttyIdr", "_Nm", "_PlcOfListg", "_PstlAdr", "_Purp", "_RegnCtry", "_RegnDt", "_ShrtNm", "_TpOfOrg"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification177Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification177Choice, False)

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if value is not None else base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if value is not None else base_types.UninitialisedField(self, 'PlcOfListg', MICIdentifier, True)

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = base_types.UninitialisedField(self, 'PlcOfListg', MICIdentifier, True)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', PostalAddress21, True)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', PostalAddress21, True)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max35Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max35Text, False)

	@property
	def RegnCtry(self):
		return self._RegnCtry

	@RegnCtry.setter
	def RegnCtry(self, value):
		self._RegnCtry = value if value is not None else base_types.UninitialisedField(self, 'RegnCtry', CountryCode, False)

	@RegnCtry.deleter
	def RegnCtry(self):
		del self._RegnCtry
		self._RegnCtry = base_types.UninitialisedField(self, 'RegnCtry', CountryCode, False)

	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if value is not None else base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@property
	def TpOfOrg(self):
		return self._TpOfOrg

	@TpOfOrg.setter
	def TpOfOrg(self, value):
		self._TpOfOrg = value if value is not None else base_types.UninitialisedField(self, 'TpOfOrg', OrganisationType1Choice, False)

	@TpOfOrg.deleter
	def TpOfOrg(self):
		del self._TpOfOrg
		self._TpOfOrg = base_types.UninitialisedField(self, 'TpOfOrg', OrganisationType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MICIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress21, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Purp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfOrg', type=OrganisationType1Choice, min=0, max=1, mutex_group=None, array=False),
	))