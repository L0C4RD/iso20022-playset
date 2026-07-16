# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max16Text
from . import Max35Text

class StructuredLongPostalAddress1(base_types._BaseFieldType):

	__slots__ = ["_BldgNm", "_Ctry", "_CtyId", "_DstrctNm", "_Flr", "_POB", "_PstCdId", "_RgnId", "_Stat", "_StrtBldgId", "_StrtNm", "_TwnNm"]
	@property
	def BldgNm(self):
		return self._BldgNm

	@BldgNm.setter
	def BldgNm(self, value):
		self._BldgNm = value if value is not None else base_types.UninitialisedField(self, 'BldgNm', Max35Text, False)

	@BldgNm.deleter
	def BldgNm(self):
		del self._BldgNm
		self._BldgNm = base_types.UninitialisedField(self, 'BldgNm', Max35Text, False)

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
	def CtyId(self):
		return self._CtyId

	@CtyId.setter
	def CtyId(self, value):
		self._CtyId = value if value is not None else base_types.UninitialisedField(self, 'CtyId', Max35Text, False)

	@CtyId.deleter
	def CtyId(self):
		del self._CtyId
		self._CtyId = base_types.UninitialisedField(self, 'CtyId', Max35Text, False)

	@property
	def DstrctNm(self):
		return self._DstrctNm

	@DstrctNm.setter
	def DstrctNm(self, value):
		self._DstrctNm = value if value is not None else base_types.UninitialisedField(self, 'DstrctNm', Max35Text, False)

	@DstrctNm.deleter
	def DstrctNm(self):
		del self._DstrctNm
		self._DstrctNm = base_types.UninitialisedField(self, 'DstrctNm', Max35Text, False)

	@property
	def Flr(self):
		return self._Flr

	@Flr.setter
	def Flr(self, value):
		self._Flr = value if value is not None else base_types.UninitialisedField(self, 'Flr', Max16Text, False)

	@Flr.deleter
	def Flr(self):
		del self._Flr
		self._Flr = base_types.UninitialisedField(self, 'Flr', Max16Text, False)

	@property
	def POB(self):
		return self._POB

	@POB.setter
	def POB(self, value):
		self._POB = value if value is not None else base_types.UninitialisedField(self, 'POB', Max16Text, False)

	@POB.deleter
	def POB(self):
		del self._POB
		self._POB = base_types.UninitialisedField(self, 'POB', Max16Text, False)

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
	def RgnId(self):
		return self._RgnId

	@RgnId.setter
	def RgnId(self, value):
		self._RgnId = value if value is not None else base_types.UninitialisedField(self, 'RgnId', Max35Text, False)

	@RgnId.deleter
	def RgnId(self):
		del self._RgnId
		self._RgnId = base_types.UninitialisedField(self, 'RgnId', Max35Text, False)

	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if value is not None else base_types.UninitialisedField(self, 'Stat', Max35Text, False)

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = base_types.UninitialisedField(self, 'Stat', Max35Text, False)

	@property
	def StrtBldgId(self):
		return self._StrtBldgId

	@StrtBldgId.setter
	def StrtBldgId(self, value):
		self._StrtBldgId = value if value is not None else base_types.UninitialisedField(self, 'StrtBldgId', Max35Text, False)

	@StrtBldgId.deleter
	def StrtBldgId(self):
		del self._StrtBldgId
		self._StrtBldgId = base_types.UninitialisedField(self, 'StrtBldgId', Max35Text, False)

	@property
	def StrtNm(self):
		return self._StrtNm

	@StrtNm.setter
	def StrtNm(self, value):
		self._StrtNm = value if value is not None else base_types.UninitialisedField(self, 'StrtNm', Max35Text, False)

	@StrtNm.deleter
	def StrtNm(self):
		del self._StrtNm
		self._StrtNm = base_types.UninitialisedField(self, 'StrtNm', Max35Text, False)

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
		base_types.FieldEntry(name='BldgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Flr', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POB', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCdId', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stat', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtBldgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))