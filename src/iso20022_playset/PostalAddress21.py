from . import base_types
from .CountryCode import CountryCode
from .Max35Text import Max35Text
from .Max16Text import Max16Text
from .YesNoIndicator import YesNoIndicator
from .Max10Text import Max10Text
from .Max70Text import Max70Text
from .AddressType2Choice import AddressType2Choice

class PostalAddress21(base_types._BaseFieldType):

	__slots__ = ["_Flr", "_SuiteId", "_Ctry", "_AdrLine", "_SdInBldg", "_MlngInd", "_PstBx", "_BldgNm", "_Vllg", "_Stat", "_DstrctNm", "_RegnAdrInd", "_CareOf", "_TwnNm", "_BldgNb", "_AdrTp", "_StrtNm", "_PstCd"]
	@property
	def Flr(self):
		return self._Flr

	@Flr.setter
	def Flr(self, value):
		self._Flr = value if type(value) != auto else self.make_default("Flr")

	@Flr.deleter
	def Flr(self):
		del self._Flr
		self._Flr = None

	@property
	def SuiteId(self):
		return self._SuiteId

	@SuiteId.setter
	def SuiteId(self, value):
		self._SuiteId = value if type(value) != auto else self.make_default("SuiteId")

	@SuiteId.deleter
	def SuiteId(self):
		del self._SuiteId
		self._SuiteId = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def AdrLine(self):
		return self._AdrLine

	@AdrLine.setter
	def AdrLine(self, value):
		self._AdrLine = value if type(value) != auto else self.make_default("AdrLine")

	@AdrLine.deleter
	def AdrLine(self):
		del self._AdrLine
		self._AdrLine = None

	@property
	def SdInBldg(self):
		return self._SdInBldg

	@SdInBldg.setter
	def SdInBldg(self, value):
		self._SdInBldg = value if type(value) != auto else self.make_default("SdInBldg")

	@SdInBldg.deleter
	def SdInBldg(self):
		del self._SdInBldg
		self._SdInBldg = None

	@property
	def MlngInd(self):
		return self._MlngInd

	@MlngInd.setter
	def MlngInd(self, value):
		self._MlngInd = value if type(value) != auto else self.make_default("MlngInd")

	@MlngInd.deleter
	def MlngInd(self):
		del self._MlngInd
		self._MlngInd = None

	@property
	def PstBx(self):
		return self._PstBx

	@PstBx.setter
	def PstBx(self, value):
		self._PstBx = value if type(value) != auto else self.make_default("PstBx")

	@PstBx.deleter
	def PstBx(self):
		del self._PstBx
		self._PstBx = None

	@property
	def BldgNm(self):
		return self._BldgNm

	@BldgNm.setter
	def BldgNm(self, value):
		self._BldgNm = value if type(value) != auto else self.make_default("BldgNm")

	@BldgNm.deleter
	def BldgNm(self):
		del self._BldgNm
		self._BldgNm = None

	@property
	def Vllg(self):
		return self._Vllg

	@Vllg.setter
	def Vllg(self, value):
		self._Vllg = value if type(value) != auto else self.make_default("Vllg")

	@Vllg.deleter
	def Vllg(self):
		del self._Vllg
		self._Vllg = None

	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if type(value) != auto else self.make_default("Stat")

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = None

	@property
	def DstrctNm(self):
		return self._DstrctNm

	@DstrctNm.setter
	def DstrctNm(self, value):
		self._DstrctNm = value if type(value) != auto else self.make_default("DstrctNm")

	@DstrctNm.deleter
	def DstrctNm(self):
		del self._DstrctNm
		self._DstrctNm = None

	@property
	def RegnAdrInd(self):
		return self._RegnAdrInd

	@RegnAdrInd.setter
	def RegnAdrInd(self, value):
		self._RegnAdrInd = value if type(value) != auto else self.make_default("RegnAdrInd")

	@RegnAdrInd.deleter
	def RegnAdrInd(self):
		del self._RegnAdrInd
		self._RegnAdrInd = None

	@property
	def CareOf(self):
		return self._CareOf

	@CareOf.setter
	def CareOf(self, value):
		self._CareOf = value if type(value) != auto else self.make_default("CareOf")

	@CareOf.deleter
	def CareOf(self):
		del self._CareOf
		self._CareOf = None

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if type(value) != auto else self.make_default("TwnNm")

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = None

	@property
	def BldgNb(self):
		return self._BldgNb

	@BldgNb.setter
	def BldgNb(self, value):
		self._BldgNb = value if type(value) != auto else self.make_default("BldgNb")

	@BldgNb.deleter
	def BldgNb(self):
		del self._BldgNb
		self._BldgNb = None

	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if type(value) != auto else self.make_default("AdrTp")

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = None

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if type(value) != auto else self.make_default("StrtNm")

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = None

	@property
	def PstCd(self):
		return self._PstCd

	@PstCd.setter
	def PstCd(self, value):
		self._PstCd = value if type(value) != auto else self.make_default("PstCd")

	@PstCd.deleter
	def PstCd(self):
		del self._PstCd
		self._PstCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Flr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SuiteId', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='SdInBldg', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstBx', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vllg', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stat', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAdrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CareOf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrTp', type=AddressType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
	))

