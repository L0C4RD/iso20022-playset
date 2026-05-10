from . import base_types
from .Max35Text import Max35Text
from .Max100Text import Max100Text
from .Max200Text import Max200Text

class LocalAddress1(base_types._BaseFieldType):

	__slots__ = ["_BldgNb", "_CtrySubDvsnMjrNm", "_AdrLine2", "_CtrySubDvsnMnrNm", "_PstlCd", "_AdrLine1", "_StrtNm", "_TwnNm"]
	@property
	def BldgNb(self):
		return self._BldgNb

	@BldgNb.setter
	def BldgNb(self, value):
		self._BldgNb = value if type(value) != base_types.auto else self.make_default("BldgNb")

	@BldgNb.deleter
	def BldgNb(self):
		del self._BldgNb
		self._BldgNb = None

	@property
	def CtrySubDvsnMjrNm(self):
		return self._CtrySubDvsnMjrNm

	@CtrySubDvsnMjrNm.setter
	def CtrySubDvsnMjrNm(self, value):
		self._CtrySubDvsnMjrNm = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMjrNm")

	@CtrySubDvsnMjrNm.deleter
	def CtrySubDvsnMjrNm(self):
		del self._CtrySubDvsnMjrNm
		self._CtrySubDvsnMjrNm = None

	@property
	def AdrLine2(self):
		return self._AdrLine2

	@AdrLine2.setter
	def AdrLine2(self, value):
		self._AdrLine2 = value if type(value) != base_types.auto else self.make_default("AdrLine2")

	@AdrLine2.deleter
	def AdrLine2(self):
		del self._AdrLine2
		self._AdrLine2 = None

	@property
	def CtrySubDvsnMnrNm(self):
		return self._CtrySubDvsnMnrNm

	@CtrySubDvsnMnrNm.setter
	def CtrySubDvsnMnrNm(self, value):
		self._CtrySubDvsnMnrNm = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMnrNm")

	@CtrySubDvsnMnrNm.deleter
	def CtrySubDvsnMnrNm(self):
		del self._CtrySubDvsnMnrNm
		self._CtrySubDvsnMnrNm = None

	@property
	def PstlCd(self):
		return self._PstlCd

	@PstlCd.setter
	def PstlCd(self, value):
		self._PstlCd = value if type(value) != base_types.auto else self.make_default("PstlCd")

	@PstlCd.deleter
	def PstlCd(self):
		del self._PstlCd
		self._PstlCd = None

	@property
	def AdrLine1(self):
		return self._AdrLine1

	@AdrLine1.setter
	def AdrLine1(self, value):
		self._AdrLine1 = value if type(value) != base_types.auto else self.make_default("AdrLine1")

	@AdrLine1.deleter
	def AdrLine1(self):
		del self._AdrLine1
		self._AdrLine1 = None

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if type(value) != base_types.auto else self.make_default("StrtNm")

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = None

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if type(value) != base_types.auto else self.make_default("TwnNm")

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BldgNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjrNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine2', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine1', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
	))

