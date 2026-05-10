from . import base_types
from ._RiskReductionService1Code import RiskReductionService1Code
from ._OrganisationIdentification15Choice import OrganisationIdentification15Choice

class PTRREvent2(base_types._BaseFieldType):

	__slots__ = ["_SvcPrvdr", "_Tchnq"]
	@property
	def SvcPrvdr(self):
		return self._SvcPrvdr

	@SvcPrvdr.setter
	def SvcPrvdr(self, value):
		self._SvcPrvdr = value if type(value) != base_types.auto else self.make_default("SvcPrvdr")

	@SvcPrvdr.deleter
	def SvcPrvdr(self):
		del self._SvcPrvdr
		self._SvcPrvdr = None

	@property
	def Tchnq(self):
		return self._Tchnq

	@Tchnq.setter
	def Tchnq(self, value):
		self._Tchnq = value if type(value) != base_types.auto else self.make_default("Tchnq")

	@Tchnq.deleter
	def Tchnq(self):
		del self._Tchnq
		self._Tchnq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcPrvdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tchnq', type=RiskReductionService1Code, min=1, max=1, mutex_group=None, array=False),
	))

