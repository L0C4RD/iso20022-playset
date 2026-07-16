# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import GeographicLocation1Choice
from . import Max16Text
from . import Max35Text
from . import Max70Text

class PostalAddress17(base_types._BaseFieldType):

	__slots__ = ["_AdrLine", "_BldgNb", "_Ctry", "_CtrySubDvsn", "_GLctn", "_PstCd", "_StrtNm", "_TwnNm"]
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
	def CtrySubDvsn(self):
		return self._CtrySubDvsn

	@CtrySubDvsn.setter
	def CtrySubDvsn(self, value):
		self._CtrySubDvsn = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsn', Max35Text, True)

	@CtrySubDvsn.deleter
	def CtrySubDvsn(self):
		del self._CtrySubDvsn
		self._CtrySubDvsn = base_types.UninitialisedField(self, 'CtrySubDvsn', Max35Text, True)

	@property
	def GLctn(self):
		return self._GLctn

	@GLctn.setter
	def GLctn(self, value):
		self._GLctn = value if value is not None else base_types.UninitialisedField(self, 'GLctn', GeographicLocation1Choice, False)

	@GLctn.deleter
	def GLctn(self):
		del self._GLctn
		self._GLctn = base_types.UninitialisedField(self, 'GLctn', GeographicLocation1Choice, False)

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
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', Max35Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='GLctn', type=GeographicLocation1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))