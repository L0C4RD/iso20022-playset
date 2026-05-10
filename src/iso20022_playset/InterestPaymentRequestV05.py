import base_types
import Max35Text
import SupplementaryData1
import InterestAmount4
import Agreement4
import InterestResult1
import Obligation9

class InterestPaymentRequestV05(base_types._BaseFieldType):

	__slots__ = ["_IntrstDueToA", "_IntrstDueToB", "_SplmtryData", "_Agrmt", "_NetAmtDtls", "_TxId", "_Oblgtn"]
	@property
	def IntrstDueToA(self):
		return self._IntrstDueToA

	@IntrstDueToA.setter
	def IntrstDueToA(self, value):
		self._IntrstDueToA = value if type(value) != auto else self.make_default("IntrstDueToA")

	@IntrstDueToA.deleter
	def IntrstDueToA(self):
		del self._IntrstDueToA
		self._IntrstDueToA = None

	@property
	def IntrstDueToB(self):
		return self._IntrstDueToB

	@IntrstDueToB.setter
	def IntrstDueToB(self, value):
		self._IntrstDueToB = value if type(value) != auto else self.make_default("IntrstDueToB")

	@IntrstDueToB.deleter
	def IntrstDueToB(self):
		del self._IntrstDueToB
		self._IntrstDueToB = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if type(value) != auto else self.make_default("Agrmt")

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = None

	@property
	def NetAmtDtls(self):
		return self._NetAmtDtls

	@NetAmtDtls.setter
	def NetAmtDtls(self, value):
		self._NetAmtDtls = value if type(value) != auto else self.make_default("NetAmtDtls")

	@NetAmtDtls.deleter
	def NetAmtDtls(self):
		del self._NetAmtDtls
		self._NetAmtDtls = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if type(value) != auto else self.make_default("Oblgtn")

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstDueToA', type=InterestAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstDueToB', type=InterestAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmtDtls', type=InterestResult1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation9, min=1, max=1, mutex_group=None, array=False),
	))

