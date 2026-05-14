# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Exact2NumericText import Exact2NumericText
from ._Frequency6Code import Frequency6Code

class FrequencyAndMoment1(base_types._BaseFieldType):

	__slots__ = ["_PtInTm", "_Tp"]
	@property
	def PtInTm(self):
		return self._PtInTm

	@PtInTm.setter
	def PtInTm(self, value):
		self._PtInTm = value if type(value) != base_types.auto else self.make_default("PtInTm")

	@PtInTm.deleter
	def PtInTm(self):
		del self._PtInTm
		self._PtInTm = None

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
		base_types.FieldEntry(name='PtInTm', type=Exact2NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Frequency6Code, min=1, max=1, mutex_group=None, array=False),
	))