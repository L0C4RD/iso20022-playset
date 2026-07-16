# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand14
from . import ATMEnvironment7

class ATMDeviceControl3(base_types._BaseFieldType):

	__slots__ = ["_Cmd", "_Envt"]
	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if value is not None else base_types.UninitialisedField(self, 'Cmd', ATMCommand14, True)

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = base_types.UninitialisedField(self, 'Cmd', ATMCommand14, True)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment7, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmd', type=ATMCommand14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
	))