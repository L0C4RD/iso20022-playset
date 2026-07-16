# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashReuseData1
from . import SecurityReuseData1

class CollateralType19(base_types._BaseFieldType):

	__slots__ = ["_Csh", "_Scty"]
	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if value is not None else base_types.UninitialisedField(self, 'Csh', CashReuseData1, True)

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = base_types.UninitialisedField(self, 'Csh', CashReuseData1, True)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', SecurityReuseData1, True)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', SecurityReuseData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Csh', type=CashReuseData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=SecurityReuseData1, min=0, max=None, mutex_group=None, array=True),
	))