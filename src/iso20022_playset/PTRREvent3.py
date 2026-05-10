from . import base_types
import OrganisationIdentification15Choice
import RiskReductionService1Code

class PTRREvent3(base_types._BaseFieldType):

	__slots__ = ["_Tchnq", "_SvcPrvdr"]
	@property
	def Tchnq(self):
		return self._Tchnq

	@Tchnq.setter
	def Tchnq(self, value):
		self._Tchnq = value if type(value) != auto else self.make_default("Tchnq")

	@Tchnq.deleter
	def Tchnq(self):
		del self._Tchnq
		self._Tchnq = None

	@property
	def SvcPrvdr(self):
		return self._SvcPrvdr

	@SvcPrvdr.setter
	def SvcPrvdr(self, value):
		self._SvcPrvdr = value if type(value) != auto else self.make_default("SvcPrvdr")

	@SvcPrvdr.deleter
	def SvcPrvdr(self):
		del self._SvcPrvdr
		self._SvcPrvdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tchnq', type=RiskReductionService1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcPrvdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))

