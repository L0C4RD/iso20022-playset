from . import base_types
from .AdjustmentType2Code import AdjustmentType2Code
from .Max35Text import Max35Text

class AdjustmentType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_OthrAdjstmntTp"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def OthrAdjstmntTp(self):
		return self._OthrAdjstmntTp

	@OthrAdjstmntTp.setter
	def OthrAdjstmntTp(self, value):
		self._OthrAdjstmntTp = value if type(value) != base_types.auto else self.make_default("OthrAdjstmntTp")

	@OthrAdjstmntTp.deleter
	def OthrAdjstmntTp(self):
		del self._OthrAdjstmntTp
		self._OthrAdjstmntTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=AdjustmentType2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrAdjstmntTp', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

