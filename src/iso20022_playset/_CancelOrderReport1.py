# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text

class CancelOrderReport1(base_types._BaseFieldType):

	__slots__ = ["_RptId"]
	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max140Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))