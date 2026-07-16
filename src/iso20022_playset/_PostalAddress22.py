# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressType2Code
from . import Max16Text
from . import Max35Text
from . import Max70Text
from . import Min2Max3AlphaText

class PostalAddress22(base_types._BaseFieldType):

	__slots__ = ["_AdrLine", "_AdrTp", "_BldgNb", "_CtryCd", "_CtrySubDvsn", "_Dept", "_PstCd", "_StrtNm", "_SubDept", "_TwnNm"]
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
		self._AdrTp = value if value is not None else base_types.UninitialisedField(self, 'AdrTp', AddressType2Code, False)

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = base_types.UninitialisedField(self, 'AdrTp', AddressType2Code, False)

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
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if value is not None else base_types.UninitialisedField(self, 'CtryCd', Min2Max3AlphaText, False)

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = base_types.UninitialisedField(self, 'CtryCd', Min2Max3AlphaText, False)

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
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', Max70Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrLine', type=Max70Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdrTp', type=AddressType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=Min2Max3AlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubDept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))