from . import base_types
from ._PlaceOfPresentation1 import PlaceOfPresentation1
from ._PresentationParty1Code import PresentationParty1Code

class PlaceOrUnderConfirmationChoice1(base_types._BaseFieldType):

	__slots__ = ["_PresntnUdrConf", "_PlcOfPresntn"]
	@property
	def PlcOfPresntn(self):
		return self._PlcOfPresntn

	@PlcOfPresntn.setter
	def PlcOfPresntn(self, value):
		self._PlcOfPresntn = value if type(value) != base_types.auto else self.make_default("PlcOfPresntn")

	@PlcOfPresntn.deleter
	def PlcOfPresntn(self):
		del self._PlcOfPresntn
		self._PlcOfPresntn = None

	@property
	def PresntnUdrConf(self):
		return self._PresntnUdrConf

	@PresntnUdrConf.setter
	def PresntnUdrConf(self, value):
		self._PresntnUdrConf = value if type(value) != base_types.auto else self.make_default("PresntnUdrConf")

	@PresntnUdrConf.deleter
	def PresntnUdrConf(self):
		del self._PresntnUdrConf
		self._PresntnUdrConf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfPresntn', type=PlaceOfPresentation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PresntnUdrConf', type=PresentationParty1Code, min=0, max=1, mutex_group=1, array=False),
	))

