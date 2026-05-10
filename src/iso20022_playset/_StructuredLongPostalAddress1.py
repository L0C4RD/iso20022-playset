from . import base_types
from .Max35Text import Max35Text
from .Max16Text import Max16Text
from .CountryCode import CountryCode

class StructuredLongPostalAddress1(base_types._BaseFieldType):

	__slots__ = ["_DstrctNm", "_Stat", "_Flr", "_StrtNm", "_BldgNm", "_CtyId", "_TwnNm", "_StrtBldgId", "_POB", "_PstCdId", "_RgnId", "_Ctry"]
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
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if type(value) != base_types.auto else self.make_default("Stat")

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = None

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
	def CtyId(self):
		return self._CtyId

	@CtyId.setter
	def CtyId(self, value):
		self._CtyId = value if type(value) != base_types.auto else self.make_default("CtyId")

	@CtyId.deleter
	def CtyId(self):
		del self._CtyId
		self._CtyId = None

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
	def StrtBldgId(self):
		return self._StrtBldgId

	@StrtBldgId.setter
	def StrtBldgId(self, value):
		self._StrtBldgId = value if type(value) != base_types.auto else self.make_default("StrtBldgId")

	@StrtBldgId.deleter
	def StrtBldgId(self):
		del self._StrtBldgId
		self._StrtBldgId = None

	@property
	def POB(self):
		return self._POB

	@POB.setter
	def POB(self, value):
		self._POB = value if type(value) != base_types.auto else self.make_default("POB")

	@POB.deleter
	def POB(self):
		del self._POB
		self._POB = None

	@property
	def PstCdId(self):
		return self._PstCdId

	@PstCdId.setter
	def PstCdId(self, value):
		self._PstCdId = value if type(value) != base_types.auto else self.make_default("PstCdId")

	@PstCdId.deleter
	def PstCdId(self):
		del self._PstCdId
		self._PstCdId = None

	@property
	def RgnId(self):
		return self._RgnId

	@RgnId.setter
	def RgnId(self, value):
		self._RgnId = value if type(value) != base_types.auto else self.make_default("RgnId")

	@RgnId.deleter
	def RgnId(self):
		del self._RgnId
		self._RgnId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DstrctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stat', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Flr', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BldgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrtBldgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POB', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCdId', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

