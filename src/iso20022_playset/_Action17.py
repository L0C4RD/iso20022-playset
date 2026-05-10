from . import base_types
from ._NetworkParameters7 import NetworkParameters7
from ._ActionMessage11 import ActionMessage11
from ._ProcessRetry3 import ProcessRetry3
from ._ProcessTiming6 import ProcessTiming6
from ._ActionType15Code import ActionType15Code

class Action17(base_types._BaseFieldType):

	__slots__ = ["_MsgToPres", "_RmotAccs", "_ActnTp", "_TmCond", "_Rtry"]
	@property
	def MsgToPres(self):
		return self._MsgToPres

	@MsgToPres.setter
	def MsgToPres(self, value):
		self._MsgToPres = value if type(value) != base_types.auto else self.make_default("MsgToPres")

	@MsgToPres.deleter
	def MsgToPres(self):
		del self._MsgToPres
		self._MsgToPres = None

	@property
	def RmotAccs(self):
		return self._RmotAccs

	@RmotAccs.setter
	def RmotAccs(self, value):
		self._RmotAccs = value if type(value) != base_types.auto else self.make_default("RmotAccs")

	@RmotAccs.deleter
	def RmotAccs(self):
		del self._RmotAccs
		self._RmotAccs = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if type(value) != base_types.auto else self.make_default("TmCond")

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = None

	@property
	def Rtry(self):
		return self._Rtry

	@Rtry.setter
	def Rtry(self, value):
		self._Rtry = value if type(value) != base_types.auto else self.make_default("Rtry")

	@Rtry.deleter
	def Rtry(self):
		del self._Rtry
		self._Rtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgToPres', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotAccs', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=ActionType15Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCond', type=ProcessTiming6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
	))

