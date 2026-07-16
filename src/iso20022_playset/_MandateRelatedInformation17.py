# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType39
from . import ISODate
from . import Max2MBBinary
from . import Max35Text

class MandateRelatedInformation17(base_types._BaseFieldType):

	__slots__ = ["_DtOfSgntr", "_MndtId", "_MndtImg", "_PrtctdMndtImg"]
	@property
	def DtOfSgntr(self):
		return self._DtOfSgntr

	@DtOfSgntr.setter
	def DtOfSgntr(self, value):
		self._DtOfSgntr = value if value is not None else base_types.UninitialisedField(self, 'DtOfSgntr', ISODate, False)

	@DtOfSgntr.deleter
	def DtOfSgntr(self):
		del self._DtOfSgntr
		self._DtOfSgntr = base_types.UninitialisedField(self, 'DtOfSgntr', ISODate, False)

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if value is not None else base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@property
	def MndtImg(self):
		return self._MndtImg

	@MndtImg.setter
	def MndtImg(self, value):
		self._MndtImg = value if value is not None else base_types.UninitialisedField(self, 'MndtImg', Max2MBBinary, False)

	@MndtImg.deleter
	def MndtImg(self):
		del self._MndtImg
		self._MndtImg = base_types.UninitialisedField(self, 'MndtImg', Max2MBBinary, False)

	@property
	def PrtctdMndtImg(self):
		return self._PrtctdMndtImg

	@PrtctdMndtImg.setter
	def PrtctdMndtImg(self, value):
		self._PrtctdMndtImg = value if value is not None else base_types.UninitialisedField(self, 'PrtctdMndtImg', ContentInformationType39, False)

	@PrtctdMndtImg.deleter
	def PrtctdMndtImg(self):
		del self._PrtctdMndtImg
		self._PrtctdMndtImg = base_types.UninitialisedField(self, 'PrtctdMndtImg', ContentInformationType39, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOfSgntr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtImg', type=Max2MBBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdMndtImg', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
	))