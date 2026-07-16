# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LocationAmenity2Code
from . import TrueFalseIndicator

class LocalAmenity2(base_types._BaseFieldType):

	__slots__ = ["_AvlblInd", "_Tp"]
	@property
	def AvlblInd(self):
		return self._AvlblInd

	@AvlblInd.setter
	def AvlblInd(self, value):
		self._AvlblInd = value if value is not None else base_types.UninitialisedField(self, 'AvlblInd', TrueFalseIndicator, False)

	@AvlblInd.deleter
	def AvlblInd(self):
		del self._AvlblInd
		self._AvlblInd = base_types.UninitialisedField(self, 'AvlblInd', TrueFalseIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', LocationAmenity2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', LocationAmenity2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LocationAmenity2Code, min=1, max=1, mutex_group=None, array=False),
	))