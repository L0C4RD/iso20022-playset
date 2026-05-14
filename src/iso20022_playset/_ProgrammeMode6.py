# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Max35Text import Max35Text

class ProgrammeMode6(base_types._BaseFieldType):

	__slots__ = ["_ApldId", "_NtlData", "_PropsdId", "_PrvtData"]
	@property
	def ApldId(self):
		return self._ApldId

	@ApldId.setter
	def ApldId(self, value):
		self._ApldId = value if type(value) != base_types.auto else self.make_default("ApldId")

	@ApldId.deleter
	def ApldId(self):
		del self._ApldId
		self._ApldId = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PropsdId(self):
		return self._PropsdId

	@PropsdId.setter
	def PropsdId(self, value):
		self._PropsdId = value if type(value) != base_types.auto else self.make_default("PropsdId")

	@PropsdId.deleter
	def PropsdId(self):
		del self._PropsdId
		self._PropsdId = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PropsdId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
	))