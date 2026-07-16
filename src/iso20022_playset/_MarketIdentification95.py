# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCodeAndName3
from . import ISODate
from . import ISODateTime
from . import MICEntityType1Code
from . import MICIdentifier
from . import MarketIdentification1Code
from . import Max210Text
from . import Max35Text
from . import Max450Text
from . import Modification1Code
from . import Period4Choice

class MarketIdentification95(base_types._BaseFieldType):

	__slots__ = ["_Acrnm", "_AuthrtyNm", "_City", "_CreDt", "_Ctgy", "_Ctry", "_InstnNm", "_LastUpdtdDt", "_Mod", "_Note", "_Oprg", "_Sgmt", "_StsDt", "_Tp", "_VldtyPrd", "_WebSite"]
	@property
	def Acrnm(self):
		return self._Acrnm

	@Acrnm.setter
	def Acrnm(self, value):
		self._Acrnm = value if value is not None else base_types.UninitialisedField(self, 'Acrnm', Max35Text, False)

	@Acrnm.deleter
	def Acrnm(self):
		del self._Acrnm
		self._Acrnm = base_types.UninitialisedField(self, 'Acrnm', Max35Text, False)

	@property
	def AuthrtyNm(self):
		return self._AuthrtyNm

	@AuthrtyNm.setter
	def AuthrtyNm(self, value):
		self._AuthrtyNm = value if value is not None else base_types.UninitialisedField(self, 'AuthrtyNm', Max450Text, False)

	@AuthrtyNm.deleter
	def AuthrtyNm(self):
		del self._AuthrtyNm
		self._AuthrtyNm = base_types.UninitialisedField(self, 'AuthrtyNm', Max450Text, False)

	@property
	def City(self):
		return self._City

	@City.setter
	def City(self, value):
		self._City = value if value is not None else base_types.UninitialisedField(self, 'City', Max35Text, False)

	@City.deleter
	def City(self):
		del self._City
		self._City = base_types.UninitialisedField(self, 'City', Max35Text, False)

	@property
	def CreDt(self):
		return self._CreDt

	@CreDt.setter
	def CreDt(self, value):
		self._CreDt = value if value is not None else base_types.UninitialisedField(self, 'CreDt', ISODate, False)

	@CreDt.deleter
	def CreDt(self):
		del self._CreDt
		self._CreDt = base_types.UninitialisedField(self, 'CreDt', ISODate, False)

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', MICEntityType1Code, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', MICEntityType1Code, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCodeAndName3, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCodeAndName3, False)

	@property
	def InstnNm(self):
		return self._InstnNm

	@InstnNm.setter
	def InstnNm(self, value):
		self._InstnNm = value if value is not None else base_types.UninitialisedField(self, 'InstnNm', Max450Text, False)

	@InstnNm.deleter
	def InstnNm(self):
		del self._InstnNm
		self._InstnNm = base_types.UninitialisedField(self, 'InstnNm', Max450Text, False)

	@property
	def LastUpdtdDt(self):
		return self._LastUpdtdDt

	@LastUpdtdDt.setter
	def LastUpdtdDt(self, value):
		self._LastUpdtdDt = value if value is not None else base_types.UninitialisedField(self, 'LastUpdtdDt', ISODateTime, False)

	@LastUpdtdDt.deleter
	def LastUpdtdDt(self):
		del self._LastUpdtdDt
		self._LastUpdtdDt = base_types.UninitialisedField(self, 'LastUpdtdDt', ISODateTime, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', Modification1Code, False)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', Modification1Code, False)

	@property
	def Note(self):
		return self._Note

	@Note.setter
	def Note(self, value):
		self._Note = value if value is not None else base_types.UninitialisedField(self, 'Note', Max450Text, False)

	@Note.deleter
	def Note(self):
		del self._Note
		self._Note = base_types.UninitialisedField(self, 'Note', Max450Text, False)

	@property
	def Oprg(self):
		return self._Oprg

	@Oprg.setter
	def Oprg(self, value):
		self._Oprg = value if value is not None else base_types.UninitialisedField(self, 'Oprg', MICIdentifier, False)

	@Oprg.deleter
	def Oprg(self):
		del self._Oprg
		self._Oprg = base_types.UninitialisedField(self, 'Oprg', MICIdentifier, False)

	@property
	def Sgmt(self):
		return self._Sgmt

	@Sgmt.setter
	def Sgmt(self, value):
		self._Sgmt = value if value is not None else base_types.UninitialisedField(self, 'Sgmt', MICIdentifier, False)

	@Sgmt.deleter
	def Sgmt(self):
		del self._Sgmt
		self._Sgmt = base_types.UninitialisedField(self, 'Sgmt', MICIdentifier, False)

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if value is not None else base_types.UninitialisedField(self, 'StsDt', ISODate, False)

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = base_types.UninitialisedField(self, 'StsDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MarketIdentification1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MarketIdentification1Code, False)

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', Period4Choice, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', Period4Choice, False)

	@property
	def WebSite(self):
		return self._WebSite

	@WebSite.setter
	def WebSite(self, value):
		self._WebSite = value if value is not None else base_types.UninitialisedField(self, 'WebSite', Max210Text, False)

	@WebSite.deleter
	def WebSite(self):
		del self._WebSite
		self._WebSite = base_types.UninitialisedField(self, 'WebSite', Max210Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acrnm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrtyNm', type=Max450Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='City', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=MICEntityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCodeAndName3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstnNm', type=Max450Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpdtdDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Note', type=Max450Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oprg', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgmt', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MarketIdentification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WebSite', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
	))