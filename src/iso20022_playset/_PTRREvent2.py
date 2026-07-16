# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrganisationIdentification15Choice
from . import RiskReductionService1Code

class PTRREvent2(base_types._BaseFieldType):

	__slots__ = ["_SvcPrvdr", "_Tchnq"]
	@property
	def SvcPrvdr(self):
		return self._SvcPrvdr

	@SvcPrvdr.setter
	def SvcPrvdr(self, value):
		self._SvcPrvdr = value if value is not None else base_types.UninitialisedField(self, 'SvcPrvdr', OrganisationIdentification15Choice, False)

	@SvcPrvdr.deleter
	def SvcPrvdr(self):
		del self._SvcPrvdr
		self._SvcPrvdr = base_types.UninitialisedField(self, 'SvcPrvdr', OrganisationIdentification15Choice, False)

	@property
	def Tchnq(self):
		return self._Tchnq

	@Tchnq.setter
	def Tchnq(self, value):
		self._Tchnq = value if value is not None else base_types.UninitialisedField(self, 'Tchnq', RiskReductionService1Code, False)

	@Tchnq.deleter
	def Tchnq(self):
		del self._Tchnq
		self._Tchnq = base_types.UninitialisedField(self, 'Tchnq', RiskReductionService1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcPrvdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tchnq', type=RiskReductionService1Code, min=1, max=1, mutex_group=None, array=False),
	))