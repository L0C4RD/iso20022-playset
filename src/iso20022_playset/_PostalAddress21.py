# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressType2Choice
from . import CountryCode
from . import Max10Text
from . import Max16Text
from . import Max35Text
from . import Max70Text
from . import YesNoIndicator

class PostalAddress21(base_types._BaseFieldType):

	__slots__ = ["_AdrLine", "_AdrTp", "_BldgNb", "_BldgNm", "_CareOf", "_Ctry", "_DstrctNm", "_Flr", "_MlngInd", "_PstBx", "_PstCd", "_RegnAdrInd", "_SdInBldg", "_Stat", "_StrtNm", "_SuiteId", "_TwnNm", "_Vllg"]
	@property
	def AdrLine(self):
		return self._AdrLine

	@AdrLine.setter
	def AdrLine(self, value):
		self._AdrLine = value if value is not None else base_types.UninitialisedField(self, 'AdrLine', Max70Text, True)

	@AdrLine.deleter
	def AdrLine(self):
		del self._AdrLine
		self._AdrLine = base_types.UninitialisedField(self, 'AdrLine', Max70Text, True)

	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if value is not None else base_types.UninitialisedField(self, 'AdrTp', AddressType2Choice, False)

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = base_types.UninitialisedField(self, 'AdrTp', AddressType2Choice, False)

	@property
	def BldgNb(self):
		return self._BldgNb

	@BldgNb.setter
	def BldgNb(self, value):
		self._BldgNb = value if value is not None else base_types.UninitialisedField(self, 'BldgNb', Max16Text, False)

	@BldgNb.deleter
	def BldgNb(self):
		del self._BldgNb
		self._BldgNb = base_types.UninitialisedField(self, 'BldgNb', Max16Text, False)

	@property
	def BldgNm(self):
		return self._BldgNm

	@BldgNm.setter
	def BldgNm(self, value):
		self._BldgNm = value if value is not None else base_types.UninitialisedField(self, 'BldgNm', Max35Text, False)

	@BldgNm.deleter
	def BldgNm(self):
		del self._BldgNm
		self._BldgNm = base_types.UninitialisedField(self, 'BldgNm', Max35Text, False)

	@property
	def CareOf(self):
		return self._CareOf

	@CareOf.setter
	def CareOf(self, value):
		self._CareOf = value if value is not None else base_types.UninitialisedField(self, 'CareOf', Max70Text, False)

	@CareOf.deleter
	def CareOf(self):
		del self._CareOf
		self._CareOf = base_types.UninitialisedField(self, 'CareOf', Max70Text, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def DstrctNm(self):
		return self._DstrctNm

	@DstrctNm.setter
	def DstrctNm(self, value):
		self._DstrctNm = value if value is not None else base_types.UninitialisedField(self, 'DstrctNm', Max35Text, False)

	@DstrctNm.deleter
	def DstrctNm(self):
		del self._DstrctNm
		self._DstrctNm = base_types.UninitialisedField(self, 'DstrctNm', Max35Text, False)

	@property
	def Flr(self):
		return self._Flr

	@Flr.setter
	def Flr(self, value):
		self._Flr = value if value is not None else base_types.UninitialisedField(self, 'Flr', Max70Text, False)

	@Flr.deleter
	def Flr(self):
		del self._Flr
		self._Flr = base_types.UninitialisedField(self, 'Flr', Max70Text, False)

	@property
	def MlngInd(self):
		return self._MlngInd

	@MlngInd.setter
	def MlngInd(self, value):
		self._MlngInd = value if value is not None else base_types.UninitialisedField(self, 'MlngInd', YesNoIndicator, False)

	@MlngInd.deleter
	def MlngInd(self):
		del self._MlngInd
		self._MlngInd = base_types.UninitialisedField(self, 'MlngInd', YesNoIndicator, False)

	@property
	def PstBx(self):
		return self._PstBx

	@PstBx.setter
	def PstBx(self, value):
		self._PstBx = value if value is not None else base_types.UninitialisedField(self, 'PstBx', Max10Text, False)

	@PstBx.deleter
	def PstBx(self):
		del self._PstBx
		self._PstBx = base_types.UninitialisedField(self, 'PstBx', Max10Text, False)

	@property
	def PstCd(self):
		return self._PstCd

	@PstCd.setter
	def PstCd(self, value):
		self._PstCd = value if value is not None else base_types.UninitialisedField(self, 'PstCd', Max16Text, False)

	@PstCd.deleter
	def PstCd(self):
		del self._PstCd
		self._PstCd = base_types.UninitialisedField(self, 'PstCd', Max16Text, False)

	@property
	def RegnAdrInd(self):
		return self._RegnAdrInd

	@RegnAdrInd.setter
	def RegnAdrInd(self, value):
		self._RegnAdrInd = value if value is not None else base_types.UninitialisedField(self, 'RegnAdrInd', YesNoIndicator, False)

	@RegnAdrInd.deleter
	def RegnAdrInd(self):
		del self._RegnAdrInd
		self._RegnAdrInd = base_types.UninitialisedField(self, 'RegnAdrInd', YesNoIndicator, False)

	@property
	def SdInBldg(self):
		return self._SdInBldg

	@SdInBldg.setter
	def SdInBldg(self, value):
		self._SdInBldg = value if value is not None else base_types.UninitialisedField(self, 'SdInBldg', Max35Text, False)

	@SdInBldg.deleter
	def SdInBldg(self):
		del self._SdInBldg
		self._SdInBldg = base_types.UninitialisedField(self, 'SdInBldg', Max35Text, False)

	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if value is not None else base_types.UninitialisedField(self, 'Stat', Max70Text, False)

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = base_types.UninitialisedField(self, 'Stat', Max70Text, False)

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if value is not None else base_types.UninitialisedField(self, 'StrtNm', Max70Text, False)

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = base_types.UninitialisedField(self, 'StrtNm', Max70Text, False)

	@property
	def SuiteId(self):
		return self._SuiteId

	@SuiteId.setter
	def SuiteId(self, value):
		self._SuiteId = value if value is not None else base_types.UninitialisedField(self, 'SuiteId', Max10Text, False)

	@SuiteId.deleter
	def SuiteId(self):
		del self._SuiteId
		self._SuiteId = base_types.UninitialisedField(self, 'SuiteId', Max10Text, False)

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', Max35Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', Max35Text, False)

	@property
	def Vllg(self):
		return self._Vllg

	@Vllg.setter
	def Vllg(self, value):
		self._Vllg = value if value is not None else base_types.UninitialisedField(self, 'Vllg', Max70Text, False)

	@Vllg.deleter
	def Vllg(self):
		del self._Vllg
		self._Vllg = base_types.UninitialisedField(self, 'Vllg', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdrTp', type=AddressType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CareOf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Flr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstBx', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAdrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SdInBldg', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stat', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SuiteId', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vllg', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))