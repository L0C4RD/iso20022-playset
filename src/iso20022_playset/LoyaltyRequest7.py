import base_types
import LoyaltyTransaction7
import LoyaltyRequestData3
import CustomerOrder1

class LoyaltyRequest7(base_types._BaseFieldType):

	__slots__ = ["_Data", "_CstmrOrdr", "_Tx"]
	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Data', type=LoyaltyRequestData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=LoyaltyTransaction7, min=1, max=1, mutex_group=None, array=False),
	))

