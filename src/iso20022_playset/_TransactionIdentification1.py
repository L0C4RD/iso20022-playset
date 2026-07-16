# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINMax35Text

class TransactionIdentification1(base_types._BaseFieldType):

	__slots__ = ["_MktInfrstrctrTxId"]
	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', RestrictedFINMax35Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', RestrictedFINMax35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=RestrictedFINMax35Text, min=1, max=1, mutex_group=None, array=False),
	))