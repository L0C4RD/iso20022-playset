# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActionMessage12 import ActionMessage12
from ._InputData7 import InputData7

class DeviceInputRequest7(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_InptData"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != base_types.auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if type(value) != base_types.auto else self.make_default("InptData")

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptData', type=InputData7, min=1, max=1, mutex_group=None, array=False),
	))