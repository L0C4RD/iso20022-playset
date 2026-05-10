from . import base_types
from .PositionSet22 import PositionSet22
from .PositionSet21 import PositionSet21
from .ISODate import ISODate

class PositionSetAggregated4(base_types._BaseFieldType):

	__slots__ = ["_CollPosSet", "_CcyPosSet", "_RefDt", "_PosSet", "_CcyCollPosSet"]
	@property
	def CollPosSet(self):
		return self._CollPosSet

	@CollPosSet.setter
	def CollPosSet(self, value):
		self._CollPosSet = value if type(value) != base_types.auto else self.make_default("CollPosSet")

	@CollPosSet.deleter
	def CollPosSet(self):
		del self._CollPosSet
		self._CollPosSet = None

	@property
	def CcyPosSet(self):
		return self._CcyPosSet

	@CcyPosSet.setter
	def CcyPosSet(self, value):
		self._CcyPosSet = value if type(value) != base_types.auto else self.make_default("CcyPosSet")

	@CcyPosSet.deleter
	def CcyPosSet(self):
		del self._CcyPosSet
		self._CcyPosSet = None

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if type(value) != base_types.auto else self.make_default("RefDt")

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = None

	@property
	def PosSet(self):
		return self._PosSet

	@PosSet.setter
	def PosSet(self, value):
		self._PosSet = value if type(value) != base_types.auto else self.make_default("PosSet")

	@PosSet.deleter
	def PosSet(self):
		del self._PosSet
		self._PosSet = None

	@property
	def CcyCollPosSet(self):
		return self._CcyCollPosSet

	@CcyCollPosSet.setter
	def CcyCollPosSet(self, value):
		self._CcyCollPosSet = value if type(value) != base_types.auto else self.make_default("CcyCollPosSet")

	@CcyCollPosSet.deleter
	def CcyCollPosSet(self):
		del self._CcyCollPosSet
		self._CcyCollPosSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPosSet', type=PositionSet22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyPosSet', type=PositionSet21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosSet', type=PositionSet21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyCollPosSet', type=PositionSet22, min=0, max=None, mutex_group=None, array=True),
	))

