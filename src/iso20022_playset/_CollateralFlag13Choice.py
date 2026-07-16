# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollaterisedData12
from . import NoReasonCode

class CollateralFlag13Choice(base_types._BaseFieldType):

	__slots__ = ["_Collsd", "_Uncollsd"]
	@property
	def Collsd(self):
		return self._Collsd

	@Collsd.setter
	def Collsd(self, value):
		self._Collsd = value if value is not None else base_types.UninitialisedField(self, 'Collsd', CollaterisedData12, False)

	@Collsd.deleter
	def Collsd(self):
		del self._Collsd
		self._Collsd = base_types.UninitialisedField(self, 'Collsd', CollaterisedData12, False)

	@property
	def Uncollsd(self):
		return self._Uncollsd

	@Uncollsd.setter
	def Uncollsd(self, value):
		self._Uncollsd = value if value is not None else base_types.UninitialisedField(self, 'Uncollsd', NoReasonCode, False)

	@Uncollsd.deleter
	def Uncollsd(self):
		del self._Uncollsd
		self._Uncollsd = base_types.UninitialisedField(self, 'Uncollsd', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Collsd', type=CollaterisedData12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Uncollsd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))