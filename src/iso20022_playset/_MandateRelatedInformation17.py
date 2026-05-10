from . import base_types
from .Max35Text import Max35Text
from .ContentInformationType39 import ContentInformationType39
from .Max2MBBinary import Max2MBBinary
from .ISODate import ISODate

class MandateRelatedInformation17(base_types._BaseFieldType):

	__slots__ = ["_PrtctdMndtImg", "_MndtImg", "_MndtId", "_DtOfSgntr"]
	@property
	def PrtctdMndtImg(self):
		return self._PrtctdMndtImg

	@PrtctdMndtImg.setter
	def PrtctdMndtImg(self, value):
		self._PrtctdMndtImg = value if type(value) != base_types.auto else self.make_default("PrtctdMndtImg")

	@PrtctdMndtImg.deleter
	def PrtctdMndtImg(self):
		del self._PrtctdMndtImg
		self._PrtctdMndtImg = None

	@property
	def MndtImg(self):
		return self._MndtImg

	@MndtImg.setter
	def MndtImg(self, value):
		self._MndtImg = value if type(value) != base_types.auto else self.make_default("MndtImg")

	@MndtImg.deleter
	def MndtImg(self):
		del self._MndtImg
		self._MndtImg = None

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if type(value) != base_types.auto else self.make_default("MndtId")

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = None

	@property
	def DtOfSgntr(self):
		return self._DtOfSgntr

	@DtOfSgntr.setter
	def DtOfSgntr(self, value):
		self._DtOfSgntr = value if type(value) != base_types.auto else self.make_default("DtOfSgntr")

	@DtOfSgntr.deleter
	def DtOfSgntr(self):
		del self._DtOfSgntr
		self._DtOfSgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdMndtImg', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtImg', type=Max2MBBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfSgntr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

