# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Max35Text
from . import PartyType20Code

class ProgrammeMode7(base_types._BaseFieldType):

	__slots__ = ["_ApldId", "_IdSelctdBy", "_NtlData", "_PropsdId", "_PrvtData"]
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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

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

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdSelctdBy', type=PartyType20Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PropsdId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
	))