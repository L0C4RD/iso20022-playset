from . import base_types
from .CompareCounterpartySide2 import CompareCounterpartySide2
from .CompareOrganisationIdentification7 import CompareOrganisationIdentification7
from .CompareOrganisationIdentification6 import CompareOrganisationIdentification6

class CounterpartyMatchingCriteria4(base_types._BaseFieldType):

	__slots__ = ["_OthrCtrPty", "_RptgCtrPty", "_CtrPtySd"]
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
	def CtrPtySd(self):
		return self._CtrPtySd

	@CtrPtySd.setter
	def CtrPtySd(self, value):
		self._CtrPtySd = value if type(value) != base_types.auto else self.make_default("CtrPtySd")

	@CtrPtySd.deleter
	def CtrPtySd(self):
		del self._CtrPtySd
		self._CtrPtySd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrCtrPty', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=CompareOrganisationIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySd', type=CompareCounterpartySide2, min=0, max=1, mutex_group=None, array=False),
	))

