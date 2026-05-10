from . import base_types
from .Mandate22 import Mandate22
from .Max35Text import Max35Text

class OriginalMandate11Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMndt", "_OrgnlMndtId"]
	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if type(value) != base_types.auto else self.make_default("OrgnlMndt")

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = None

	@property
	def OrgnlMndtId(self):
		return self._OrgnlMndtId

	@OrgnlMndtId.setter
	def OrgnlMndtId(self, value):
		self._OrgnlMndtId = value if type(value) != base_types.auto else self.make_default("OrgnlMndtId")

	@OrgnlMndtId.deleter
	def OrgnlMndtId(self):
		del self._OrgnlMndtId
		self._OrgnlMndtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMndt', type=Mandate22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlMndtId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

