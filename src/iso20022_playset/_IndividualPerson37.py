from . import base_types
from ._CitizenshipInformation2 import CitizenshipInformation2
from ._CivilStatus1Choice import CivilStatus1Choice
from ._CountryCode import CountryCode
from ._GDPRData1 import GDPRData1
from ._Gender1Code import Gender1Code
from ._ISODate import ISODate
from ._Max140Text import Max140Text
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._NamePrefix1Choice import NamePrefix1Choice
from ._PersonalInformation1 import PersonalInformation1
from ._PoliticallyExposedPerson1 import PoliticallyExposedPerson1
from ._PostalAddress21 import PostalAddress21

class IndividualPerson37(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_BizFctn", "_CityOfBirth", "_CtryOfBirth", "_Ctznsh", "_CvlSts", "_DthDt", "_EdctnLvl", "_EmplngCpny", "_FmlyInf", "_GDPRData", "_Gndr", "_GvnNm", "_MddlNm", "_Nm", "_NmPrfx", "_NmSfx", "_PltclyXpsdPrsn", "_Prfssn", "_PrvcOfBirth", "_PstlAdr"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if type(value) != base_types.auto else self.make_default("BirthDt")

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = None

	@property
	def BizFctn(self):
		return self._BizFctn

	@BizFctn.setter
	def BizFctn(self, value):
		self._BizFctn = value if type(value) != base_types.auto else self.make_default("BizFctn")

	@BizFctn.deleter
	def BizFctn(self):
		del self._BizFctn
		self._BizFctn = None

	@property
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if type(value) != base_types.auto else self.make_default("CityOfBirth")

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = None

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if type(value) != base_types.auto else self.make_default("CtryOfBirth")

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = None

	@property
	def Ctznsh(self):
		return self._Ctznsh

	@Ctznsh.setter
	def Ctznsh(self, value):
		self._Ctznsh = value if type(value) != base_types.auto else self.make_default("Ctznsh")

	@Ctznsh.deleter
	def Ctznsh(self):
		del self._Ctznsh
		self._Ctznsh = None

	@property
	def CvlSts(self):
		return self._CvlSts

	@CvlSts.setter
	def CvlSts(self, value):
		self._CvlSts = value if type(value) != base_types.auto else self.make_default("CvlSts")

	@CvlSts.deleter
	def CvlSts(self):
		del self._CvlSts
		self._CvlSts = None

	@property
	def DthDt(self):
		return self._DthDt

	@DthDt.setter
	def DthDt(self, value):
		self._DthDt = value if type(value) != base_types.auto else self.make_default("DthDt")

	@DthDt.deleter
	def DthDt(self):
		del self._DthDt
		self._DthDt = None

	@property
	def EdctnLvl(self):
		return self._EdctnLvl

	@EdctnLvl.setter
	def EdctnLvl(self, value):
		self._EdctnLvl = value if type(value) != base_types.auto else self.make_default("EdctnLvl")

	@EdctnLvl.deleter
	def EdctnLvl(self):
		del self._EdctnLvl
		self._EdctnLvl = None

	@property
	def EmplngCpny(self):
		return self._EmplngCpny

	@EmplngCpny.setter
	def EmplngCpny(self, value):
		self._EmplngCpny = value if type(value) != base_types.auto else self.make_default("EmplngCpny")

	@EmplngCpny.deleter
	def EmplngCpny(self):
		del self._EmplngCpny
		self._EmplngCpny = None

	@property
	def FmlyInf(self):
		return self._FmlyInf

	@FmlyInf.setter
	def FmlyInf(self, value):
		self._FmlyInf = value if type(value) != base_types.auto else self.make_default("FmlyInf")

	@FmlyInf.deleter
	def FmlyInf(self):
		del self._FmlyInf
		self._FmlyInf = None

	@property
	def GDPRData(self):
		return self._GDPRData

	@GDPRData.setter
	def GDPRData(self, value):
		self._GDPRData = value if type(value) != base_types.auto else self.make_default("GDPRData")

	@GDPRData.deleter
	def GDPRData(self):
		del self._GDPRData
		self._GDPRData = None

	@property
	def Gndr(self):
		return self._Gndr

	@Gndr.setter
	def Gndr(self, value):
		self._Gndr = value if type(value) != base_types.auto else self.make_default("Gndr")

	@Gndr.deleter
	def Gndr(self):
		del self._Gndr
		self._Gndr = None

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if type(value) != base_types.auto else self.make_default("GvnNm")

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = None

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if type(value) != base_types.auto else self.make_default("MddlNm")

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if type(value) != base_types.auto else self.make_default("NmPrfx")

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = None

	@property
	def NmSfx(self):
		return self._NmSfx

	@NmSfx.setter
	def NmSfx(self, value):
		self._NmSfx = value if type(value) != base_types.auto else self.make_default("NmSfx")

	@NmSfx.deleter
	def NmSfx(self):
		del self._NmSfx
		self._NmSfx = None

	@property
	def PltclyXpsdPrsn(self):
		return self._PltclyXpsdPrsn

	@PltclyXpsdPrsn.setter
	def PltclyXpsdPrsn(self, value):
		self._PltclyXpsdPrsn = value if type(value) != base_types.auto else self.make_default("PltclyXpsdPrsn")

	@PltclyXpsdPrsn.deleter
	def PltclyXpsdPrsn(self):
		del self._PltclyXpsdPrsn
		self._PltclyXpsdPrsn = None

	@property
	def Prfssn(self):
		return self._Prfssn

	@Prfssn.setter
	def Prfssn(self, value):
		self._Prfssn = value if type(value) != base_types.auto else self.make_default("Prfssn")

	@Prfssn.deleter
	def Prfssn(self):
		del self._Prfssn
		self._Prfssn = None

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if type(value) != base_types.auto else self.make_default("PrvcOfBirth")

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CityOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctznsh', type=CitizenshipInformation2, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='CvlSts', type=CivilStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EdctnLvl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngCpny', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FmlyInf', type=PersonalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GDPRData', type=GDPRData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Gndr', type=Gender1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmSfx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltclyXpsdPrsn', type=PoliticallyExposedPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfssn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvcOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress21, min=1, max=10, mutex_group=None, array=True),
	))

