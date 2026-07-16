# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import Number

class DevicePoweroffCardReaderRequest7(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_PwrOffMaxWtgTm"]
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
	def PwrOffMaxWtgTm(self):
		return self._PwrOffMaxWtgTm

	@PwrOffMaxWtgTm.setter
	def PwrOffMaxWtgTm(self, value):
		self._PwrOffMaxWtgTm = value if value is not None else base_types.UninitialisedField(self, 'PwrOffMaxWtgTm', Number, False)

	@PwrOffMaxWtgTm.deleter
	def PwrOffMaxWtgTm(self):
		del self._PwrOffMaxWtgTm
		self._PwrOffMaxWtgTm = base_types.UninitialisedField(self, 'PwrOffMaxWtgTm', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PwrOffMaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
	))