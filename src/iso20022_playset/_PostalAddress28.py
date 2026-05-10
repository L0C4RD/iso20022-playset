from . import base_types
from .Max35Text import Max35Text
from .Max16Text import Max16Text
from .ISODate import ISODate
from .CountryCode import CountryCode
from .Max70Text import Max70Text
from .AddressType3Choice import AddressType3Choice
from .Max140Text import Max140Text

class PostalAddress28(base_types._BaseFieldType):

	__slots__ = ["_Room", "_BldgNm", "_CtrySubDvsn", "_DstrctNm", "_SubDept", "_PstBx", "_TwnNm", "_UnitNb", "_Ctry", "_AdrTp", "_Dept", "_Flr", "_PstCd", "_AdrLine", "_StrtNm", "_CareOf", "_VldFr", "_BldgNb", "_TwnLctnNm"]
	@property
	def Room(self):
		return self._Room

	@Room.setter
	def Room(self, value):
		self._Room = value if type(value) != base_types.auto else self.make_default("Room")

	@Room.deleter
	def Room(self):
		del self._Room
		self._Room = None

	@property
	def BldgNm(self):
		return self._BldgNm

	@BldgNm.setter
	def BldgNm(self, value):
		self._BldgNm = value if type(value) != base_types.auto else self.make_default("BldgNm")

	@BldgNm.deleter
	def BldgNm(self):
		del self._BldgNm
		self._BldgNm = None

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
	def DstrctNm(self):
		return self._DstrctNm

	@DstrctNm.setter
	def DstrctNm(self, value):
		self._DstrctNm = value if type(value) != base_types.auto else self.make_default("DstrctNm")

	@DstrctNm.deleter
	def DstrctNm(self):
		del self._DstrctNm
		self._DstrctNm = None

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
	def PstBx(self):
		return self._PstBx

	@PstBx.setter
	def PstBx(self, value):
		self._PstBx = value if type(value) != base_types.auto else self.make_default("PstBx")

	@PstBx.deleter
	def PstBx(self):
		del self._PstBx
		self._PstBx = None

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

	@property
	def UnitNb(self):
		return self._UnitNb

	@UnitNb.setter
	def UnitNb(self, value):
		self._UnitNb = value if type(value) != base_types.auto else self.make_default("UnitNb")

	@UnitNb.deleter
	def UnitNb(self):
		del self._UnitNb
		self._UnitNb = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

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
	def Flr(self):
		return self._Flr

	@Flr.setter
	def Flr(self, value):
		self._Flr = value if type(value) != base_types.auto else self.make_default("Flr")

	@Flr.deleter
	def Flr(self):
		del self._Flr
		self._Flr = None

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
	def CareOf(self):
		return self._CareOf

	@CareOf.setter
	def CareOf(self, value):
		self._CareOf = value if type(value) != base_types.auto else self.make_default("CareOf")

	@CareOf.deleter
	def CareOf(self):
		del self._CareOf
		self._CareOf = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

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
	def TwnLctnNm(self):
		return self._TwnLctnNm

	@TwnLctnNm.setter
	def TwnLctnNm(self, value):
		self._TwnLctnNm = value if type(value) != base_types.auto else self.make_default("TwnLctnNm")

	@TwnLctnNm.deleter
	def TwnLctnNm(self):
		del self._TwnLctnNm
		self._TwnLctnNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Room', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrctNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubDept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstBx', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrTp', type=AddressType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Flr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=7, mutex_group=None, array=True),
		base_types.FieldEntry(name='StrtNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CareOf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnLctnNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

