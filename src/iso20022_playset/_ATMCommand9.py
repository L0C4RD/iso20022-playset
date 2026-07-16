# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand5Code
from . import ATMCommandIdentification1

class ATMCommand9(base_types._BaseFieldType):

	__slots__ = ["_CmdId", "_Tp"]
	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if value is not None else base_types.UninitialisedField(self, 'CmdId', ATMCommandIdentification1, False)

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = base_types.UninitialisedField(self, 'CmdId', ATMCommandIdentification1, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ATMCommand5Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ATMCommand5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCommand5Code, min=1, max=1, mutex_group=None, array=False),
	))