import base_types
import PersonalInformation1
import CountryCode
import PoliticallyExposedPerson1
import Max35Text
import Gender1Code
import Max350Text
import ModificationScope39
import CivilStatus1Choice
import GDPRData1
import ISODate
import ModificationScope34
import NamePrefix1Choice
import Max140Text

class IndividualPerson38(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_GvnNm", "_EdctnLvl", "_EmplngCpny", "_Prfssn", "_PltclyXpsdPrsn", "_GDPRData", "_MddlNm", "_CityOfBirth", "_Gndr", "_BirthDt", "_ModfdPstlAdr", "_ModfdCtznsh", "_NmPrfx", "_BizFctn", "_FmlyInf", "_CtryOfBirth", "_NmSfx", "_CvlSts", "_PrvcOfBirth", "_DthDt"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if type(value) != auto else self.make_default("GvnNm")

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = None

	@property
	def EdctnLvl(self):
		return self._EdctnLvl

	@EdctnLvl.setter
	def EdctnLvl(self, value):
		self._EdctnLvl = value if type(value) != auto else self.make_default("EdctnLvl")

	@EdctnLvl.deleter
	def EdctnLvl(self):
		del self._EdctnLvl
		self._EdctnLvl = None

	@property
	def EmplngCpny(self):
		return self._EmplngCpny

	@EmplngCpny.setter
	def EmplngCpny(self, value):
		self._EmplngCpny = value if type(value) != auto else self.make_default("EmplngCpny")

	@EmplngCpny.deleter
	def EmplngCpny(self):
		del self._EmplngCpny
		self._EmplngCpny = None

	@property
	def Prfssn(self):
		return self._Prfssn

	@Prfssn.setter
	def Prfssn(self, value):
		self._Prfssn = value if type(value) != auto else self.make_default("Prfssn")

	@Prfssn.deleter
	def Prfssn(self):
		del self._Prfssn
		self._Prfssn = None

	@property
	def PltclyXpsdPrsn(self):
		return self._PltclyXpsdPrsn

	@PltclyXpsdPrsn.setter
	def PltclyXpsdPrsn(self, value):
		self._PltclyXpsdPrsn = value if type(value) != auto else self.make_default("PltclyXpsdPrsn")

	@PltclyXpsdPrsn.deleter
	def PltclyXpsdPrsn(self):
		del self._PltclyXpsdPrsn
		self._PltclyXpsdPrsn = None

	@property
	def GDPRData(self):
		return self._GDPRData

	@GDPRData.setter
	def GDPRData(self, value):
		self._GDPRData = value if type(value) != auto else self.make_default("GDPRData")

	@GDPRData.deleter
	def GDPRData(self):
		del self._GDPRData
		self._GDPRData = None

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if type(value) != auto else self.make_default("MddlNm")

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = None

	@property
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if type(value) != auto else self.make_default("CityOfBirth")

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = None

	@property
	def Gndr(self):
		return self._Gndr

	@Gndr.setter
	def Gndr(self, value):
		self._Gndr = value if type(value) != auto else self.make_default("Gndr")

	@Gndr.deleter
	def Gndr(self):
		del self._Gndr
		self._Gndr = None

	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if type(value) != auto else self.make_default("BirthDt")

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = None

	@property
	def ModfdPstlAdr(self):
		return self._ModfdPstlAdr

	@ModfdPstlAdr.setter
	def ModfdPstlAdr(self, value):
		self._ModfdPstlAdr = value if type(value) != auto else self.make_default("ModfdPstlAdr")

	@ModfdPstlAdr.deleter
	def ModfdPstlAdr(self):
		del self._ModfdPstlAdr
		self._ModfdPstlAdr = None

	@property
	def ModfdCtznsh(self):
		return self._ModfdCtznsh

	@ModfdCtznsh.setter
	def ModfdCtznsh(self, value):
		self._ModfdCtznsh = value if type(value) != auto else self.make_default("ModfdCtznsh")

	@ModfdCtznsh.deleter
	def ModfdCtznsh(self):
		del self._ModfdCtznsh
		self._ModfdCtznsh = None

	@property
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if type(value) != auto else self.make_default("NmPrfx")

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = None

	@property
	def BizFctn(self):
		return self._BizFctn

	@BizFctn.setter
	def BizFctn(self, value):
		self._BizFctn = value if type(value) != auto else self.make_default("BizFctn")

	@BizFctn.deleter
	def BizFctn(self):
		del self._BizFctn
		self._BizFctn = None

	@property
	def FmlyInf(self):
		return self._FmlyInf

	@FmlyInf.setter
	def FmlyInf(self, value):
		self._FmlyInf = value if type(value) != auto else self.make_default("FmlyInf")

	@FmlyInf.deleter
	def FmlyInf(self):
		del self._FmlyInf
		self._FmlyInf = None

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if type(value) != auto else self.make_default("CtryOfBirth")

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = None

	@property
	def NmSfx(self):
		return self._NmSfx

	@NmSfx.setter
	def NmSfx(self, value):
		self._NmSfx = value if type(value) != auto else self.make_default("NmSfx")

	@NmSfx.deleter
	def NmSfx(self):
		del self._NmSfx
		self._NmSfx = None

	@property
	def CvlSts(self):
		return self._CvlSts

	@CvlSts.setter
	def CvlSts(self, value):
		self._CvlSts = value if type(value) != auto else self.make_default("CvlSts")

	@CvlSts.deleter
	def CvlSts(self):
		del self._CvlSts
		self._CvlSts = None

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if type(value) != auto else self.make_default("PrvcOfBirth")

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = None

	@property
	def DthDt(self):
		return self._DthDt

	@DthDt.setter
	def DthDt(self, value):
		self._DthDt = value if type(value) != auto else self.make_default("DthDt")

	@DthDt.deleter
	def DthDt(self):
		del self._DthDt
		self._DthDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EdctnLvl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngCpny', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfssn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltclyXpsdPrsn', type=PoliticallyExposedPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GDPRData', type=GDPRData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CityOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Gndr', type=Gender1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdPstlAdr', type=ModificationScope34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdCtznsh', type=ModificationScope39, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FmlyInf', type=PersonalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmSfx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvlSts', type=CivilStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvcOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

