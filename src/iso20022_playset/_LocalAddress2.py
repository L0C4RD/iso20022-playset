from . import base_types
from ._Max100Text import Max100Text
from ._Max200Text import Max200Text
from ._Max35Text import Max35Text

class LocalAddress2(base_types._BaseFieldType):

	__slots__ = ["_BldgNb", "_CtrySubDvsnMjrNm", "_CtrySubDvsnMnrNm", "_Line1", "_Line2", "_PstlCd", "_StrtNm", "_TwnNm"]
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
	def Line1(self):
		return self._Line1

	@Line1.setter
	def Line1(self, value):
		self._Line1 = value if type(value) != base_types.auto else self.make_default("Line1")

	@Line1.deleter
	def Line1(self):
		del self._Line1
		self._Line1 = None

	@property
	def Line2(self):
		return self._Line2

	@Line2.setter
	def Line2(self, value):
		self._Line2 = value if type(value) != base_types.auto else self.make_default("Line2")

	@Line2.deleter
	def Line2(self):
		del self._Line2
		self._Line2 = None

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
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Line1', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Line2', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max200Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
	))

