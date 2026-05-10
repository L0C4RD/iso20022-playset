import base_types
import StandingOrderIdentification8
import StandingOrderOrError10Choice

class StandingOrderReport3(base_types._BaseFieldType):

	__slots__ = ["_StgOrdrOrErr", "_StgOrdrId"]
	@property
	def StgOrdrOrErr(self):
		return self._StgOrdrOrErr

	@StgOrdrOrErr.setter
	def StgOrdrOrErr(self, value):
		self._StgOrdrOrErr = value if type(value) != auto else self.make_default("StgOrdrOrErr")

	@StgOrdrOrErr.deleter
	def StgOrdrOrErr(self):
		del self._StgOrdrOrErr
		self._StgOrdrOrErr = None

	@property
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if type(value) != auto else self.make_default("StgOrdrId")

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StgOrdrOrErr', type=StandingOrderOrError10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrId', type=StandingOrderIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

