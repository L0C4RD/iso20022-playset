# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralData33 import CollateralData33
from ._OrganisationIdentification15Choice import OrganisationIdentification15Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class PositionSetDimensions12(base_types._BaseFieldType):

	__slots__ = ["_CollData", "_OtlrsIncl", "_RptgCtrPty"]
	@property
	def CollData(self):
		return self._CollData

	@CollData.setter
	def CollData(self, value):
		self._CollData = value if type(value) != base_types.auto else self.make_default("CollData")

	@CollData.deleter
	def CollData(self):
		del self._CollData
		self._CollData = None

	@property
	def OtlrsIncl(self):
		return self._OtlrsIncl

	@OtlrsIncl.setter
	def OtlrsIncl(self, value):
		self._OtlrsIncl = value if type(value) != base_types.auto else self.make_default("OtlrsIncl")

	@OtlrsIncl.deleter
	def OtlrsIncl(self):
		del self._OtlrsIncl
		self._OtlrsIncl = None

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != base_types.auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollData', type=CollateralData33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OtlrsIncl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))