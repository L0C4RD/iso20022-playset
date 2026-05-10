import base_types
import ShipmentDateRange2
import ShipmentDateRange1

class ShipmentSchedule2Choice(base_types._BaseFieldType):

	__slots__ = ["_ShipmntDtRg", "_ShipmntSubSchdl"]
	@property
	def ShipmntDtRg(self):
		return self._ShipmntDtRg

	@ShipmntDtRg.setter
	def ShipmntDtRg(self, value):
		self._ShipmntDtRg = value if type(value) != auto else self.make_default("ShipmntDtRg")

	@ShipmntDtRg.deleter
	def ShipmntDtRg(self):
		del self._ShipmntDtRg
		self._ShipmntDtRg = None

	@property
	def ShipmntSubSchdl(self):
		return self._ShipmntSubSchdl

	@ShipmntSubSchdl.setter
	def ShipmntSubSchdl(self, value):
		self._ShipmntSubSchdl = value if type(value) != auto else self.make_default("ShipmntSubSchdl")

	@ShipmntSubSchdl.deleter
	def ShipmntSubSchdl(self):
		del self._ShipmntSubSchdl
		self._ShipmntSubSchdl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShipmntDtRg', type=ShipmentDateRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShipmntSubSchdl', type=ShipmentDateRange2, min=2, max=None, mutex_group=1, array=True),
	))

