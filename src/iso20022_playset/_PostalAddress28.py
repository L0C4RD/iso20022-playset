# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressType3Choice
from . import CountryCode
from . import ISODate
from . import Max140Text
from . import Max16Text
from . import Max35Text
from . import Max70Text

class PostalAddress28(base_types._BaseFieldType):

	__slots__ = ["_AdrLine", "_AdrTp", "_BldgNb", "_BldgNm", "_CareOf", "_Ctry", "_CtrySubDvsn", "_Dept", "_DstrctNm", "_Flr", "_PstBx", "_PstCd", "_Room", "_StrtNm", "_SubDept", "_TwnLctnNm", "_TwnNm", "_UnitNb", "_VldFr"]
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
		self._AdrTp = value if value is not None else base_types.UninitialisedField(self, 'AdrTp', AddressType3Choice, False)

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = base_types.UninitialisedField(self, 'AdrTp', AddressType3Choice, False)

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
		self._BldgNm = value if value is not None else base_types.UninitialisedField(self, 'BldgNm', Max140Text, False)

	@BldgNm.deleter
	def BldgNm(self):
		del self._BldgNm
		self._BldgNm = base_types.UninitialisedField(self, 'BldgNm', Max140Text, False)

	@property
	def CareOf(self):
		return self._CareOf

	@CareOf.setter
	def CareOf(self, value):
		self._CareOf = value if value is not None else base_types.UninitialisedField(self, 'CareOf', Max140Text, False)

	@CareOf.deleter
	def CareOf(self):
		del self._CareOf
		self._CareOf = base_types.UninitialisedField(self, 'CareOf', Max140Text, False)

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
		self._CtrySubDvsn = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsn', Max35Text, False)

	@CtrySubDvsn.deleter
	def CtrySubDvsn(self):
		del self._CtrySubDvsn
		self._CtrySubDvsn = base_types.UninitialisedField(self, 'CtrySubDvsn', Max35Text, False)

	@property
	def Dept(self):
		return self._Dept

	@Dept.setter
	def Dept(self, value):
		self._Dept = value if value is not None else base_types.UninitialisedField(self, 'Dept', Max70Text, False)

	@Dept.deleter
	def Dept(self):
		del self._Dept
		self._Dept = base_types.UninitialisedField(self, 'Dept', Max70Text, False)

	@property
	def DstrctNm(self):
		return self._DstrctNm

	@DstrctNm.setter
	def DstrctNm(self, value):
		self._DstrctNm = value if value is not None else base_types.UninitialisedField(self, 'DstrctNm', Max140Text, False)

	@DstrctNm.deleter
	def DstrctNm(self):
		del self._DstrctNm
		self._DstrctNm = base_types.UninitialisedField(self, 'DstrctNm', Max140Text, False)

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
	def PstBx(self):
		return self._PstBx

	@PstBx.setter
	def PstBx(self, value):
		self._PstBx = value if value is not None else base_types.UninitialisedField(self, 'PstBx', Max16Text, False)

	@PstBx.deleter
	def PstBx(self):
		del self._PstBx
		self._PstBx = base_types.UninitialisedField(self, 'PstBx', Max16Text, False)

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
	def Room(self):
		return self._Room

	@Room.setter
	def Room(self, value):
		self._Room = value if value is not None else base_types.UninitialisedField(self, 'Room', Max70Text, False)

	@Room.deleter
	def Room(self):
		del self._Room
		self._Room = base_types.UninitialisedField(self, 'Room', Max70Text, False)

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if value is not None else base_types.UninitialisedField(self, 'StrtNm', Max140Text, False)

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = base_types.UninitialisedField(self, 'StrtNm', Max140Text, False)

	@property
	def SubDept(self):
		return self._SubDept

	@SubDept.setter
	def SubDept(self, value):
		self._SubDept = value if value is not None else base_types.UninitialisedField(self, 'SubDept', Max70Text, False)

	@SubDept.deleter
	def SubDept(self):
		del self._SubDept
		self._SubDept = base_types.UninitialisedField(self, 'SubDept', Max70Text, False)

	@property
	def TwnLctnNm(self):
		return self._TwnLctnNm

	@TwnLctnNm.setter
	def TwnLctnNm(self, value):
		self._TwnLctnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnLctnNm', Max140Text, False)

	@TwnLctnNm.deleter
	def TwnLctnNm(self):
		del self._TwnLctnNm
		self._TwnLctnNm = base_types.UninitialisedField(self, 'TwnLctnNm', Max140Text, False)

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', Max140Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', Max140Text, False)

	@property
	def UnitNb(self):
		return self._UnitNb

	@UnitNb.setter
	def UnitNb(self, value):
		self._UnitNb = value if value is not None else base_types.UninitialisedField(self, 'UnitNb', Max16Text, False)

	@UnitNb.deleter
	def UnitNb(self):
		del self._UnitNb
		self._UnitNb = base_types.UninitialisedField(self, 'UnitNb', Max16Text, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=7, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdrTp', type=AddressType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CareOf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrctNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Flr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstBx', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Room', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubDept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnLctnNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))