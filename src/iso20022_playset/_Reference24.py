from . import base_types
from ._Max35Text import Max35Text
from ._TradeLegNotificationIdentification1Choice import TradeLegNotificationIdentification1Choice

class Reference24(base_types._BaseFieldType):

	__slots__ = ["_NetPosId", "_TradLegNtfctnId"]
	@property
	def NetPosId(self):
		return self._NetPosId

	@NetPosId.setter
	def NetPosId(self, value):
		self._NetPosId = value if type(value) != base_types.auto else self.make_default("NetPosId")

	@NetPosId.deleter
	def NetPosId(self):
		del self._NetPosId
		self._NetPosId = None

	@property
	def TradLegNtfctnId(self):
		return self._TradLegNtfctnId

	@TradLegNtfctnId.setter
	def TradLegNtfctnId(self, value):
		self._TradLegNtfctnId = value if type(value) != base_types.auto else self.make_default("TradLegNtfctnId")

	@TradLegNtfctnId.deleter
	def TradLegNtfctnId(self):
		del self._TradLegNtfctnId
		self._TradLegNtfctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetPosId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegNtfctnId', type=TradeLegNotificationIdentification1Choice, min=0, max=None, mutex_group=None, array=True),
	))

