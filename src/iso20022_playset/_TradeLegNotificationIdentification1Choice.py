# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import UTIIdentifier

class TradeLegNotificationIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_TradLegNtfctnId", "_UnqTxIdr"]
	@property
	def TradLegNtfctnId(self):
		return self._TradLegNtfctnId

	@TradLegNtfctnId.setter
	def TradLegNtfctnId(self, value):
		self._TradLegNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'TradLegNtfctnId', Max35Text, False)

	@TradLegNtfctnId.deleter
	def TradLegNtfctnId(self):
		del self._TradLegNtfctnId
		self._TradLegNtfctnId = base_types.UninitialisedField(self, 'TradLegNtfctnId', Max35Text, False)

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradLegNtfctnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
	))