import base_types
import Max8HexBinaryText
import MACData1

class ContentInformationType41(base_types._BaseFieldType):

	__slots__ = ["_MACData", "_MAC"]
	@property
	def MACData(self):
		return self._MACData

	@MACData.setter
	def MACData(self, value):
		self._MACData = value if type(value) != auto else self.make_default("MACData")

	@MACData.deleter
	def MACData(self):
		del self._MACData
		self._MACData = None

	@property
	def MAC(self):
		return self._MAC

	@MAC.setter
	def MAC(self, value):
		self._MAC = value if type(value) != auto else self.make_default("MAC")

	@MAC.deleter
	def MAC(self):
		del self._MAC
		self._MAC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MACData', type=MACData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MAC', type=Max8HexBinaryText, min=1, max=1, mutex_group=None, array=False),
	))

