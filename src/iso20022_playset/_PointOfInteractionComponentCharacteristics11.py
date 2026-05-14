# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CommunicationCharacteristics5 import CommunicationCharacteristics5
from ._CryptographicKey19 import CryptographicKey19
from ._MemoryCharacteristics1 import MemoryCharacteristics1
from ._Number import Number

class PointOfInteractionComponentCharacteristics11(base_types._BaseFieldType):

	__slots__ = ["_Com", "_Mmry", "_SbcbrIdntyMdls", "_SctyAccsMdls", "_SctyElmt"]
	@property
	def Com(self):
		return self._Com

	@Com.setter
	def Com(self, value):
		self._Com = value if type(value) != base_types.auto else self.make_default("Com")

	@Com.deleter
	def Com(self):
		del self._Com
		self._Com = None

	@property
	def Mmry(self):
		return self._Mmry

	@Mmry.setter
	def Mmry(self, value):
		self._Mmry = value if type(value) != base_types.auto else self.make_default("Mmry")

	@Mmry.deleter
	def Mmry(self):
		del self._Mmry
		self._Mmry = None

	@property
	def SbcbrIdntyMdls(self):
		return self._SbcbrIdntyMdls

	@SbcbrIdntyMdls.setter
	def SbcbrIdntyMdls(self, value):
		self._SbcbrIdntyMdls = value if type(value) != base_types.auto else self.make_default("SbcbrIdntyMdls")

	@SbcbrIdntyMdls.deleter
	def SbcbrIdntyMdls(self):
		del self._SbcbrIdntyMdls
		self._SbcbrIdntyMdls = None

	@property
	def SctyAccsMdls(self):
		return self._SctyAccsMdls

	@SctyAccsMdls.setter
	def SctyAccsMdls(self, value):
		self._SctyAccsMdls = value if type(value) != base_types.auto else self.make_default("SctyAccsMdls")

	@SctyAccsMdls.deleter
	def SctyAccsMdls(self):
		del self._SctyAccsMdls
		self._SctyAccsMdls = None

	@property
	def SctyElmt(self):
		return self._SctyElmt

	@SctyElmt.setter
	def SctyElmt(self, value):
		self._SctyElmt = value if type(value) != base_types.auto else self.make_default("SctyElmt")

	@SctyElmt.deleter
	def SctyElmt(self):
		del self._SctyElmt
		self._SctyElmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Com', type=CommunicationCharacteristics5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mmry', type=MemoryCharacteristics1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbcbrIdntyMdls', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyAccsMdls', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyElmt', type=CryptographicKey19, min=0, max=None, mutex_group=None, array=True),
	))