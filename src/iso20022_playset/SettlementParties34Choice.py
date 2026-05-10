import base_types
import OrganisationIdentification15Choice

class SettlementParties34Choice(base_types._BaseFieldType):

	__slots__ = ["_CntrlSctiesDpstryPtcpt", "_IndrctPtcpt"]
	@property
	def CntrlSctiesDpstryPtcpt(self):
		return self._CntrlSctiesDpstryPtcpt

	@CntrlSctiesDpstryPtcpt.setter
	def CntrlSctiesDpstryPtcpt(self, value):
		self._CntrlSctiesDpstryPtcpt = value if type(value) != auto else self.make_default("CntrlSctiesDpstryPtcpt")

	@CntrlSctiesDpstryPtcpt.deleter
	def CntrlSctiesDpstryPtcpt(self):
		del self._CntrlSctiesDpstryPtcpt
		self._CntrlSctiesDpstryPtcpt = None

	@property
	def IndrctPtcpt(self):
		return self._IndrctPtcpt

	@IndrctPtcpt.setter
	def IndrctPtcpt(self, value):
		self._IndrctPtcpt = value if type(value) != auto else self.make_default("IndrctPtcpt")

	@IndrctPtcpt.deleter
	def IndrctPtcpt(self):
		del self._IndrctPtcpt
		self._IndrctPtcpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrlSctiesDpstryPtcpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndrctPtcpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=1, array=False),
	))

