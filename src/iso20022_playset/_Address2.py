# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOCountrySubDivisionCode
from . import ISOMax3ACountryCode
from . import Max16Text
from . import Max50Text
from . import Max99Text

class Address2(base_types._BaseFieldType):

	__slots__ = ["_AdrLine1", "_AdrLine2", "_BldgNb", "_Ctry", "_CtrySubDvsnMjr", "_CtrySubDvsnMjrNm", "_CtrySubDvsnMnr", "_CtrySubDvsnMnrNm", "_PstlCd", "_StrtNm", "_TwnNm"]
	@property
	def AdrLine1(self):
		return self._AdrLine1

	@AdrLine1.setter
	def AdrLine1(self, value):
		self._AdrLine1 = value if value is not None else base_types.UninitialisedField(self, 'AdrLine1', Max99Text, False)

	@AdrLine1.deleter
	def AdrLine1(self):
		del self._AdrLine1
		self._AdrLine1 = base_types.UninitialisedField(self, 'AdrLine1', Max99Text, False)

	@property
	def AdrLine2(self):
		return self._AdrLine2

	@AdrLine2.setter
	def AdrLine2(self, value):
		self._AdrLine2 = value if value is not None else base_types.UninitialisedField(self, 'AdrLine2', Max99Text, False)

	@AdrLine2.deleter
	def AdrLine2(self):
		del self._AdrLine2
		self._AdrLine2 = base_types.UninitialisedField(self, 'AdrLine2', Max99Text, False)

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
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', ISOMax3ACountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', ISOMax3ACountryCode, False)

	@property
	def CtrySubDvsnMjr(self):
		return self._CtrySubDvsnMjr

	@CtrySubDvsnMjr.setter
	def CtrySubDvsnMjr(self, value):
		self._CtrySubDvsnMjr = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@CtrySubDvsnMjr.deleter
	def CtrySubDvsnMjr(self):
		del self._CtrySubDvsnMjr
		self._CtrySubDvsnMjr = base_types.UninitialisedField(self, 'CtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@property
	def CtrySubDvsnMjrNm(self):
		return self._CtrySubDvsnMjrNm

	@CtrySubDvsnMjrNm.setter
	def CtrySubDvsnMjrNm(self, value):
		self._CtrySubDvsnMjrNm = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMjrNm', Max50Text, False)

	@CtrySubDvsnMjrNm.deleter
	def CtrySubDvsnMjrNm(self):
		del self._CtrySubDvsnMjrNm
		self._CtrySubDvsnMjrNm = base_types.UninitialisedField(self, 'CtrySubDvsnMjrNm', Max50Text, False)

	@property
	def CtrySubDvsnMnr(self):
		return self._CtrySubDvsnMnr

	@CtrySubDvsnMnr.setter
	def CtrySubDvsnMnr(self, value):
		self._CtrySubDvsnMnr = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@CtrySubDvsnMnr.deleter
	def CtrySubDvsnMnr(self):
		del self._CtrySubDvsnMnr
		self._CtrySubDvsnMnr = base_types.UninitialisedField(self, 'CtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@property
	def CtrySubDvsnMnrNm(self):
		return self._CtrySubDvsnMnrNm

	@CtrySubDvsnMnrNm.setter
	def CtrySubDvsnMnrNm(self, value):
		self._CtrySubDvsnMnrNm = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMnrNm', Max50Text, False)

	@CtrySubDvsnMnrNm.deleter
	def CtrySubDvsnMnrNm(self):
		del self._CtrySubDvsnMnrNm
		self._CtrySubDvsnMnrNm = base_types.UninitialisedField(self, 'CtrySubDvsnMnrNm', Max50Text, False)

	@property
	def PstlCd(self):
		return self._PstlCd

	@PstlCd.setter
	def PstlCd(self, value):
		self._PstlCd = value if value is not None else base_types.UninitialisedField(self, 'PstlCd', Max16Text, False)

	@PstlCd.deleter
	def PstlCd(self):
		del self._PstlCd
		self._PstlCd = base_types.UninitialisedField(self, 'PstlCd', Max16Text, False)

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if value is not None else base_types.UninitialisedField(self, 'StrtNm', Max99Text, False)

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = base_types.UninitialisedField(self, 'StrtNm', Max99Text, False)

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', Max50Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', Max50Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrLine1', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine2', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))