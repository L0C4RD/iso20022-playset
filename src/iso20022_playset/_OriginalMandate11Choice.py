# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Mandate22
from . import Max35Text

class OriginalMandate11Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMndt", "_OrgnlMndtId"]
	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMndt', Mandate22, False)

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = base_types.UninitialisedField(self, 'OrgnlMndt', Mandate22, False)

	@property
	def OrgnlMndtId(self):
		return self._OrgnlMndtId

	@OrgnlMndtId.setter
	def OrgnlMndtId(self, value):
		self._OrgnlMndtId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMndtId', Max35Text, False)

	@OrgnlMndtId.deleter
	def OrgnlMndtId(self):
		del self._OrgnlMndtId
		self._OrgnlMndtId = base_types.UninitialisedField(self, 'OrgnlMndtId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMndt', type=Mandate22, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlMndtId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))