# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Commodity43
from . import Security51

class SecurityCommodity9(base_types._BaseFieldType):

	__slots__ = ["_Cmmdty", "_Scty"]
	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', Commodity43, True)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', Commodity43, True)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', Security51, True)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', Security51, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmmdty', type=Commodity43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=Security51, min=0, max=None, mutex_group=None, array=True),
	))