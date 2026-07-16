# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Max35Text
from . import PartyType20Code

class ProgrammeMode4(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_ApldId", "_IdSelctdBy", "_PropsdId"]
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
	def ApldId(self):
		return self._ApldId

	@ApldId.setter
	def ApldId(self, value):
		self._ApldId = value if value is not None else base_types.UninitialisedField(self, 'ApldId', Max35Text, False)

	@ApldId.deleter
	def ApldId(self):
		del self._ApldId
		self._ApldId = base_types.UninitialisedField(self, 'ApldId', Max35Text, False)

	@property
	def IdSelctdBy(self):
		return self._IdSelctdBy

	@IdSelctdBy.setter
	def IdSelctdBy(self, value):
		self._IdSelctdBy = value if value is not None else base_types.UninitialisedField(self, 'IdSelctdBy', PartyType20Code, False)

	@IdSelctdBy.deleter
	def IdSelctdBy(self):
		del self._IdSelctdBy
		self._IdSelctdBy = base_types.UninitialisedField(self, 'IdSelctdBy', PartyType20Code, False)

	@property
	def PropsdId(self):
		return self._PropsdId

	@PropsdId.setter
	def PropsdId(self, value):
		self._PropsdId = value if value is not None else base_types.UninitialisedField(self, 'PropsdId', Max35Text, True)

	@PropsdId.deleter
	def PropsdId(self):
		del self._PropsdId
		self._PropsdId = base_types.UninitialisedField(self, 'PropsdId', Max35Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApldId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdSelctdBy', type=PartyType20Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))