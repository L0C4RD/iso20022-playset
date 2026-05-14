# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._UTIIdentifier import UTIIdentifier

class TradeLegNotificationIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_TradLegNtfctnId", "_UnqTxIdr"]
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

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradLegNtfctnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
	))