from . import base_types
from ._CompareOrganisationIdentification6 import CompareOrganisationIdentification6
from ._CompareOrganisationIdentification7 import CompareOrganisationIdentification7
from ._CompareLegDirection2 import CompareLegDirection2

class CounterpartyMatchingCriteria6(base_types._BaseFieldType):

	__slots__ = ["_RptgCtrPty", "_DrctnOrSd", "_OthrCtrPty"]
	@property
	def DrctnOrSd(self):
		return self._DrctnOrSd

	@DrctnOrSd.setter
	def DrctnOrSd(self, value):
		self._DrctnOrSd = value if type(value) != base_types.auto else self.make_default("DrctnOrSd")

	@DrctnOrSd.deleter
	def DrctnOrSd(self):
		del self._DrctnOrSd
		self._DrctnOrSd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrctnOrSd', type=CompareLegDirection2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=CompareOrganisationIdentification6, min=0, max=1, mutex_group=None, array=False),
	))

