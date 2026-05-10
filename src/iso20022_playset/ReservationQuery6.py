import base_types
import QueryType2Code
import ReservationCriteria6Choice

class ReservationQuery6(base_types._BaseFieldType):

	__slots__ = ["_RsvatnCrit", "_QryTp"]
	@property
	def RsvatnCrit(self):
		return self._RsvatnCrit

	@RsvatnCrit.setter
	def RsvatnCrit(self, value):
		self._RsvatnCrit = value if type(value) != auto else self.make_default("RsvatnCrit")

	@RsvatnCrit.deleter
	def RsvatnCrit(self):
		del self._RsvatnCrit
		self._RsvatnCrit = None

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsvatnCrit', type=ReservationCriteria6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))

