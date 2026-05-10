import base_types
import TrueFalseIndicator

class LogoutRequest1(base_types._BaseFieldType):

	__slots__ = ["_MntncAllwd"]
	@property
	def MntncAllwd(self):
		return self._MntncAllwd

	@MntncAllwd.setter
	def MntncAllwd(self, value):
		self._MntncAllwd = value if type(value) != auto else self.make_default("MntncAllwd")

	@MntncAllwd.deleter
	def MntncAllwd(self):
		del self._MntncAllwd
		self._MntncAllwd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MntncAllwd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

