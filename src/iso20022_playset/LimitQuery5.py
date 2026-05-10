import base_types
import QueryType2Code
import LimitCriteria7Choice

class LimitQuery5(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_LmtCrit"]
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

	@property
	def LmtCrit(self):
		return self._LmtCrit

	@LmtCrit.setter
	def LmtCrit(self, value):
		self._LmtCrit = value if type(value) != auto else self.make_default("LmtCrit")

	@LmtCrit.deleter
	def LmtCrit(self):
		del self._LmtCrit
		self._LmtCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtCrit', type=LimitCriteria7Choice, min=0, max=1, mutex_group=None, array=False),
	))

