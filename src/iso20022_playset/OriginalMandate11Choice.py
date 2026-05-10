import base_types
import Max35Text
import Mandate22

class OriginalMandate11Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMndtId", "_OrgnlMndt"]
	@property
	def OrgnlMndtId(self):
		return self._OrgnlMndtId

	@OrgnlMndtId.setter
	def OrgnlMndtId(self, value):
		self._OrgnlMndtId = value if type(value) != auto else self.make_default("OrgnlMndtId")

	@OrgnlMndtId.deleter
	def OrgnlMndtId(self):
		del self._OrgnlMndtId
		self._OrgnlMndtId = None

	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if type(value) != auto else self.make_default("OrgnlMndt")

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMndtId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlMndt', type=Mandate22, min=0, max=1, mutex_group=1, array=False),
	))

