# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeConfirmation4
from . import TradeNonConfirmation1

class TradeConfirmation3Choice(base_types._BaseFieldType):

	__slots__ = ["_Confd", "_NonConfd"]
	@property
	def Confd(self):
		return self._Confd

	@Confd.setter
	def Confd(self, value):
		self._Confd = value if value is not None else base_types.UninitialisedField(self, 'Confd', TradeConfirmation4, False)

	@Confd.deleter
	def Confd(self):
		del self._Confd
		self._Confd = base_types.UninitialisedField(self, 'Confd', TradeConfirmation4, False)

	@property
	def NonConfd(self):
		return self._NonConfd

	@NonConfd.setter
	def NonConfd(self, value):
		self._NonConfd = value if value is not None else base_types.UninitialisedField(self, 'NonConfd', TradeNonConfirmation1, False)

	@NonConfd.deleter
	def NonConfd(self):
		del self._NonConfd
		self._NonConfd = base_types.UninitialisedField(self, 'NonConfd', TradeNonConfirmation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Confd', type=TradeConfirmation4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonConfd', type=TradeNonConfirmation1, min=0, max=1, mutex_group=1, array=False),
	))