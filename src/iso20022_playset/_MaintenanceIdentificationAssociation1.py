# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class MaintenanceIdentificationAssociation1(base_types._BaseFieldType):

	__slots__ = ["_MstrTMId", "_TMId"]
	@property
	def MstrTMId(self):
		return self._MstrTMId

	@MstrTMId.setter
	def MstrTMId(self, value):
		self._MstrTMId = value if value is not None else base_types.UninitialisedField(self, 'MstrTMId', Max35Text, False)

	@MstrTMId.deleter
	def MstrTMId(self):
		del self._MstrTMId
		self._MstrTMId = base_types.UninitialisedField(self, 'MstrTMId', Max35Text, False)

	@property
	def TMId(self):
		return self._TMId

	@TMId.setter
	def TMId(self, value):
		self._TMId = value if value is not None else base_types.UninitialisedField(self, 'TMId', Max35Text, False)

	@TMId.deleter
	def TMId(self):
		del self._TMId
		self._TMId = base_types.UninitialisedField(self, 'TMId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MstrTMId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))