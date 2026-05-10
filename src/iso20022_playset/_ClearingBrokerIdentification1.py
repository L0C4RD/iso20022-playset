from . import base_types
from .Max35Text import Max35Text
from .SideIndicator1Code import SideIndicator1Code

class ClearingBrokerIdentification1(base_types._BaseFieldType):

	__slots__ = ["_ClrBrkrId", "_SdInd"]
	@property
	def ClrBrkrId(self):
		return self._ClrBrkrId

	@ClrBrkrId.setter
	def ClrBrkrId(self, value):
		self._ClrBrkrId = value if type(value) != base_types.auto else self.make_default("ClrBrkrId")

	@ClrBrkrId.deleter
	def ClrBrkrId(self):
		del self._ClrBrkrId
		self._ClrBrkrId = None

	@property
	def SdInd(self):
		return self._SdInd

	@SdInd.setter
	def SdInd(self, value):
		self._SdInd = value if type(value) != base_types.auto else self.make_default("SdInd")

	@SdInd.deleter
	def SdInd(self):
		del self._SdInd
		self._SdInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrBrkrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SdInd', type=SideIndicator1Code, min=1, max=1, mutex_group=None, array=False),
	))

