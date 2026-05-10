from . import base_types
from .EqualisationMethodologyType1Code import EqualisationMethodologyType1Code
from .RelatedSubscription1 import RelatedSubscription1

class EqualisationMethodologyType2(base_types._BaseFieldType):

	__slots__ = ["_RltdSbcpt", "_EqulstnMthdlgyTpCd"]
	@property
	def RltdSbcpt(self):
		return self._RltdSbcpt

	@RltdSbcpt.setter
	def RltdSbcpt(self, value):
		self._RltdSbcpt = value if type(value) != base_types.auto else self.make_default("RltdSbcpt")

	@RltdSbcpt.deleter
	def RltdSbcpt(self):
		del self._RltdSbcpt
		self._RltdSbcpt = None

	@property
	def EqulstnMthdlgyTpCd(self):
		return self._EqulstnMthdlgyTpCd

	@EqulstnMthdlgyTpCd.setter
	def EqulstnMthdlgyTpCd(self, value):
		self._EqulstnMthdlgyTpCd = value if type(value) != base_types.auto else self.make_default("EqulstnMthdlgyTpCd")

	@EqulstnMthdlgyTpCd.deleter
	def EqulstnMthdlgyTpCd(self):
		del self._EqulstnMthdlgyTpCd
		self._EqulstnMthdlgyTpCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdSbcpt', type=RelatedSubscription1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EqulstnMthdlgyTpCd', type=EqualisationMethodologyType1Code, min=1, max=1, mutex_group=None, array=False),
	))

