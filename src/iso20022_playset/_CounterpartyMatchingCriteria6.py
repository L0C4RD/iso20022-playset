# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareLegDirection2
from . import CompareOrganisationIdentification6
from . import CompareOrganisationIdentification7

class CounterpartyMatchingCriteria6(base_types._BaseFieldType):

	__slots__ = ["_DrctnOrSd", "_OthrCtrPty", "_RptgCtrPty"]
	@property
	def DrctnOrSd(self):
		return self._DrctnOrSd

	@DrctnOrSd.setter
	def DrctnOrSd(self, value):
		self._DrctnOrSd = value if value is not None else base_types.UninitialisedField(self, 'DrctnOrSd', CompareLegDirection2, False)

	@DrctnOrSd.deleter
	def DrctnOrSd(self):
		del self._DrctnOrSd
		self._DrctnOrSd = base_types.UninitialisedField(self, 'DrctnOrSd', CompareLegDirection2, False)

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', CompareOrganisationIdentification7, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', CompareOrganisationIdentification7, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', CompareOrganisationIdentification6, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', CompareOrganisationIdentification6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrctnOrSd', type=CompareLegDirection2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=CompareOrganisationIdentification6, min=0, max=1, mutex_group=None, array=False),
	))