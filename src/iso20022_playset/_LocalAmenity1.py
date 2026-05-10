from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .LocationAmenity1Code import LocationAmenity1Code
from .Max35Text import Max35Text

class LocalAmenity1(base_types._BaseFieldType):

	__slots__ = ["_AvlblInd", "_Tp", "_OthrTp"]
	@property
	def AvlblInd(self):
		return self._AvlblInd

	@AvlblInd.setter
	def AvlblInd(self, value):
		self._AvlblInd = value if type(value) != base_types.auto else self.make_default("AvlblInd")

	@AvlblInd.deleter
	def AvlblInd(self):
		del self._AvlblInd
		self._AvlblInd = None

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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LocationAmenity1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

