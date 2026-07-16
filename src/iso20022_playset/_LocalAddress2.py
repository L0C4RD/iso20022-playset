# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100Text
from . import Max200Text
from . import Max35Text

class LocalAddress2(base_types._BaseFieldType):

	__slots__ = ["_BldgNb", "_CtrySubDvsnMjrNm", "_CtrySubDvsnMnrNm", "_Line1", "_Line2", "_PstlCd", "_StrtNm", "_TwnNm"]
	@property
	def BldgNb(self):
		return self._BldgNb

	@BldgNb.setter
	def BldgNb(self, value):
		self._BldgNb = value if value is not None else base_types.UninitialisedField(self, 'BldgNb', Max35Text, False)

	@BldgNb.deleter
	def BldgNb(self):
		del self._BldgNb
		self._BldgNb = base_types.UninitialisedField(self, 'BldgNb', Max35Text, False)

	@property
	def CtrySubDvsnMjrNm(self):
		return self._CtrySubDvsnMjrNm

	@CtrySubDvsnMjrNm.setter
	def CtrySubDvsnMjrNm(self, value):
		self._CtrySubDvsnMjrNm = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMjrNm', Max100Text, False)

	@CtrySubDvsnMjrNm.deleter
	def CtrySubDvsnMjrNm(self):
		del self._CtrySubDvsnMjrNm
		self._CtrySubDvsnMjrNm = base_types.UninitialisedField(self, 'CtrySubDvsnMjrNm', Max100Text, False)

	@property
	def CtrySubDvsnMnrNm(self):
		return self._CtrySubDvsnMnrNm

	@CtrySubDvsnMnrNm.setter
	def CtrySubDvsnMnrNm(self, value):
		self._CtrySubDvsnMnrNm = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMnrNm', Max100Text, False)

	@CtrySubDvsnMnrNm.deleter
	def CtrySubDvsnMnrNm(self):
		del self._CtrySubDvsnMnrNm
		self._CtrySubDvsnMnrNm = base_types.UninitialisedField(self, 'CtrySubDvsnMnrNm', Max100Text, False)

	@property
	def Line1(self):
		return self._Line1

	@Line1.setter
	def Line1(self, value):
		self._Line1 = value if value is not None else base_types.UninitialisedField(self, 'Line1', Max200Text, False)

	@Line1.deleter
	def Line1(self):
		del self._Line1
		self._Line1 = base_types.UninitialisedField(self, 'Line1', Max200Text, False)

	@property
	def Line2(self):
		return self._Line2

	@Line2.setter
	def Line2(self, value):
		self._Line2 = value if value is not None else base_types.UninitialisedField(self, 'Line2', Max200Text, False)

	@Line2.deleter
	def Line2(self):
		del self._Line2
		self._Line2 = base_types.UninitialisedField(self, 'Line2', Max200Text, False)

	@property
	def PstlCd(self):
		return self._PstlCd

	@PstlCd.setter
	def PstlCd(self, value):
		self._PstlCd = value if value is not None else base_types.UninitialisedField(self, 'PstlCd', Max35Text, False)

	@PstlCd.deleter
	def PstlCd(self):
		del self._PstlCd
		self._PstlCd = base_types.UninitialisedField(self, 'PstlCd', Max35Text, False)

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if value is not None else base_types.UninitialisedField(self, 'StrtNm', Max200Text, False)

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = base_types.UninitialisedField(self, 'StrtNm', Max200Text, False)

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', Max100Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', Max100Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BldgNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjrNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Line1', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Line2', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
	))