# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CivilStatus1Choice
from . import CountryCode
from . import GDPRData1
from . import Gender1Code
from . import ISODate
from . import Max140Text
from . import Max350Text
from . import Max35Text
from . import ModificationScope34
from . import ModificationScope39
from . import NamePrefix1Choice
from . import PersonalInformation1
from . import PoliticallyExposedPerson1

class IndividualPerson38(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_BizFctn", "_CityOfBirth", "_CtryOfBirth", "_CvlSts", "_DthDt", "_EdctnLvl", "_EmplngCpny", "_FmlyInf", "_GDPRData", "_Gndr", "_GvnNm", "_MddlNm", "_ModfdCtznsh", "_ModfdPstlAdr", "_Nm", "_NmPrfx", "_NmSfx", "_PltclyXpsdPrsn", "_Prfssn", "_PrvcOfBirth"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if value is not None else base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@property
	def BizFctn(self):
		return self._BizFctn

	@BizFctn.setter
	def BizFctn(self, value):
		self._BizFctn = value if value is not None else base_types.UninitialisedField(self, 'BizFctn', Max35Text, False)

	@BizFctn.deleter
	def BizFctn(self):
		del self._BizFctn
		self._BizFctn = base_types.UninitialisedField(self, 'BizFctn', Max35Text, False)

	@property
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CityOfBirth', Max35Text, False)

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = base_types.UninitialisedField(self, 'CityOfBirth', Max35Text, False)

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBirth', CountryCode, False)

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = base_types.UninitialisedField(self, 'CtryOfBirth', CountryCode, False)

	@property
	def CvlSts(self):
		return self._CvlSts

	@CvlSts.setter
	def CvlSts(self, value):
		self._CvlSts = value if value is not None else base_types.UninitialisedField(self, 'CvlSts', CivilStatus1Choice, False)

	@CvlSts.deleter
	def CvlSts(self):
		del self._CvlSts
		self._CvlSts = base_types.UninitialisedField(self, 'CvlSts', CivilStatus1Choice, False)

	@property
	def DthDt(self):
		return self._DthDt

	@DthDt.setter
	def DthDt(self, value):
		self._DthDt = value if value is not None else base_types.UninitialisedField(self, 'DthDt', ISODate, False)

	@DthDt.deleter
	def DthDt(self):
		del self._DthDt
		self._DthDt = base_types.UninitialisedField(self, 'DthDt', ISODate, False)

	@property
	def EdctnLvl(self):
		return self._EdctnLvl

	@EdctnLvl.setter
	def EdctnLvl(self, value):
		self._EdctnLvl = value if value is not None else base_types.UninitialisedField(self, 'EdctnLvl', Max35Text, False)

	@EdctnLvl.deleter
	def EdctnLvl(self):
		del self._EdctnLvl
		self._EdctnLvl = base_types.UninitialisedField(self, 'EdctnLvl', Max35Text, False)

	@property
	def EmplngCpny(self):
		return self._EmplngCpny

	@EmplngCpny.setter
	def EmplngCpny(self, value):
		self._EmplngCpny = value if value is not None else base_types.UninitialisedField(self, 'EmplngCpny', Max140Text, False)

	@EmplngCpny.deleter
	def EmplngCpny(self):
		del self._EmplngCpny
		self._EmplngCpny = base_types.UninitialisedField(self, 'EmplngCpny', Max140Text, False)

	@property
	def FmlyInf(self):
		return self._FmlyInf

	@FmlyInf.setter
	def FmlyInf(self, value):
		self._FmlyInf = value if value is not None else base_types.UninitialisedField(self, 'FmlyInf', PersonalInformation1, False)

	@FmlyInf.deleter
	def FmlyInf(self):
		del self._FmlyInf
		self._FmlyInf = base_types.UninitialisedField(self, 'FmlyInf', PersonalInformation1, False)

	@property
	def GDPRData(self):
		return self._GDPRData

	@GDPRData.setter
	def GDPRData(self, value):
		self._GDPRData = value if value is not None else base_types.UninitialisedField(self, 'GDPRData', GDPRData1, True)

	@GDPRData.deleter
	def GDPRData(self):
		del self._GDPRData
		self._GDPRData = base_types.UninitialisedField(self, 'GDPRData', GDPRData1, True)

	@property
	def Gndr(self):
		return self._Gndr

	@Gndr.setter
	def Gndr(self, value):
		self._Gndr = value if value is not None else base_types.UninitialisedField(self, 'Gndr', Gender1Code, False)

	@Gndr.deleter
	def Gndr(self):
		del self._Gndr
		self._Gndr = base_types.UninitialisedField(self, 'Gndr', Gender1Code, False)

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if value is not None else base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if value is not None else base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@property
	def ModfdCtznsh(self):
		return self._ModfdCtznsh

	@ModfdCtznsh.setter
	def ModfdCtznsh(self, value):
		self._ModfdCtznsh = value if value is not None else base_types.UninitialisedField(self, 'ModfdCtznsh', ModificationScope39, True)

	@ModfdCtznsh.deleter
	def ModfdCtznsh(self):
		del self._ModfdCtznsh
		self._ModfdCtznsh = base_types.UninitialisedField(self, 'ModfdCtznsh', ModificationScope39, True)

	@property
	def ModfdPstlAdr(self):
		return self._ModfdPstlAdr

	@ModfdPstlAdr.setter
	def ModfdPstlAdr(self, value):
		self._ModfdPstlAdr = value if value is not None else base_types.UninitialisedField(self, 'ModfdPstlAdr', ModificationScope34, True)

	@ModfdPstlAdr.deleter
	def ModfdPstlAdr(self):
		del self._ModfdPstlAdr
		self._ModfdPstlAdr = base_types.UninitialisedField(self, 'ModfdPstlAdr', ModificationScope34, True)

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
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if value is not None else base_types.UninitialisedField(self, 'NmPrfx', NamePrefix1Choice, False)

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = base_types.UninitialisedField(self, 'NmPrfx', NamePrefix1Choice, False)

	@property
	def NmSfx(self):
		return self._NmSfx

	@NmSfx.setter
	def NmSfx(self, value):
		self._NmSfx = value if value is not None else base_types.UninitialisedField(self, 'NmSfx', Max35Text, False)

	@NmSfx.deleter
	def NmSfx(self):
		del self._NmSfx
		self._NmSfx = base_types.UninitialisedField(self, 'NmSfx', Max35Text, False)

	@property
	def PltclyXpsdPrsn(self):
		return self._PltclyXpsdPrsn

	@PltclyXpsdPrsn.setter
	def PltclyXpsdPrsn(self, value):
		self._PltclyXpsdPrsn = value if value is not None else base_types.UninitialisedField(self, 'PltclyXpsdPrsn', PoliticallyExposedPerson1, False)

	@PltclyXpsdPrsn.deleter
	def PltclyXpsdPrsn(self):
		del self._PltclyXpsdPrsn
		self._PltclyXpsdPrsn = base_types.UninitialisedField(self, 'PltclyXpsdPrsn', PoliticallyExposedPerson1, False)

	@property
	def Prfssn(self):
		return self._Prfssn

	@Prfssn.setter
	def Prfssn(self, value):
		self._Prfssn = value if value is not None else base_types.UninitialisedField(self, 'Prfssn', Max35Text, False)

	@Prfssn.deleter
	def Prfssn(self):
		del self._Prfssn
		self._Prfssn = base_types.UninitialisedField(self, 'Prfssn', Max35Text, False)

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'PrvcOfBirth', Max35Text, False)

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = base_types.UninitialisedField(self, 'PrvcOfBirth', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CityOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvlSts', type=CivilStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EdctnLvl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngCpny', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FmlyInf', type=PersonalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GDPRData', type=GDPRData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Gndr', type=Gender1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdCtznsh', type=ModificationScope39, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdPstlAdr', type=ModificationScope34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmSfx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltclyXpsdPrsn', type=PoliticallyExposedPerson1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prfssn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvcOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))