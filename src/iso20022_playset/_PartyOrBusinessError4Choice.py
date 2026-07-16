# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling4
from . import SystemParty6

class PartyOrBusinessError4Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_SysPty"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling4, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling4, True)

	@property
	def SysPty(self):
		return self._SysPty

	@SysPty.setter
	def SysPty(self, value):
		self._SysPty = value if value is not None else base_types.UninitialisedField(self, 'SysPty', SystemParty6, False)

	@SysPty.deleter
	def SysPty(self):
		del self._SysPty
		self._SysPty = base_types.UninitialisedField(self, 'SysPty', SystemParty6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SysPty', type=SystemParty6, min=0, max=1, mutex_group=1, array=False),
	))