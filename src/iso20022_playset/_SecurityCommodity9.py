# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Commodity43 import Commodity43
from ._Security51 import Security51

class SecurityCommodity9(base_types._BaseFieldType):

	__slots__ = ["_Cmmdty", "_Scty"]
	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != base_types.auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != base_types.auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmmdty', type=Commodity43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=Security51, min=0, max=None, mutex_group=None, array=True),
	))