from . import base_types
from .OnLinePIN11 import OnLinePIN11

class DeviceSecureInputResponse6(base_types._BaseFieldType):

	__slots__ = ["_CrdhldrPIN"]
	@property
	def CrdhldrPIN(self):
		return self._CrdhldrPIN

	@CrdhldrPIN.setter
	def CrdhldrPIN(self, value):
		self._CrdhldrPIN = value if type(value) != auto else self.make_default("CrdhldrPIN")

	@CrdhldrPIN.deleter
	def CrdhldrPIN(self):
		del self._CrdhldrPIN
		self._CrdhldrPIN = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrdhldrPIN', type=OnLinePIN11, min=0, max=1, mutex_group=None, array=False),
	))

