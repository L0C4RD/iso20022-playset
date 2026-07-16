# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import DateAndPlaceOfBirth2
from . import InvestorType1Choice
from . import Max256Text
from . import NaturalPersonIdentification1
from . import Ownership1
from . import PersonName3

class PartyIdentification217(base_types._BaseFieldType):

	__slots__ = ["_DtAndPlcOfBirth", "_EmailAdr", "_Id", "_InvstrTp", "_NmAndAdr", "_Ntlty", "_Ownrsh"]
	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth2, False)

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth2, False)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', NaturalPersonIdentification1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', NaturalPersonIdentification1, False)

	@property
	def InvstrTp(self):
		return self._InvstrTp

	@InvstrTp.setter
	def InvstrTp(self, value):
		self._InvstrTp = value if value is not None else base_types.UninitialisedField(self, 'InvstrTp', InvestorType1Choice, False)

	@InvstrTp.deleter
	def InvstrTp(self):
		del self._InvstrTp
		self._InvstrTp = base_types.UninitialisedField(self, 'InvstrTp', InvestorType1Choice, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', PersonName3, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', PersonName3, False)

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if value is not None else base_types.UninitialisedField(self, 'Ntlty', CountryCode, False)

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = base_types.UninitialisedField(self, 'Ntlty', CountryCode, False)

	@property
	def Ownrsh(self):
		return self._Ownrsh

	@Ownrsh.setter
	def Ownrsh(self, value):
		self._Ownrsh = value if value is not None else base_types.UninitialisedField(self, 'Ownrsh', Ownership1, False)

	@Ownrsh.deleter
	def Ownrsh(self):
		del self._Ownrsh
		self._Ownrsh = base_types.UninitialisedField(self, 'Ownrsh', Ownership1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=NaturalPersonIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PersonName3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ownrsh', type=Ownership1, min=0, max=1, mutex_group=None, array=False),
	))