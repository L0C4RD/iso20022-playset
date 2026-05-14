# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LocationAmenity2Code import LocationAmenity2Code
from ._TrueFalseIndicator import TrueFalseIndicator

class LocalAmenity2(base_types._BaseFieldType):

	__slots__ = ["_AvlblInd", "_Tp"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LocationAmenity2Code, min=1, max=1, mutex_group=None, array=False),
	))