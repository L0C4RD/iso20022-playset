from . import base_types
from ._CardSecurityInformation1 import CardSecurityInformation1
from ._Exact3NumericText import Exact3NumericText
from ._ISOYearMonth import ISOYearMonth
from ._Min8Max28NumericText import Min8Max28NumericText
from ._TrackData1 import TrackData1
from ._Min2Max3NumericText import Min2Max3NumericText

class PlainCardData1(base_types._BaseFieldType):

	__slots__ = ["_FctvDt", "_PAN", "_TrckData", "_CardSctyCd", "_SvcCd", "_XpryDt", "_CardSeqNb"]
	@property
	def CardSctyCd(self):
		return self._CardSctyCd

	@CardSctyCd.setter
	def CardSctyCd(self, value):
		self._CardSctyCd = value if type(value) != base_types.auto else self.make_default("CardSctyCd")

	@CardSctyCd.deleter
	def CardSctyCd(self):
		del self._CardSctyCd
		self._CardSctyCd = None

	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if type(value) != base_types.auto else self.make_default("CardSeqNb")

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != base_types.auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if type(value) != base_types.auto else self.make_default("PAN")

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = None

	@property
	def SvcCd(self):
		return self._SvcCd

	@SvcCd.setter
	def SvcCd(self, value):
		self._SvcCd = value if type(value) != base_types.auto else self.make_default("SvcCd")

	@SvcCd.deleter
	def SvcCd(self):
		del self._SvcCd
		self._SvcCd = None

	@property
	def TrckData(self):
		return self._TrckData

	@TrckData.setter
	def TrckData(self, value):
		self._TrckData = value if type(value) != base_types.auto else self.make_default("TrckData")

	@TrckData.deleter
	def TrckData(self):
		del self._TrckData
		self._TrckData = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSctyCd', type=CardSecurityInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckData', type=TrackData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=1, max=1, mutex_group=None, array=False),
	))

