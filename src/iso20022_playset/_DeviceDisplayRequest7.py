# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12

class DeviceDisplayRequest7(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, True)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=1, max=None, mutex_group=None, array=True),
	))