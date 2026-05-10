from . import base_types
from ._Max52Text import Max52Text
from ._TrueFalseIndicator import TrueFalseIndicator
from ._OrganisationIdentification15Choice import OrganisationIdentification15Choice

class PositionSetDimensions15(base_types._BaseFieldType):

	__slots__ = ["_CollPrtflId", "_OtlrsIncl", "_RptgCtrPty", "_OthrCtrPty"]
	@property
	def CollPrtflId(self):
		return self._CollPrtflId

	@CollPrtflId.setter
	def CollPrtflId(self, value):
		self._CollPrtflId = value if type(value) != base_types.auto else self.make_default("CollPrtflId")

	@CollPrtflId.deleter
	def CollPrtflId(self):
		del self._CollPrtflId
		self._CollPrtflId = None

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

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != base_types.auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrtflId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OtlrsIncl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))

