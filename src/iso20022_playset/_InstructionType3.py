# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstructionType3Code

class InstructionType3(base_types._BaseFieldType):

	__slots__ = ["_Tp"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', InstructionType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', InstructionType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=InstructionType3Code, min=1, max=1, mutex_group=None, array=False),
	))