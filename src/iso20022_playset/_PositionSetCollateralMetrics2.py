# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSetCollateralTotal2

class PositionSetCollateralMetrics2(base_types._BaseFieldType):

	__slots__ = ["_Clean", "_Ttl"]
	@property
	def Clean(self):
		return self._Clean

	@Clean.setter
	def Clean(self, value):
		self._Clean = value if value is not None else base_types.UninitialisedField(self, 'Clean', PositionSetCollateralTotal2, False)

	@Clean.deleter
	def Clean(self):
		del self._Clean
		self._Clean = base_types.UninitialisedField(self, 'Clean', PositionSetCollateralTotal2, False)

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if value is not None else base_types.UninitialisedField(self, 'Ttl', PositionSetCollateralTotal2, False)

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = base_types.UninitialisedField(self, 'Ttl', PositionSetCollateralTotal2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clean', type=PositionSetCollateralTotal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=PositionSetCollateralTotal2, min=0, max=1, mutex_group=None, array=False),
	))