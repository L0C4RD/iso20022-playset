# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import SystemIdentification2Choice

class SystemAndCurrency1(base_types._BaseFieldType):

	__slots__ = ["_SysCcy", "_SysId"]
	@property
	def SysCcy(self):
		return self._SysCcy

	@SysCcy.setter
	def SysCcy(self, value):
		self._SysCcy = value if value is not None else base_types.UninitialisedField(self, 'SysCcy', ActiveCurrencyCode, False)

	@SysCcy.deleter
	def SysCcy(self):
		del self._SysCcy
		self._SysCcy = base_types.UninitialisedField(self, 'SysCcy', ActiveCurrencyCode, False)

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
	))