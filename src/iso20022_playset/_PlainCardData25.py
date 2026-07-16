# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact3NumericText
from . import Max104Text
from . import Max10DateText
from . import Max10Text
from . import Max37Text
from . import Max45Text
from . import Max76Text
from . import Min2Max3NumericText
from . import Min8Max28NumericText

class PlainCardData25(base_types._BaseFieldType):

	__slots__ = ["_CardSeqNb", "_CrdhldrNm", "_FctvDt", "_PAN", "_SvcCd", "_Trck1", "_Trck2", "_Trck3", "_XpryDt"]
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
	def CrdhldrNm(self):
		return self._CrdhldrNm

	@CrdhldrNm.setter
	def CrdhldrNm(self, value):
		self._CrdhldrNm = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrNm', Max45Text, False)

	@CrdhldrNm.deleter
	def CrdhldrNm(self):
		del self._CrdhldrNm
		self._CrdhldrNm = base_types.UninitialisedField(self, 'CrdhldrNm', Max45Text, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', Max10Text, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', Max10Text, False)

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
	def Trck1(self):
		return self._Trck1

	@Trck1.setter
	def Trck1(self, value):
		self._Trck1 = value if value is not None else base_types.UninitialisedField(self, 'Trck1', Max76Text, False)

	@Trck1.deleter
	def Trck1(self):
		del self._Trck1
		self._Trck1 = base_types.UninitialisedField(self, 'Trck1', Max76Text, False)

	@property
	def Trck2(self):
		return self._Trck2

	@Trck2.setter
	def Trck2(self, value):
		self._Trck2 = value if value is not None else base_types.UninitialisedField(self, 'Trck2', Max37Text, False)

	@Trck2.deleter
	def Trck2(self):
		del self._Trck2
		self._Trck2 = base_types.UninitialisedField(self, 'Trck2', Max37Text, False)

	@property
	def Trck3(self):
		return self._Trck3

	@Trck3.setter
	def Trck3(self, value):
		self._Trck3 = value if value is not None else base_types.UninitialisedField(self, 'Trck3', Max104Text, False)

	@Trck3.deleter
	def Trck3(self):
		del self._Trck3
		self._Trck3 = base_types.UninitialisedField(self, 'Trck3', Max104Text, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', Max10DateText, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', Max10DateText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrNm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck1', type=Max76Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck2', type=Max37Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck3', type=Max104Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=Max10DateText, min=0, max=1, mutex_group=None, array=False),
	))