# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Max16Text

class Terminal8(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_Id"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', AdditionalData1, True)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', AdditionalData1, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max16Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
	))