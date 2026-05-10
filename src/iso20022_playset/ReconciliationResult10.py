import base_types
import OrganisationIdentification15Choice
import MatchingCriteria10

class ReconciliationResult10(base_types._BaseFieldType):

	__slots__ = ["_CtrPty2", "_MtchgCrit", "_CtrPty1"]
	@property
	def CtrPty2(self):
		return self._CtrPty2

	@CtrPty2.setter
	def CtrPty2(self, value):
		self._CtrPty2 = value if type(value) != auto else self.make_default("CtrPty2")

	@CtrPty2.deleter
	def CtrPty2(self):
		del self._CtrPty2
		self._CtrPty2 = None

	@property
	def MtchgCrit(self):
		return self._MtchgCrit

	@MtchgCrit.setter
	def MtchgCrit(self, value):
		self._MtchgCrit = value if type(value) != auto else self.make_default("MtchgCrit")

	@MtchgCrit.deleter
	def MtchgCrit(self):
		del self._MtchgCrit
		self._MtchgCrit = None

	@property
	def CtrPty1(self):
		return self._CtrPty1

	@CtrPty1.setter
	def CtrPty1(self, value):
		self._CtrPty1 = value if type(value) != auto else self.make_default("CtrPty1")

	@CtrPty1.deleter
	def CtrPty1(self):
		del self._CtrPty1
		self._CtrPty1 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPty2', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgCrit', type=MatchingCriteria10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty1', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
	))

