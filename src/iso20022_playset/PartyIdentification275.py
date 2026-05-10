import base_types
import ISOYear
import CountryCode
import Ownership1
import InvestorType1Choice
import ActivityIndicator1Choice
import NameAndAddress17
import PartyIdentification198Choice
import Max256Text

class PartyIdentification275(base_types._BaseFieldType):

	__slots__ = ["_Id", "_CtryOfIncorprtn", "_EmailAdr", "_ActvtyInd", "_Ownrsh", "_YrOfIncorprtn", "_NmAndAdr", "_InvstrTp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def CtryOfIncorprtn(self):
		return self._CtryOfIncorprtn

	@CtryOfIncorprtn.setter
	def CtryOfIncorprtn(self, value):
		self._CtryOfIncorprtn = value if type(value) != auto else self.make_default("CtryOfIncorprtn")

	@CtryOfIncorprtn.deleter
	def CtryOfIncorprtn(self):
		del self._CtryOfIncorprtn
		self._CtryOfIncorprtn = None

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def Ownrsh(self):
		return self._Ownrsh

	@Ownrsh.setter
	def Ownrsh(self, value):
		self._Ownrsh = value if type(value) != auto else self.make_default("Ownrsh")

	@Ownrsh.deleter
	def Ownrsh(self):
		del self._Ownrsh
		self._Ownrsh = None

	@property
	def YrOfIncorprtn(self):
		return self._YrOfIncorprtn

	@YrOfIncorprtn.setter
	def YrOfIncorprtn(self, value):
		self._YrOfIncorprtn = value if type(value) != auto else self.make_default("YrOfIncorprtn")

	@YrOfIncorprtn.deleter
	def YrOfIncorprtn(self):
		del self._YrOfIncorprtn
		self._YrOfIncorprtn = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def InvstrTp(self):
		return self._InvstrTp

	@InvstrTp.setter
	def InvstrTp(self, value):
		self._InvstrTp = value if type(value) != auto else self.make_default("InvstrTp")

	@InvstrTp.deleter
	def InvstrTp(self):
		del self._InvstrTp
		self._InvstrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification198Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncorprtn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=ActivityIndicator1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ownrsh', type=Ownership1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YrOfIncorprtn', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

