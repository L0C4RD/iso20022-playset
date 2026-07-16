# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import SecuredCollateral2Choice
from . import SpecialCollateral2Code

class Collateral18(base_types._BaseFieldType):

	__slots__ = ["_Hrcut", "_SpclCollInd", "_Valtn"]
	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@property
	def SpclCollInd(self):
		return self._SpclCollInd

	@SpclCollInd.setter
	def SpclCollInd(self, value):
		self._SpclCollInd = value if value is not None else base_types.UninitialisedField(self, 'SpclCollInd', SpecialCollateral2Code, False)

	@SpclCollInd.deleter
	def SpclCollInd(self):
		del self._SpclCollInd
		self._SpclCollInd = base_types.UninitialisedField(self, 'SpclCollInd', SpecialCollateral2Code, False)

	@property
	def Valtn(self):
		return self._Valtn

	@Valtn.setter
	def Valtn(self, value):
		self._Valtn = value if value is not None else base_types.UninitialisedField(self, 'Valtn', SecuredCollateral2Choice, False)

	@Valtn.deleter
	def Valtn(self):
		del self._Valtn
		self._Valtn = base_types.UninitialisedField(self, 'Valtn', SecuredCollateral2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCollInd', type=SpecialCollateral2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Valtn', type=SecuredCollateral2Choice, min=1, max=1, mutex_group=None, array=False),
	))