import base_types
import Max140Text

class CancelOrderReport1(base_types._BaseFieldType):

	__slots__ = ["_RptId"]
	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

