# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData2
from . import FleetLineItem6

class AddendumData7(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_FleetLineItm"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData2, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData2, True)

	@property
	def FleetLineItm(self):
		return self._FleetLineItm

	@FleetLineItm.setter
	def FleetLineItm(self, value):
		self._FleetLineItm = value if value is not None else base_types.UninitialisedField(self, 'FleetLineItm', FleetLineItem6, True)

	@FleetLineItm.deleter
	def FleetLineItm(self):
		del self._FleetLineItm
		self._FleetLineItm = base_types.UninitialisedField(self, 'FleetLineItm', FleetLineItem6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FleetLineItm', type=FleetLineItem6, min=0, max=None, mutex_group=None, array=True),
	))