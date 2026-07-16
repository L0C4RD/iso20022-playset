# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import ActionType15Code
from . import NetworkParameters7
from . import ProcessRetry3
from . import ProcessTiming6

class Action18(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_MsgToPres", "_RmotAccs", "_Rtry", "_TmCond"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', ActionType15Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', ActionType15Code, False)

	@property
	def MsgToPres(self):
		return self._MsgToPres

	@MsgToPres.setter
	def MsgToPres(self, value):
		self._MsgToPres = value if value is not None else base_types.UninitialisedField(self, 'MsgToPres', ActionMessage12, False)

	@MsgToPres.deleter
	def MsgToPres(self):
		del self._MsgToPres
		self._MsgToPres = base_types.UninitialisedField(self, 'MsgToPres', ActionMessage12, False)

	@property
	def RmotAccs(self):
		return self._RmotAccs

	@RmotAccs.setter
	def RmotAccs(self, value):
		self._RmotAccs = value if value is not None else base_types.UninitialisedField(self, 'RmotAccs', NetworkParameters7, False)

	@RmotAccs.deleter
	def RmotAccs(self):
		del self._RmotAccs
		self._RmotAccs = base_types.UninitialisedField(self, 'RmotAccs', NetworkParameters7, False)

	@property
	def Rtry(self):
		return self._Rtry

	@Rtry.setter
	def Rtry(self, value):
		self._Rtry = value if value is not None else base_types.UninitialisedField(self, 'Rtry', ProcessRetry3, False)

	@Rtry.deleter
	def Rtry(self):
		del self._Rtry
		self._Rtry = base_types.UninitialisedField(self, 'Rtry', ProcessRetry3, False)

	@property
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if value is not None else base_types.UninitialisedField(self, 'TmCond', ProcessTiming6, False)

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = base_types.UninitialisedField(self, 'TmCond', ProcessTiming6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=ActionType15Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToPres', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotAccs', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCond', type=ProcessTiming6, min=0, max=1, mutex_group=None, array=False),
	))