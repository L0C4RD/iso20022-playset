# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TradeLegNotificationIdentification1Choice

class Reference24(base_types._BaseFieldType):

	__slots__ = ["_NetPosId", "_TradLegNtfctnId"]
	@property
	def NetPosId(self):
		return self._NetPosId

	@NetPosId.setter
	def NetPosId(self, value):
		self._NetPosId = value if value is not None else base_types.UninitialisedField(self, 'NetPosId', Max35Text, False)

	@NetPosId.deleter
	def NetPosId(self):
		del self._NetPosId
		self._NetPosId = base_types.UninitialisedField(self, 'NetPosId', Max35Text, False)

	@property
	def TradLegNtfctnId(self):
		return self._TradLegNtfctnId

	@TradLegNtfctnId.setter
	def TradLegNtfctnId(self, value):
		self._TradLegNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'TradLegNtfctnId', TradeLegNotificationIdentification1Choice, True)

	@TradLegNtfctnId.deleter
	def TradLegNtfctnId(self):
		del self._TradLegNtfctnId
		self._TradLegNtfctnId = base_types.UninitialisedField(self, 'TradLegNtfctnId', TradeLegNotificationIdentification1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetPosId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegNtfctnId', type=TradeLegNotificationIdentification1Choice, min=0, max=None, mutex_group=None, array=True),
	))