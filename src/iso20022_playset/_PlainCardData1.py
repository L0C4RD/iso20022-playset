# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardSecurityInformation1
from . import Exact3NumericText
from . import ISOYearMonth
from . import Min2Max3NumericText
from . import Min8Max28NumericText
from . import TrackData1

class PlainCardData1(base_types._BaseFieldType):

	__slots__ = ["_CardSctyCd", "_CardSeqNb", "_FctvDt", "_PAN", "_SvcCd", "_TrckData", "_XpryDt"]
	@property
	def CardSctyCd(self):
		return self._CardSctyCd

	@CardSctyCd.setter
	def CardSctyCd(self, value):
		self._CardSctyCd = value if value is not None else base_types.UninitialisedField(self, 'CardSctyCd', CardSecurityInformation1, False)

	@CardSctyCd.deleter
	def CardSctyCd(self):
		del self._CardSctyCd
		self._CardSctyCd = base_types.UninitialisedField(self, 'CardSctyCd', CardSecurityInformation1, False)

	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if value is not None else base_types.UninitialisedField(self, 'CardSeqNb', Min2Max3NumericText, False)

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = base_types.UninitialisedField(self, 'CardSeqNb', Min2Max3NumericText, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', ISOYearMonth, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', ISOYearMonth, False)

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if value is not None else base_types.UninitialisedField(self, 'PAN', Min8Max28NumericText, False)

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = base_types.UninitialisedField(self, 'PAN', Min8Max28NumericText, False)

	@property
	def SvcCd(self):
		return self._SvcCd

	@SvcCd.setter
	def SvcCd(self, value):
		self._SvcCd = value if value is not None else base_types.UninitialisedField(self, 'SvcCd', Exact3NumericText, False)

	@SvcCd.deleter
	def SvcCd(self):
		del self._SvcCd
		self._SvcCd = base_types.UninitialisedField(self, 'SvcCd', Exact3NumericText, False)

	@property
	def TrckData(self):
		return self._TrckData

	@TrckData.setter
	def TrckData(self, value):
		self._TrckData = value if value is not None else base_types.UninitialisedField(self, 'TrckData', TrackData1, True)

	@TrckData.deleter
	def TrckData(self):
		del self._TrckData
		self._TrckData = base_types.UninitialisedField(self, 'TrckData', TrackData1, True)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISOYearMonth, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISOYearMonth, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSctyCd', type=CardSecurityInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckData', type=TrackData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=1, max=1, mutex_group=None, array=False),
	))