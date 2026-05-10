import base_types
import DecimalNumber
import Number
import FromToQuantityRange2

class TransactionsBin2(base_types._BaseFieldType):

	__slots__ = ["_Rg", "_TtlNtnlAmt", "_NbOfTxs"]
	@property
	def Rg(self):
		return self._Rg

	@Rg.setter
	def Rg(self, value):
		self._Rg = value if type(value) != auto else self.make_default("Rg")

	@Rg.deleter
	def Rg(self):
		del self._Rg
		self._Rg = None

	@property
	def TtlNtnlAmt(self):
		return self._TtlNtnlAmt

	@TtlNtnlAmt.setter
	def TtlNtnlAmt(self, value):
		self._TtlNtnlAmt = value if type(value) != auto else self.make_default("TtlNtnlAmt")

	@TtlNtnlAmt.deleter
	def TtlNtnlAmt(self):
		del self._TtlNtnlAmt
		self._TtlNtnlAmt = None

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rg', type=FromToQuantityRange2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNtnlAmt', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

