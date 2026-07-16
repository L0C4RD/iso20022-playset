# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EqualisationMethodologyType1Code
from . import RelatedSubscription1

class EqualisationMethodologyType2(base_types._BaseFieldType):

	__slots__ = ["_EqulstnMthdlgyTpCd", "_RltdSbcpt"]
	@property
	def EqulstnMthdlgyTpCd(self):
		return self._EqulstnMthdlgyTpCd

	@EqulstnMthdlgyTpCd.setter
	def EqulstnMthdlgyTpCd(self, value):
		self._EqulstnMthdlgyTpCd = value if value is not None else base_types.UninitialisedField(self, 'EqulstnMthdlgyTpCd', EqualisationMethodologyType1Code, False)

	@EqulstnMthdlgyTpCd.deleter
	def EqulstnMthdlgyTpCd(self):
		del self._EqulstnMthdlgyTpCd
		self._EqulstnMthdlgyTpCd = base_types.UninitialisedField(self, 'EqulstnMthdlgyTpCd', EqualisationMethodologyType1Code, False)

	@property
	def RltdSbcpt(self):
		return self._RltdSbcpt

	@RltdSbcpt.setter
	def RltdSbcpt(self, value):
		self._RltdSbcpt = value if value is not None else base_types.UninitialisedField(self, 'RltdSbcpt', RelatedSubscription1, True)

	@RltdSbcpt.deleter
	def RltdSbcpt(self):
		del self._RltdSbcpt
		self._RltdSbcpt = base_types.UninitialisedField(self, 'RltdSbcpt', RelatedSubscription1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EqulstnMthdlgyTpCd', type=EqualisationMethodologyType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSbcpt', type=RelatedSubscription1, min=0, max=None, mutex_group=None, array=True),
	))