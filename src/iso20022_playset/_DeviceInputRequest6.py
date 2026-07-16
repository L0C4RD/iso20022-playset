# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage11
from . import InputData6

class DeviceInputRequest6(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_InptData"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage11, False)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage11, False)

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if value is not None else base_types.UninitialisedField(self, 'InptData', InputData6, False)

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = base_types.UninitialisedField(self, 'InptData', InputData6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptData', type=InputData6, min=1, max=1, mutex_group=None, array=False),
	))