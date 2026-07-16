# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivityIndicator1Choice
from . import CountryCode
from . import ISOYear
from . import InvestorType1Choice
from . import Max256Text
from . import NameAndAddress17
from . import Ownership1
from . import PartyIdentification198Choice

class PartyIdentification275(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_CtryOfIncorprtn", "_EmailAdr", "_Id", "_InvstrTp", "_NmAndAdr", "_Ownrsh", "_YrOfIncorprtn"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', ActivityIndicator1Choice, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', ActivityIndicator1Choice, False)

	@property
	def CtryOfIncorprtn(self):
		return self._CtryOfIncorprtn

	@CtryOfIncorprtn.setter
	def CtryOfIncorprtn(self, value):
		self._CtryOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIncorprtn', CountryCode, False)

	@CtryOfIncorprtn.deleter
	def CtryOfIncorprtn(self):
		del self._CtryOfIncorprtn
		self._CtryOfIncorprtn = base_types.UninitialisedField(self, 'CtryOfIncorprtn', CountryCode, False)

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
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification198Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification198Choice, False)

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
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress17, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress17, False)

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

	@property
	def YrOfIncorprtn(self):
		return self._YrOfIncorprtn

	@YrOfIncorprtn.setter
	def YrOfIncorprtn(self, value):
		self._YrOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'YrOfIncorprtn', ISOYear, False)

	@YrOfIncorprtn.deleter
	def YrOfIncorprtn(self):
		del self._YrOfIncorprtn
		self._YrOfIncorprtn = base_types.UninitialisedField(self, 'YrOfIncorprtn', ISOYear, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=ActivityIndicator1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncorprtn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification198Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ownrsh', type=Ownership1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YrOfIncorprtn', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
	))