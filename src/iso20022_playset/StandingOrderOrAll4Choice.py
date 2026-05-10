from . import base_types
import StandingOrderIdentification8
import StandingOrderIdentification9

class StandingOrderOrAll4Choice(base_types._BaseFieldType):

	__slots__ = ["_StgOrdr", "_AllStgOrdrs"]
	@property
	def StgOrdr(self):
		return self._StgOrdr

	@StgOrdr.setter
	def StgOrdr(self, value):
		self._StgOrdr = value if type(value) != auto else self.make_default("StgOrdr")

	@StgOrdr.deleter
	def StgOrdr(self):
		del self._StgOrdr
		self._StgOrdr = None

	@property
	def AllStgOrdrs(self):
		return self._AllStgOrdrs

	@AllStgOrdrs.setter
	def AllStgOrdrs(self, value):
		self._AllStgOrdrs = value if type(value) != auto else self.make_default("AllStgOrdrs")

	@AllStgOrdrs.deleter
	def AllStgOrdrs(self):
		del self._AllStgOrdrs
		self._AllStgOrdrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StgOrdr', type=StandingOrderIdentification8, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='AllStgOrdrs', type=StandingOrderIdentification9, min=1, max=None, mutex_group=1, array=True),
	))

