# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SwapType1Code import SwapType1Code
from ._UnderlyingInterestRateType3Code import UnderlyingInterestRateType3Code

class InterestRateDerivative2Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_SwpRltd"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def SwpRltd(self):
		return self._SwpRltd

	@SwpRltd.setter
	def SwpRltd(self, value):
		self._SwpRltd = value if type(value) != base_types.auto else self.make_default("SwpRltd")

	@SwpRltd.deleter
	def SwpRltd(self):
		del self._SwpRltd
		self._SwpRltd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=UnderlyingInterestRateType3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SwpRltd', type=SwapType1Code, min=0, max=1, mutex_group=1, array=False),
	))