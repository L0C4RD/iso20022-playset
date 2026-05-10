from . import base_types
from ._ISODate import ISODate
from ._Max210Text import Max210Text
from ._MICEntityType1Code import MICEntityType1Code
from ._Modification1Code import Modification1Code
from ._MICIdentifier import MICIdentifier
from ._CountryCodeAndName3 import CountryCodeAndName3
from ._MarketIdentification1Code import MarketIdentification1Code
from ._Period4Choice import Period4Choice
from ._Max35Text import Max35Text
from ._Max450Text import Max450Text
from ._ISODateTime import ISODateTime

class MarketIdentification95(base_types._BaseFieldType):

	__slots__ = ["_StsDt", "_WebSite", "_CreDt", "_InstnNm", "_VldtyPrd", "_Sgmt", "_Ctgy", "_Ctry", "_Oprg", "_Acrnm", "_Mod", "_City", "_LastUpdtdDt", "_Tp", "_Note", "_AuthrtyNm"]
	@property
	def Acrnm(self):
		return self._Acrnm

	@Acrnm.setter
	def Acrnm(self, value):
		self._Acrnm = value if type(value) != base_types.auto else self.make_default("Acrnm")

	@Acrnm.deleter
	def Acrnm(self):
		del self._Acrnm
		self._Acrnm = None

	@property
	def AuthrtyNm(self):
		return self._AuthrtyNm

	@AuthrtyNm.setter
	def AuthrtyNm(self, value):
		self._AuthrtyNm = value if type(value) != base_types.auto else self.make_default("AuthrtyNm")

	@AuthrtyNm.deleter
	def AuthrtyNm(self):
		del self._AuthrtyNm
		self._AuthrtyNm = None

	@property
	def City(self):
		return self._City

	@City.setter
	def City(self, value):
		self._City = value if type(value) != base_types.auto else self.make_default("City")

	@City.deleter
	def City(self):
		del self._City
		self._City = None

	@property
	def CreDt(self):
		return self._CreDt

	@CreDt.setter
	def CreDt(self, value):
		self._CreDt = value if type(value) != base_types.auto else self.make_default("CreDt")

	@CreDt.deleter
	def CreDt(self):
		del self._CreDt
		self._CreDt = None

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != base_types.auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def InstnNm(self):
		return self._InstnNm

	@InstnNm.setter
	def InstnNm(self, value):
		self._InstnNm = value if type(value) != base_types.auto else self.make_default("InstnNm")

	@InstnNm.deleter
	def InstnNm(self):
		del self._InstnNm
		self._InstnNm = None

	@property
	def LastUpdtdDt(self):
		return self._LastUpdtdDt

	@LastUpdtdDt.setter
	def LastUpdtdDt(self, value):
		self._LastUpdtdDt = value if type(value) != base_types.auto else self.make_default("LastUpdtdDt")

	@LastUpdtdDt.deleter
	def LastUpdtdDt(self):
		del self._LastUpdtdDt
		self._LastUpdtdDt = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def Note(self):
		return self._Note

	@Note.setter
	def Note(self, value):
		self._Note = value if type(value) != base_types.auto else self.make_default("Note")

	@Note.deleter
	def Note(self):
		del self._Note
		self._Note = None

	@property
	def Oprg(self):
		return self._Oprg

	@Oprg.setter
	def Oprg(self, value):
		self._Oprg = value if type(value) != base_types.auto else self.make_default("Oprg")

	@Oprg.deleter
	def Oprg(self):
		del self._Oprg
		self._Oprg = None

	@property
	def Sgmt(self):
		return self._Sgmt

	@Sgmt.setter
	def Sgmt(self, value):
		self._Sgmt = value if type(value) != base_types.auto else self.make_default("Sgmt")

	@Sgmt.deleter
	def Sgmt(self):
		del self._Sgmt
		self._Sgmt = None

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if type(value) != base_types.auto else self.make_default("StsDt")

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	@property
	def WebSite(self):
		return self._WebSite

	@WebSite.setter
	def WebSite(self, value):
		self._WebSite = value if type(value) != base_types.auto else self.make_default("WebSite")

	@WebSite.deleter
	def WebSite(self):
		del self._WebSite
		self._WebSite = None

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

