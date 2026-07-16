# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerOrder1
from . import LoyaltyRequestData3
from . import LoyaltyTransaction8

class LoyaltyRequest8(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_Data", "_Tx"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', LoyaltyRequestData3, True)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', LoyaltyRequestData3, True)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', LoyaltyTransaction8, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', LoyaltyTransaction8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=LoyaltyRequestData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=LoyaltyTransaction8, min=1, max=1, mutex_group=None, array=False),
	))