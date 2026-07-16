# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationCharacteristics5
from . import CryptographicKey18
from . import MemoryCharacteristics1
from . import Number

class PointOfInteractionComponentCharacteristics10(base_types._BaseFieldType):

	__slots__ = ["_Com", "_Mmry", "_SbcbrIdntyMdls", "_SctyAccsMdls", "_SctyElmt"]
	@property
	def Com(self):
		return self._Com

	@Com.setter
	def Com(self, value):
		self._Com = value if value is not None else base_types.UninitialisedField(self, 'Com', CommunicationCharacteristics5, True)

	@Com.deleter
	def Com(self):
		del self._Com
		self._Com = base_types.UninitialisedField(self, 'Com', CommunicationCharacteristics5, True)

	@property
	def Mmry(self):
		return self._Mmry

	@Mmry.setter
	def Mmry(self, value):
		self._Mmry = value if value is not None else base_types.UninitialisedField(self, 'Mmry', MemoryCharacteristics1, True)

	@Mmry.deleter
	def Mmry(self):
		del self._Mmry
		self._Mmry = base_types.UninitialisedField(self, 'Mmry', MemoryCharacteristics1, True)

	@property
	def SbcbrIdntyMdls(self):
		return self._SbcbrIdntyMdls

	@SbcbrIdntyMdls.setter
	def SbcbrIdntyMdls(self, value):
		self._SbcbrIdntyMdls = value if value is not None else base_types.UninitialisedField(self, 'SbcbrIdntyMdls', Number, False)

	@SbcbrIdntyMdls.deleter
	def SbcbrIdntyMdls(self):
		del self._SbcbrIdntyMdls
		self._SbcbrIdntyMdls = base_types.UninitialisedField(self, 'SbcbrIdntyMdls', Number, False)

	@property
	def SctyAccsMdls(self):
		return self._SctyAccsMdls

	@SctyAccsMdls.setter
	def SctyAccsMdls(self, value):
		self._SctyAccsMdls = value if value is not None else base_types.UninitialisedField(self, 'SctyAccsMdls', Number, False)

	@SctyAccsMdls.deleter
	def SctyAccsMdls(self):
		del self._SctyAccsMdls
		self._SctyAccsMdls = base_types.UninitialisedField(self, 'SctyAccsMdls', Number, False)

	@property
	def SctyElmt(self):
		return self._SctyElmt

	@SctyElmt.setter
	def SctyElmt(self, value):
		self._SctyElmt = value if value is not None else base_types.UninitialisedField(self, 'SctyElmt', CryptographicKey18, True)

	@SctyElmt.deleter
	def SctyElmt(self):
		del self._SctyElmt
		self._SctyElmt = base_types.UninitialisedField(self, 'SctyElmt', CryptographicKey18, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Com', type=CommunicationCharacteristics5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mmry', type=MemoryCharacteristics1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbcbrIdntyMdls', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyAccsMdls', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyElmt', type=CryptographicKey18, min=0, max=None, mutex_group=None, array=True),
	))