# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShipmentDateRange1
from . import ShipmentDateRange2

class ShipmentSchedule2Choice(base_types._BaseFieldType):

	__slots__ = ["_ShipmntDtRg", "_ShipmntSubSchdl"]
	@property
	def ShipmntDtRg(self):
		return self._ShipmntDtRg

	@ShipmntDtRg.setter
	def ShipmntDtRg(self, value):
		self._ShipmntDtRg = value if value is not None else base_types.UninitialisedField(self, 'ShipmntDtRg', ShipmentDateRange1, False)

	@ShipmntDtRg.deleter
	def ShipmntDtRg(self):
		del self._ShipmntDtRg
		self._ShipmntDtRg = base_types.UninitialisedField(self, 'ShipmntDtRg', ShipmentDateRange1, False)

	@property
	def ShipmntSubSchdl(self):
		return self._ShipmntSubSchdl

	@ShipmntSubSchdl.setter
	def ShipmntSubSchdl(self, value):
		self._ShipmntSubSchdl = value if value is not None else base_types.UninitialisedField(self, 'ShipmntSubSchdl', ShipmentDateRange2, True)

	@ShipmntSubSchdl.deleter
	def ShipmntSubSchdl(self):
		del self._ShipmntSubSchdl
		self._ShipmntSubSchdl = base_types.UninitialisedField(self, 'ShipmntSubSchdl', ShipmentDateRange2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShipmntDtRg', type=ShipmentDateRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShipmntSubSchdl', type=ShipmentDateRange2, min=2, max=None, mutex_group=1, array=True),
	))