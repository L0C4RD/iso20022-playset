# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralData33
from . import OrganisationIdentification15Choice
from . import TrueFalseIndicator

class PositionSetDimensions12(base_types._BaseFieldType):

	__slots__ = ["_CollData", "_OtlrsIncl", "_RptgCtrPty"]
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
	def OtlrsIncl(self):
		return self._OtlrsIncl

	@OtlrsIncl.setter
	def OtlrsIncl(self, value):
		self._OtlrsIncl = value if value is not None else base_types.UninitialisedField(self, 'OtlrsIncl', TrueFalseIndicator, False)

	@OtlrsIncl.deleter
	def OtlrsIncl(self):
		del self._OtlrsIncl
		self._OtlrsIncl = base_types.UninitialisedField(self, 'OtlrsIncl', TrueFalseIndicator, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', OrganisationIdentification15Choice, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', OrganisationIdentification15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollData', type=CollateralData33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OtlrsIncl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))