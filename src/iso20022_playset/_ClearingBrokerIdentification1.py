# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import SideIndicator1Code

class ClearingBrokerIdentification1(base_types._BaseFieldType):

	__slots__ = ["_ClrBrkrId", "_SdInd"]
	@property
	def ClrBrkrId(self):
		return self._ClrBrkrId

	@ClrBrkrId.setter
	def ClrBrkrId(self, value):
		self._ClrBrkrId = value if value is not None else base_types.UninitialisedField(self, 'ClrBrkrId', Max35Text, False)

	@ClrBrkrId.deleter
	def ClrBrkrId(self):
		del self._ClrBrkrId
		self._ClrBrkrId = base_types.UninitialisedField(self, 'ClrBrkrId', Max35Text, False)

	@property
	def SdInd(self):
		return self._SdInd

	@SdInd.setter
	def SdInd(self, value):
		self._SdInd = value if value is not None else base_types.UninitialisedField(self, 'SdInd', SideIndicator1Code, False)

	@SdInd.deleter
	def SdInd(self):
		del self._SdInd
		self._SdInd = base_types.UninitialisedField(self, 'SdInd', SideIndicator1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrBrkrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SdInd', type=SideIndicator1Code, min=1, max=1, mutex_group=None, array=False),
	))