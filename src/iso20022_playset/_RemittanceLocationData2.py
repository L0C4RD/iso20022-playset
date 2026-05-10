from . import base_types
from ._Max2048Text import Max2048Text
from ._NameAndAddress18 import NameAndAddress18
from ._RemittanceLocationMethod2Code import RemittanceLocationMethod2Code

class RemittanceLocationData2(base_types._BaseFieldType):

	__slots__ = ["_ElctrncAdr", "_Mtd", "_PstlAdr"]
	@property
	def ElctrncAdr(self):
		return self._ElctrncAdr

	@ElctrncAdr.setter
	def ElctrncAdr(self, value):
		self._ElctrncAdr = value if type(value) != base_types.auto else self.make_default("ElctrncAdr")

	@ElctrncAdr.deleter
	def ElctrncAdr(self):
		del self._ElctrncAdr
		self._ElctrncAdr = None

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != base_types.auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=RemittanceLocationMethod2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
	))

