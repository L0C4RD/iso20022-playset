# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtorActivation5
from . import Party53Choice

class OriginalActivation3Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlActvtnData", "_OrgnlDbtrId"]
	@property
	def OrgnlActvtnData(self):
		return self._OrgnlActvtnData

	@OrgnlActvtnData.setter
	def OrgnlActvtnData(self, value):
		self._OrgnlActvtnData = value if value is not None else base_types.UninitialisedField(self, 'OrgnlActvtnData', DebtorActivation5, False)

	@OrgnlActvtnData.deleter
	def OrgnlActvtnData(self):
		del self._OrgnlActvtnData
		self._OrgnlActvtnData = base_types.UninitialisedField(self, 'OrgnlActvtnData', DebtorActivation5, False)

	@property
	def OrgnlDbtrId(self):
		return self._OrgnlDbtrId

	@OrgnlDbtrId.setter
	def OrgnlDbtrId(self, value):
		self._OrgnlDbtrId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDbtrId', Party53Choice, False)

	@OrgnlDbtrId.deleter
	def OrgnlDbtrId(self):
		del self._OrgnlDbtrId
		self._OrgnlDbtrId = base_types.UninitialisedField(self, 'OrgnlDbtrId', Party53Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlActvtnData', type=DebtorActivation5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlDbtrId', type=Party53Choice, min=0, max=1, mutex_group=1, array=False),
	))