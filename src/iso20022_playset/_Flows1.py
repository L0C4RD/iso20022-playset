# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102

class Flows1(base_types._BaseFieldType):

	__slots__ = ["_InvstmtFlows", "_PmtBkFlows"]
	@property
	def InvstmtFlows(self):
		return self._InvstmtFlows

	@InvstmtFlows.setter
	def InvstmtFlows(self, value):
		self._InvstmtFlows = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFlows', AmountAndDirection102, False)

	@InvstmtFlows.deleter
	def InvstmtFlows(self):
		del self._InvstmtFlows
		self._InvstmtFlows = base_types.UninitialisedField(self, 'InvstmtFlows', AmountAndDirection102, False)

	@property
	def PmtBkFlows(self):
		return self._PmtBkFlows

	@PmtBkFlows.setter
	def PmtBkFlows(self, value):
		self._PmtBkFlows = value if value is not None else base_types.UninitialisedField(self, 'PmtBkFlows', AmountAndDirection102, False)

	@PmtBkFlows.deleter
	def PmtBkFlows(self):
		del self._PmtBkFlows
		self._PmtBkFlows = base_types.UninitialisedField(self, 'PmtBkFlows', AmountAndDirection102, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtFlows', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtBkFlows', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))