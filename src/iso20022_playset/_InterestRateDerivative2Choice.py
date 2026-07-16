# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SwapType1Code
from . import UnderlyingInterestRateType3Code

class InterestRateDerivative2Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_SwpRltd"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', UnderlyingInterestRateType3Code, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', UnderlyingInterestRateType3Code, False)

	@property
	def SwpRltd(self):
		return self._SwpRltd

	@SwpRltd.setter
	def SwpRltd(self, value):
		self._SwpRltd = value if value is not None else base_types.UninitialisedField(self, 'SwpRltd', SwapType1Code, False)

	@SwpRltd.deleter
	def SwpRltd(self):
		del self._SwpRltd
		self._SwpRltd = base_types.UninitialisedField(self, 'SwpRltd', SwapType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=UnderlyingInterestRateType3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SwpRltd', type=SwapType1Code, min=0, max=1, mutex_group=1, array=False),
	))