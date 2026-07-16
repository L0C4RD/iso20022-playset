# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AggregateHoldingBalance1
from . import Intermediary29

class AggregateHoldingBalance3(base_types._BaseFieldType):

	__slots__ = ["_Agt", "_BalForAcct"]
	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if value is not None else base_types.UninitialisedField(self, 'Agt', Intermediary29, True)

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = base_types.UninitialisedField(self, 'Agt', Intermediary29, True)

	@property
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if value is not None else base_types.UninitialisedField(self, 'BalForAcct', AggregateHoldingBalance1, True)

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = base_types.UninitialisedField(self, 'BalForAcct', AggregateHoldingBalance1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agt', type=Intermediary29, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalForAcct', type=AggregateHoldingBalance1, min=1, max=None, mutex_group=None, array=True),
	))