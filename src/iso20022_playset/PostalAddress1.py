from . import base_types
from .Max70Text import Max70Text
from .Max16Text import Max16Text
from .CountryCode import CountryCode
from .AddressType2Code import AddressType2Code
from .Max35Text import Max35Text

class PostalAddress1(base_types._BaseFieldType):

	__slots__ = ["_AdrTp", "_AdrLine", "_TwnNm", "_CtrySubDvsn", "_PstCd", "_BldgNb", "_Ctry", "_StrtNm"]
	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if type(value) != base_types.auto else self.make_default("AdrTp")

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = None

	@property
	def AdrLine(self):
		return self._AdrLine

	@AdrLine.setter
	def AdrLine(self, value):
		self._AdrLine = value if type(value) != base_types.auto else self.make_default("AdrLine")

	@AdrLine.deleter
	def AdrLine(self):
		del self._AdrLine
		self._AdrLine = None

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if type(value) != base_types.auto else self.make_default("TwnNm")

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = None

	@property
	def CtrySubDvsn(self):
		return self._CtrySubDvsn

	@CtrySubDvsn.setter
	def CtrySubDvsn(self, value):
		self._CtrySubDvsn = value if type(value) != base_types.auto else self.make_default("CtrySubDvsn")

	@CtrySubDvsn.deleter
	def CtrySubDvsn(self):
		del self._CtrySubDvsn
		self._CtrySubDvsn = None

	@property
	def PstCd(self):
		return self._PstCd

	@PstCd.setter
	def PstCd(self, value):
		self._PstCd = value if type(value) != base_types.auto else self.make_default("PstCd")

	@PstCd.deleter
	def PstCd(self):
		del self._PstCd
		self._PstCd = None

	@property
	def BldgNb(self):
		return self._BldgNb

	@BldgNb.setter
	def BldgNb(self, value):
		self._BldgNb = value if type(value) != base_types.auto else self.make_default("BldgNb")

	@BldgNb.deleter
	def BldgNb(self):
		del self._BldgNb
		self._BldgNb = None

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
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if type(value) != base_types.auto else self.make_default("StrtNm")

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrTp', type=AddressType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

