import base_types
import Min2Max3NumericText
import ISOYearMonth
import CardSecurityInformation1
import Exact3NumericText
import TrackData1
import Min8Max28NumericText

class PlainCardData1(base_types._BaseFieldType):

	__slots__ = ["_SvcCd", "_PAN", "_CardSeqNb", "_TrckData", "_CardSctyCd", "_FctvDt", "_XpryDt"]
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
	def TrckData(self):
		return self._TrckData

	@TrckData.setter
	def TrckData(self, value):
		self._TrckData = value if type(value) != auto else self.make_default("TrckData")

	@TrckData.deleter
	def TrckData(self):
		del self._TrckData
		self._TrckData = None

	@property
	def CardSctyCd(self):
		return self._CardSctyCd

	@CardSctyCd.setter
	def CardSctyCd(self, value):
		self._CardSctyCd = value if type(value) != auto else self.make_default("CardSctyCd")

	@CardSctyCd.deleter
	def CardSctyCd(self):
		del self._CardSctyCd
		self._CardSctyCd = None

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
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckData', type=TrackData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardSctyCd', type=CardSecurityInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=1, max=1, mutex_group=None, array=False),
	))

