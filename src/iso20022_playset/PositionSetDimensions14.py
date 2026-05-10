import base_types
import CollateralData33
import TrueFalseIndicator
import LoanData134
import CounterpartyData86

class PositionSetDimensions14(base_types._BaseFieldType):

	__slots__ = ["_OtlrsIncl", "_CollData", "_LnData", "_CtrPtyData"]
	@property
	def OtlrsIncl(self):
		return self._OtlrsIncl

	@OtlrsIncl.setter
	def OtlrsIncl(self, value):
		self._OtlrsIncl = value if type(value) != auto else self.make_default("OtlrsIncl")

	@OtlrsIncl.deleter
	def OtlrsIncl(self):
		del self._OtlrsIncl
		self._OtlrsIncl = None

	@property
	def CollData(self):
		return self._CollData

	@CollData.setter
	def CollData(self, value):
		self._CollData = value if type(value) != auto else self.make_default("CollData")

	@CollData.deleter
	def CollData(self):
		del self._CollData
		self._CollData = None

	@property
	def LnData(self):
		return self._LnData

	@LnData.setter
	def LnData(self, value):
		self._LnData = value if type(value) != auto else self.make_default("LnData")

	@LnData.deleter
	def LnData(self):
		del self._LnData
		self._LnData = None

	@property
	def CtrPtyData(self):
		return self._CtrPtyData

	@CtrPtyData.setter
	def CtrPtyData(self, value):
		self._CtrPtyData = value if type(value) != auto else self.make_default("CtrPtyData")

	@CtrPtyData.deleter
	def CtrPtyData(self):
		del self._CtrPtyData
		self._CtrPtyData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OtlrsIncl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollData', type=CollateralData33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnData', type=LoanData134, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyData', type=CounterpartyData86, min=0, max=1, mutex_group=None, array=False),
	))

