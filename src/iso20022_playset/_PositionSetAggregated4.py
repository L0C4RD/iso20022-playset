# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import PositionSet21
from . import PositionSet22

class PositionSetAggregated4(base_types._BaseFieldType):

	__slots__ = ["_CcyCollPosSet", "_CcyPosSet", "_CollPosSet", "_PosSet", "_RefDt"]
	@property
	def CcyCollPosSet(self):
		return self._CcyCollPosSet

	@CcyCollPosSet.setter
	def CcyCollPosSet(self, value):
		self._CcyCollPosSet = value if value is not None else base_types.UninitialisedField(self, 'CcyCollPosSet', PositionSet22, True)

	@CcyCollPosSet.deleter
	def CcyCollPosSet(self):
		del self._CcyCollPosSet
		self._CcyCollPosSet = base_types.UninitialisedField(self, 'CcyCollPosSet', PositionSet22, True)

	@property
	def CcyPosSet(self):
		return self._CcyPosSet

	@CcyPosSet.setter
	def CcyPosSet(self, value):
		self._CcyPosSet = value if value is not None else base_types.UninitialisedField(self, 'CcyPosSet', PositionSet21, True)

	@CcyPosSet.deleter
	def CcyPosSet(self):
		del self._CcyPosSet
		self._CcyPosSet = base_types.UninitialisedField(self, 'CcyPosSet', PositionSet21, True)

	@property
	def CollPosSet(self):
		return self._CollPosSet

	@CollPosSet.setter
	def CollPosSet(self, value):
		self._CollPosSet = value if value is not None else base_types.UninitialisedField(self, 'CollPosSet', PositionSet22, True)

	@CollPosSet.deleter
	def CollPosSet(self):
		del self._CollPosSet
		self._CollPosSet = base_types.UninitialisedField(self, 'CollPosSet', PositionSet22, True)

	@property
	def PosSet(self):
		return self._PosSet

	@PosSet.setter
	def PosSet(self, value):
		self._PosSet = value if value is not None else base_types.UninitialisedField(self, 'PosSet', PositionSet21, True)

	@PosSet.deleter
	def PosSet(self):
		del self._PosSet
		self._PosSet = base_types.UninitialisedField(self, 'PosSet', PositionSet21, True)

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if value is not None else base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyCollPosSet', type=PositionSet22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyPosSet', type=PositionSet21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CollPosSet', type=PositionSet22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PosSet', type=PositionSet21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))