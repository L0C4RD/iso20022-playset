from . import base_types
from .Max70Text import Max70Text
from .Min2Max3AlphaText import Min2Max3AlphaText
from .Max16Text import Max16Text
from .AddressType2Code import AddressType2Code
from .Max35Text import Max35Text

class PostalAddress22(base_types._BaseFieldType):

	__slots__ = ["_AdrTp", "_Dept", "_AdrLine", "_CtryCd", "_PstCd", "_CtrySubDvsn", "_BldgNb", "_StrtNm", "_SubDept", "_TwnNm"]
	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if type(value) != base_types.auto else self.make_default("AdrTp")

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = None

	@property
	def Dept(self):
		return self._Dept

	@Dept.setter
	def Dept(self, value):
		self._Dept = value if type(value) != base_types.auto else self.make_default("Dept")

	@Dept.deleter
	def Dept(self):
		del self._Dept
		self._Dept = None

	@property
	def AdrLine(self):
		return self._AdrLine

	@AdrLine.setter
	def AdrLine(self, value):
		self._AdrLine = value if type(value) != base_types.auto else self.make_default("AdrLine")

	@AdrLine.deleter
	def AdrLine(self):
		del self._AdrLine
		self._AdrLine = None

	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if type(value) != base_types.auto else self.make_default("CtryCd")

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = None

	@property
	def PstCd(self):
		return self._PstCd

	@PstCd.setter
	def PstCd(self, value):
		self._PstCd = value if type(value) != base_types.auto else self.make_default("PstCd")

	@PstCd.deleter
	def PstCd(self):
		del self._PstCd
		self._PstCd = None

	@property
	def CtrySubDvsn(self):
		return self._CtrySubDvsn

	@CtrySubDvsn.setter
	def CtrySubDvsn(self, value):
		self._CtrySubDvsn = value if type(value) != base_types.auto else self.make_default("CtrySubDvsn")

	@CtrySubDvsn.deleter
	def CtrySubDvsn(self):
		del self._CtrySubDvsn
		self._CtrySubDvsn = None

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
	def SubDept(self):
		return self._SubDept

	@SubDept.setter
	def SubDept(self, value):
		self._SubDept = value if type(value) != base_types.auto else self.make_default("SubDept")

	@SubDept.deleter
	def SubDept(self):
		del self._SubDept
		self._SubDept = None

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
		base_types.FieldEntry(name='AdrTp', type=AddressType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtryCd', type=Min2Max3AlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubDept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

