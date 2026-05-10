import base_types
import ISODate
import Percentage14Rate
import Number
import FinancialInstrumentQuantity18Choice

class Participation6(base_types._BaseFieldType):

	__slots__ = ["_PctgOfVtngRghts", "_ClctnDt", "_TtlNbOfSctiesOutsdng", "_TtlNbOfVtngRghts"]
	@property
	def PctgOfVtngRghts(self):
		return self._PctgOfVtngRghts

	@PctgOfVtngRghts.setter
	def PctgOfVtngRghts(self, value):
		self._PctgOfVtngRghts = value if type(value) != auto else self.make_default("PctgOfVtngRghts")

	@PctgOfVtngRghts.deleter
	def PctgOfVtngRghts(self):
		del self._PctgOfVtngRghts
		self._PctgOfVtngRghts = None

	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if type(value) != auto else self.make_default("ClctnDt")

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = None

	@property
	def TtlNbOfSctiesOutsdng(self):
		return self._TtlNbOfSctiesOutsdng

	@TtlNbOfSctiesOutsdng.setter
	def TtlNbOfSctiesOutsdng(self, value):
		self._TtlNbOfSctiesOutsdng = value if type(value) != auto else self.make_default("TtlNbOfSctiesOutsdng")

	@TtlNbOfSctiesOutsdng.deleter
	def TtlNbOfSctiesOutsdng(self):
		del self._TtlNbOfSctiesOutsdng
		self._TtlNbOfSctiesOutsdng = None

	@property
	def TtlNbOfVtngRghts(self):
		return self._TtlNbOfVtngRghts

	@TtlNbOfVtngRghts.setter
	def TtlNbOfVtngRghts(self, value):
		self._TtlNbOfVtngRghts = value if type(value) != auto else self.make_default("TtlNbOfVtngRghts")

	@TtlNbOfVtngRghts.deleter
	def TtlNbOfVtngRghts(self):
		del self._TtlNbOfVtngRghts
		self._TtlNbOfVtngRghts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PctgOfVtngRghts', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfSctiesOutsdng', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfVtngRghts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

