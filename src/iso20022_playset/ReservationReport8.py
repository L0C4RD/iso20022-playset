import base_types
import ReservationOrError9Choice
import ReservationIdentification4

class ReservationReport8(base_types._BaseFieldType):

	__slots__ = ["_RsvatnId", "_RsvatnOrErr"]
	@property
	def RsvatnId(self):
		return self._RsvatnId

	@RsvatnId.setter
	def RsvatnId(self, value):
		self._RsvatnId = value if type(value) != auto else self.make_default("RsvatnId")

	@RsvatnId.deleter
	def RsvatnId(self):
		del self._RsvatnId
		self._RsvatnId = None

	@property
	def RsvatnOrErr(self):
		return self._RsvatnOrErr

	@RsvatnOrErr.setter
	def RsvatnOrErr(self, value):
		self._RsvatnOrErr = value if type(value) != auto else self.make_default("RsvatnOrErr")

	@RsvatnOrErr.deleter
	def RsvatnOrErr(self):
		del self._RsvatnOrErr
		self._RsvatnOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsvatnId', type=ReservationIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnOrErr', type=ReservationOrError9Choice, min=1, max=1, mutex_group=None, array=False),
	))

