# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max16Text
from . import Max35Text
from . import Max70Text

class PostalAddress2(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_CtrySubDvsn", "_PstCdId", "_StrtNm", "_TwnNm"]
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
	def PstCdId(self):
		return self._PstCdId

	@PstCdId.setter
	def PstCdId(self, value):
		self._PstCdId = value if value is not None else base_types.UninitialisedField(self, 'PstCdId', Max16Text, False)

	@PstCdId.deleter
	def PstCdId(self):
		del self._PstCdId
		self._PstCdId = base_types.UninitialisedField(self, 'PstCdId', Max16Text, False)

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
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCdId', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))