# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashCompare3
from . import Commodity42
from . import Security48

class SecurityCommodityCash4(base_types._BaseFieldType):

	__slots__ = ["_Cmmdty", "_Csh", "_Scty"]
	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', Commodity42, True)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', Commodity42, True)

	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if value is not None else base_types.UninitialisedField(self, 'Csh', CashCompare3, True)

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = base_types.UninitialisedField(self, 'Csh', CashCompare3, True)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', Security48, True)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', Security48, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmmdty', type=Commodity42, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Csh', type=CashCompare3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=Security48, min=0, max=None, mutex_group=None, array=True),
	))