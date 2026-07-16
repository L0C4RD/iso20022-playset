# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import InputData7

class DeviceInputRequest7(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_InptData"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, False)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, False)

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if value is not None else base_types.UninitialisedField(self, 'InptData', InputData7, False)

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = base_types.UninitialisedField(self, 'InptData', InputData7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptData', type=InputData7, min=1, max=1, mutex_group=None, array=False),
	))