from . import base_types
from .Max37Text import Max37Text
from .Max76Text import Max76Text
from .Max45Text import Max45Text
from .Max10Text import Max10Text
from .Exact3NumericText import Exact3NumericText
from .Min8Max28NumericText import Min8Max28NumericText
from .Max104Text import Max104Text
from .Min2Max3NumericText import Min2Max3NumericText

class PlainCardData22(base_types._BaseFieldType):

	__slots__ = ["_CrdhldrNm", "_Trck2", "_Trck1", "_Trck3", "_XpryDt", "_PAN", "_FctvDt", "_CardSeqNb", "_SvcCd"]
	@property
	def CrdhldrNm(self):
		return self._CrdhldrNm

	@CrdhldrNm.setter
	def CrdhldrNm(self, value):
		self._CrdhldrNm = value if type(value) != auto else self.make_default("CrdhldrNm")

	@CrdhldrNm.deleter
	def CrdhldrNm(self):
		del self._CrdhldrNm
		self._CrdhldrNm = None

	@property
	def Trck2(self):
		return self._Trck2

	@Trck2.setter
	def Trck2(self, value):
		self._Trck2 = value if type(value) != auto else self.make_default("Trck2")

	@Trck2.deleter
	def Trck2(self):
		del self._Trck2
		self._Trck2 = None

	@property
	def Trck1(self):
		return self._Trck1

	@Trck1.setter
	def Trck1(self, value):
		self._Trck1 = value if type(value) != auto else self.make_default("Trck1")

	@Trck1.deleter
	def Trck1(self):
		del self._Trck1
		self._Trck1 = None

	@property
	def Trck3(self):
		return self._Trck3

	@Trck3.setter
	def Trck3(self, value):
		self._Trck3 = value if type(value) != auto else self.make_default("Trck3")

	@Trck3.deleter
	def Trck3(self):
		del self._Trck3
		self._Trck3 = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if type(value) != auto else self.make_default("PAN")

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if type(value) != auto else self.make_default("CardSeqNb")

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = None

	@property
	def SvcCd(self):
		return self._SvcCd

	@SvcCd.setter
	def SvcCd(self, value):
		self._SvcCd = value if type(value) != auto else self.make_default("SvcCd")

	@SvcCd.deleter
	def SvcCd(self):
		del self._SvcCd
		self._SvcCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrdhldrNm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck2', type=Max37Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck1', type=Max76Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck3', type=Max104Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
	))

