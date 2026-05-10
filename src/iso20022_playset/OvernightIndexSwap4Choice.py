import base_types
import ReportPeriodActivity3Code
import OvernightIndexSwapTransaction4

class OvernightIndexSwap4Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_Tx"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if type(value) != auto else self.make_default("DataSetActn")

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = None

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
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tx', type=OvernightIndexSwapTransaction4, min=1, max=None, mutex_group=1, array=True),
	))

