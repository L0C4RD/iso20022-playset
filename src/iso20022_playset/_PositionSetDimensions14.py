# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralData33
from . import CounterpartyData86
from . import LoanData134
from . import TrueFalseIndicator

class PositionSetDimensions14(base_types._BaseFieldType):

	__slots__ = ["_CollData", "_CtrPtyData", "_LnData", "_OtlrsIncl"]
	@property
	def CollData(self):
		return self._CollData

	@CollData.setter
	def CollData(self, value):
		self._CollData = value if value is not None else base_types.UninitialisedField(self, 'CollData', CollateralData33, False)

	@CollData.deleter
	def CollData(self):
		del self._CollData
		self._CollData = base_types.UninitialisedField(self, 'CollData', CollateralData33, False)

	@property
	def CtrPtyData(self):
		return self._CtrPtyData

	@CtrPtyData.setter
	def CtrPtyData(self, value):
		self._CtrPtyData = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyData', CounterpartyData86, False)

	@CtrPtyData.deleter
	def CtrPtyData(self):
		del self._CtrPtyData
		self._CtrPtyData = base_types.UninitialisedField(self, 'CtrPtyData', CounterpartyData86, False)

	@property
	def LnData(self):
		return self._LnData

	@LnData.setter
	def LnData(self, value):
		self._LnData = value if value is not None else base_types.UninitialisedField(self, 'LnData', LoanData134, False)

	@LnData.deleter
	def LnData(self):
		del self._LnData
		self._LnData = base_types.UninitialisedField(self, 'LnData', LoanData134, False)

	@property
	def OtlrsIncl(self):
		return self._OtlrsIncl

	@OtlrsIncl.setter
	def OtlrsIncl(self, value):
		self._OtlrsIncl = value if value is not None else base_types.UninitialisedField(self, 'OtlrsIncl', TrueFalseIndicator, False)

	@OtlrsIncl.deleter
	def OtlrsIncl(self):
		del self._OtlrsIncl
		self._OtlrsIncl = base_types.UninitialisedField(self, 'OtlrsIncl', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollData', type=CollateralData33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyData', type=CounterpartyData86, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnData', type=LoanData134, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OtlrsIncl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))