# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrganisationIdentification15Choice

class SettlementParties34Choice(base_types._BaseFieldType):

	__slots__ = ["_CntrlSctiesDpstryPtcpt", "_IndrctPtcpt"]
	@property
	def CntrlSctiesDpstryPtcpt(self):
		return self._CntrlSctiesDpstryPtcpt

	@CntrlSctiesDpstryPtcpt.setter
	def CntrlSctiesDpstryPtcpt(self, value):
		self._CntrlSctiesDpstryPtcpt = value if value is not None else base_types.UninitialisedField(self, 'CntrlSctiesDpstryPtcpt', OrganisationIdentification15Choice, False)

	@CntrlSctiesDpstryPtcpt.deleter
	def CntrlSctiesDpstryPtcpt(self):
		del self._CntrlSctiesDpstryPtcpt
		self._CntrlSctiesDpstryPtcpt = base_types.UninitialisedField(self, 'CntrlSctiesDpstryPtcpt', OrganisationIdentification15Choice, False)

	@property
	def IndrctPtcpt(self):
		return self._IndrctPtcpt

	@IndrctPtcpt.setter
	def IndrctPtcpt(self, value):
		self._IndrctPtcpt = value if value is not None else base_types.UninitialisedField(self, 'IndrctPtcpt', OrganisationIdentification15Choice, False)

	@IndrctPtcpt.deleter
	def IndrctPtcpt(self):
		del self._IndrctPtcpt
		self._IndrctPtcpt = base_types.UninitialisedField(self, 'IndrctPtcpt', OrganisationIdentification15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrlSctiesDpstryPtcpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndrctPtcpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=1, array=False),
	))